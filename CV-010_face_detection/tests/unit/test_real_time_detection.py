import unittest
import os
import sys
from unittest.mock import patch, MagicMock
import cv2

# Добавляем путь к src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

# Импортируем модуль после добавления пути
from real_time_detection import RealTimeFaceDetector

class TestRealTimeFaceDetector(unittest.TestCase):
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        # Создаем временный файл каскада
        os.makedirs('test_cascades', exist_ok=True)
        cascade_path = os.path.join('test_cascades', 'haarcascade_frontalface_default.xml')
        import shutil
        if os.path.exists('../configs/haarcascade_frontalface_default.xml'):
            shutil.copy('../configs/haarcascade_frontalface_default.xml', cascade_path)
        else:
            # Если файла нет, создаем заглушку
            with open(cascade_path, 'w') as f:
                f.write('dummy cascade content')
        
        # Сохраняем оригинальный путь к каскадам
        self.original_haarcascades = cv2.data.haarcascades
        # Меняем путь к каскадам на нашу временную директорию
        cv2.data.haarcascades = os.path.abspath('test_cascades')
    
    def tearDown(self):
        """Очистка после каждого теста"""
        import shutil
        if os.path.exists('test_cascades'):
            shutil.rmtree('test_cascades')
        # Восстанавливаем оригинальный путь
        cv2.data.haarcascades = self.original_haarcascades
    
    @patch('cv2.CascadeClassifier')
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.destroyAllWindows')
    def test_init_success(self, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_VideoCapture, mock_CascadeClassifier):
        """Тест: инициализация детектора"""
        # Настройка моков
        mock_CascadeClassifier.return_value.empty.return_value = False
        
        # Создаем детектор
        detector = RealTimeFaceDetector()
        
        # Проверяем, что CascadeClassifier был вызван с правильным путем
        expected_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
        mock_CascadeClassifier.assert_called_once_with(expected_path)
        self.assertFalse(detector.face_cascade.empty())
    
    @patch('cv2.CascadeClassifier')
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.destroyAllWindows')
    def test_init_cascade_not_found(self, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_VideoCapture, mock_CascadeClassifier):    
        """Тест: ошибка, если файл каскада не найден"""
        # Настройка моков
        mock_CascadeClassifier.side_effect = Exception('File not found')
        
        # Проверяем, что при инициализации возникает исключение
        with self.assertRaises(Exception):
            detector = RealTimeFaceDetector()
    
    @patch('cv2.CascadeClassifier')
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.destroyAllWindows')
    @patch('cv2.cvtColor')
    @patch('cv2.rectangle')
    @patch('cv2.putText')
    def test_camera_detection_success(self, mock_putText, mock_rectangle, mock_cvtColor, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_VideoCapture, mock_CascadeClassifier):
        """Тест: успешная детекция с камеры"""
        # Настройка моков
        mock_CascadeClassifier.return_value.empty.return_value = False
        mock_CascadeClassifier.return_value.detectMultiScale.return_value = [(100, 100, 50, 50)]  # Найдено одно лицо
        
        mock_cap = MagicMock()
        mock_cap.isOpened.return_value = True
        mock_cap.read.return_value = (True, "frame")  # Успешное чтение кадра
        mock_VideoCapture.return_value = mock_cap
        
        mock_cvtColor.return_value = "gray_frame"
        mock_waitKey.return_value = 0  # Не нажата 'q'
        
        # Создаем детектор и запускаем детекцию
        detector = RealTimeFaceDetector()
        detector.start_camera_detection()
        
        # Проверяем, что VideoCapture был вызван
        mock_VideoCapture.assert_called_once_with(0)
        # Проверяем, что read был вызван (успешно)
        mock_cap.read.assert_called()
        # Проверяем, что detectMultiScale был вызван
        detector.face_cascade.detectMultiScale.assert_called()
        # Проверяем, что rectangle был вызван для рисования bounding box
        mock_rectangle.assert_called()
        # Проверяем, что imshow был вызван для отображения кадра
        mock_imshow.assert_called()
        
    @patch('cv2.CascadeClassifier')
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.destroyAllWindows')
    def test_camera_open_failure(self, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_VideoCapture, mock_CascadeClassifier):
        """Тест: ошибка открытия камеры"""
        # Настройка моков
        mock_CascadeClassifier.return_value.empty.return_value = False
        
        mock_cap = MagicMock()
        mock_cap.isOpened.return_value = False
        mock_VideoCapture.return_value = mock_cap
        
        # Перехватываем print вывод
        with patch('builtins.print') as mock_print:
            # Создаем детектор и запускаем детекцию
            detector = RealTimeFaceDetector()
            detector.start_camera_detection()
            
            # Проверяем, что было напечатано сообщение об ошибке
            mock_print.assert_any_call("❌ Ошибка: Не удалось подключиться к камере")
    
    @patch('cv2.CascadeClassifier')
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.destroyAllWindows')
    def test_frame_capture_failure(self, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_VideoCapture, mock_CascadeClassifier):
        """Тест: ошибка захвата кадра"""
        # Настройка моков
        mock_CascadeClassifier.return_value.empty.return_value = False
        
        mock_cap = MagicMock()
        mock_cap.isOpened.return_value = True
        mock_cap.read.return_value = (False, None)  # Ошибка чтения кадра
        mock_VideoCapture.return_value = mock_cap
        
        # Перехватываем print вывод
        with patch('builtins.print') as mock_print:
            # Создаем детектор и запускаем детекцию
            detector = RealTimeFaceDetector()
            detector.start_camera_detection()
            
            # Проверяем, что было напечатано сообщение об ошибке
            mock_print.assert_any_call("❌ Ошибка: Не удалось захватить кадр")
    
    @patch('cv2.CascadeClassifier')
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.destroyAllWindows')
    def test_exit_on_q_press(self, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_VideoCapture, mock_CascadeClassifier):
        """Тест: выход при нажатии 'q'"""
        # Настройка моков
        mock_CascadeClassifier.return_value.empty.return_value = False
        
        mock_cap = MagicMock()
        mock_cap.isOpened.return_value = True
        mock_cap.read.return_value = (True, "frame")  # Успешное чтение кадра
        mock_VideoCapture.return_value = mock_cap
        
        # Нажата клавиша 'q'
        mock_waitKey.return_value = ord('q')
        
        # Создаем детектор и запускаем детекцию
        detector = RealTimeFaceDetector()
        detector.start_camera_detection()
        
        # Проверяем, что destroyAllWindows был вызван
        mock_destroyAllWindows.assert_called_once()

if __name__ == '__main__':
    unittest.main()