import unittest
import cv2
import numpy as np
from unittest.mock import Mock, patch
from src.qr_detector import QRDetector


class TestQRDetector(unittest.TestCase):
    """
    Тесты для класса QRDetector.
    """
    
    def setUp(self):
        """
        Инициализация перед каждым тестом.
        """
        self.detector = QRDetector()
    
    def test_detector_initialization(self):
        """
        Тест инициализации детектора.
        """
        self.assertIsNotNone(self.detector.detector)
    
    def test_detect_and_decode_with_valid_qr_code(self):
        """
        Тест распознавания валидного QR-кода.
        """
        # Создаем изображение с QR-кодом (имитация)
        with patch.object(self.detector.detector, 'detectAndDecode') as mock_detect:
            mock_detect.return_value = ("https://example.com", np.array([[[10, 10], [100, 10], [100, 100], [10, 100]]]), None)
            
            success, data, bbox = self.detector.detect_and_decode(np.zeros((400, 400, 3), dtype=np.uint8))
            
            self.assertTrue(success)
            self.assertEqual(data, "https://example.com")
            self.assertIsNotNone(bbox)
    
    def test_detect_and_decode_with_no_qr_code(self):
        """
        Тест ситуации, когда QR-код не обнаружен.
        """
        # Создаем пустое изображение
        with patch.object(self.detector.detector, 'detectAndDecode') as mock_detect:
            mock_detect.return_value = ("", None, None)
            
            success, data, bbox = self.detector.detect_and_decode(np.zeros((400, 400, 3), dtype=np.uint8))
            
            self.assertFalse(success)
            self.assertIsNone(data)
            self.assertIsNone(bbox)
    
    def test_draw_detection_with_valid_bbox(self):
        """
        Тест отрисовки рамки вокруг QR-кода.
        """
        # Создаем тестовое изображение
        frame = np.zeros((400, 400, 3), dtype=np.uint8)
        
        # Создаем bounding box
        bbox = np.array([[[10, 10], [100, 10], [100, 100], [10, 100]]])
        
        # Рисуем рамку
        result_frame = self.detector.draw_detection(frame.copy(), bbox)
        
        # Проверяем, что рамка нарисована (пиксели изменились)
        self.assertFalse(np.array_equal(frame, result_frame))
    
    def test_draw_detection_with_invalid_bbox(self):
        """
        Тест отрисовки с невалидным bounding box.
        """
        # Создаем тестовое изображение
        frame = np.zeros((400, 400, 3), dtype=np.uint8)
        
        # Рисуем рамку с None bbox
        result_frame = self.detector.draw_detection(frame.copy(), None)
        
        # Проверяем, что изображение не изменилось
        self.assertTrue(np.array_equal(frame, result_frame))


class TestSimpleQRApp(unittest.TestCase):
    """
    Тесты для класса SimpleQRApp.
    """
    
    @patch('cv2.VideoCapture')
    def test_app_initialization(self, mock_video_capture):
        """
        Тест инициализации приложения.
        """
        # Настраиваем мок
        mock_cap = Mock()
        mock_cap.isOpened.return_value = True
        mock_video_capture.return_value = mock_cap
        
        # Создаем приложение
        app = SimpleQRApp()
        
        # Проверяем, что VideoCapture был вызван
        mock_video_capture.assert_called_once_with(0)
        self.assertEqual(app.cap, mock_cap)
    
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.destroyAllWindows')
    @patch('src.qr_detector.QRDetector')
    def test_app_start_success(self, mock_detector_class, mock_destroy, mock_wait, mock_imshow, mock_video_capture):
        """
        Тест успешного запуска приложения.
        """
        # Настраиваем моки
        mock_cap = Mock()
        mock_cap.isOpened.return_value = True
        mock_cap.read.return_value = (True, np.zeros((400, 400, 3), dtype=np.uint8))
        mock_video_capture.return_value = mock_cap
        
        mock_detector = Mock()
        mock_detector.detect_and_decode.return_value = (False, None, None)
        mock_detector_class.return_value = mock_detector
        
        # Настраиваем выход по ESC
        mock_wait.return_value = 27  # ESC
        
        # Создаем и запускаем приложение
        app = SimpleQRApp()
        app.start()
        
        # Проверяем, что ресурсы освобождены
        mock_cap.release.assert_called_once()
        mock_destroy.assert_called_once()
    
    @patch('cv2.VideoCapture')
    @patch('cv2.destroyAllWindows')
    def test_cleanup_method(self, mock_destroy, mock_video_capture):
        """
        Тест метода cleanup.
        """
        # Настраиваем мок
        mock_cap = Mock()
        mock_video_capture.return_value = mock_cap
        
        # Создаем приложение и вызываем cleanup
        app = SimpleQRApp()
        app.cap = mock_cap
        app.cleanup()
        
        # Проверяем, что ресурсы освобождены
        mock_cap.release.assert_called_once()
        mock_destroy.assert_called_once()

if __name__ == '__main__':
    unittest.main()