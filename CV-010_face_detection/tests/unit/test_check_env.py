import unittest
import sys
import os
import io
import contextlib
from unittest.mock import patch, MagicMock, mock_open
import importlib
import cv2
import src.check_env

class TestCheckEnv(unittest.TestCase):
    
    def setUp(self):
        """Создание временной директории и файлов для тестирования"""
        # Создаем временную структуру
        os.makedirs('test_static', exist_ok=True)
        with open('test_static/test.jpg', 'w') as f:
            f.write('dummy image content')
            
        # Создаем директорию configs и копируем настоящий каскад Хаара
        os.makedirs('configs', exist_ok=True)
        # Копируем настоящий файл каскада из проекта
        import shutil
        if os.path.exists('../configs/haarcascade_frontalface_default.xml'):
            shutil.copy('../configs/haarcascade_frontalface_default.xml', 'configs/haarcascade_frontalface_default.xml')
        else:
            # Если файла нет, создаем заглушку
            with open('configs/haarcascade_frontalface_default.xml', 'w') as f:
                f.write('dummy cascade content')
        
        # Сохраняем оригинальный путь к каскадам OpenCV
        self.original_haarcascades = cv2.data.haarcascades
            
    def tearDown(self):
        """Очистка временных файлов"""
        import shutil
        if os.path.exists('test_static'):
            shutil.rmtree('test_static')
        if os.path.exists('configs'):
            shutil.rmtree('configs')
        if os.path.exists('test.jpg'):
            os.remove('test.jpg')
        
        # Восстанавливаем оригинальный путь к каскадам OpenCV
        cv2.data.haarcascades = self.original_haarcascades
            
    @patch('src.check_env.get_versions')
    @patch('src.check_env.check_static_directory')
    @patch('src.check_env.test_face_detection')
    @patch('src.check_env.print_results')
    def test_static_dir_exists_with_files(self, mock_print_results, mock_test_face_detection, mock_check_static_directory, mock_get_versions):
        """Тест: директория static существует и содержит файлы"""
        # Настройка моков
        mock_get_versions.return_value = {
            'python': '3.8.10',
            'numpy': '1.21.0',
            'opencv': '4.5.0'
        }
        
        mock_check_static_directory.return_value = {
            'exists': True,
            'path': '../static',
            'files': ['input.jpg', 'test.jpg'],
            'message': 'Directory "../static" exists'
        }
        
        mock_test_face_detection.return_value = {
            'success': True,
            'message': 'Face cascade classifier loaded successfully'
        }
        
        mock_print_results.return_value = 0
        
        # Создаем модуль check_env заново для теста
        if 'src.check_env' in sys.modules:
            del sys.modules['src.check_env']
        
        # Импортируем модуль
        import src.check_env
        
        # Вызываем main функцию напрямую
        exit_code = src.check_env.main(run_tests=False)
        
        # Проверяем, что все функции были вызваны
        mock_get_versions.assert_called_once()
        mock_check_static_directory.assert_called_once()
        mock_test_face_detection.assert_called_once()
        mock_print_results.assert_called_once()
        
        # Проверяем, что функция вернула правильный код
        self.assertEqual(exit_code, 0)
        
        # Создаем временную директорию static
        os.makedirs('../static', exist_ok=True)
        with open('../static/input.jpg', 'w') as f:
            f.write('dummy image content')
        with open('../static/test.jpg', 'w') as f:
            f.write('dummy image content')
        
        try:
            # Создаем модуль check_env заново для теста
            if 'src.check_env' in sys.modules:
                del sys.modules['src.check_env']
            
            # Импортируем модуль
            import src.check_env
            
            # Вызываем main функцию напрямую
            exit_code = src.check_env.main()
            
            # Проверяем, что все функции были вызваны
            mock_get_versions.assert_called_once()
            mock_check_static_directory.assert_called_once()
            mock_test_face_detection.assert_called_once()
            mock_print_results.assert_called_once()
            
            # Проверяем, что функция вернула правильный код
            self.assertEqual(exit_code, 0)
            
        finally:
            # Очищаем временные файлы
            if os.path.exists('../static'):
                import shutil
                shutil.rmtree('../static')

    @patch('src.check_env.get_versions')
    @patch('src.check_env.check_static_directory')
    @patch('src.check_env.test_face_detection')
    @patch('src.check_env.print_results')
    def test_static_dir_does_not_exist(self, mock_print_results, mock_test_face_detection, mock_check_static_directory, mock_get_versions):
        """Тест: директория static не существует"""
        # Удаляем директорию static если она существует
        if os.path.exists('../static'):
            import shutil
            shutil.rmtree('../static')
            
        try:
            # Создаем модуль check_env заново для теста
            if 'src.check_env' in sys.modules:
                del sys.modules['src.check_env']
            
            # Импортируем модуль
            import src.check_env
            
            # Вызываем main функцию напрямую
            exit_code = src.check_env.main()
            
            # Проверяем, что все функции были вызваны
            mock_get_versions.assert_called_once()
            mock_check_static_directory.assert_called_once()
            mock_test_face_detection.assert_called_once()
            mock_print_results.assert_called_once()
            
            # Проверяем, что функция вернула правильный код
            self.assertEqual(exit_code, 1)
            
        finally:
            # Восстанавливаем директорию static если нужно
            if os.path.exists('../static'):
                import shutil
                shutil.rmtree('../static')

    @patch('src.check_env.get_versions')
    @patch('src.check_env.check_static_directory')
    @patch('src.check_env.test_face_detection')
    @patch('src.check_env.print_results')
    def test_face_cascade_loaded_successfully(self, mock_print_results, mock_test_face_detection, mock_check_static_directory, mock_get_versions):
        """Тест: каскад Хаара загружен успешно"""
        # Настройка моков
        mock_get_versions.return_value = {
            'python': '3.8.10',
            'numpy': '1.21.0',
            'opencv': '4.5.0'
        }
        
        mock_check_static_directory.return_value = {
            'exists': True,
            'path': '../static',
            'files': ['input.jpg'],
            'message': 'Directory "../static" exists'
        }
        
        mock_test_face_detection.return_value = {
            'success': True,
            'message': 'Face cascade classifier loaded successfully'
        }
        
        mock_print_results.return_value = 0
        
        # Создаем временную директорию static
        os.makedirs('../static', exist_ok=True)
        with open('../static/input.jpg', 'w') as f:
            f.write('dummy image content')
        
        try:
            # Создаем модуль check_env заново для теста
            if 'src.check_env' in sys.modules:
                del sys.modules['src.check_env']
            
            # Импортируем модуль
            import src.check_env
            
            # Вызываем main функцию напрямую
            exit_code = src.check_env.main()
            
            # Проверяем, что все функции были вызваны
            mock_get_versions.assert_called_once()
            mock_check_static_directory.assert_called_once()
            mock_test_face_detection.assert_called_once()
            mock_print_results.assert_called_once()
            
            # Проверяем, что функция вернула правильный код
            self.assertEqual(exit_code, 0)
            
        finally:
            # Очищаем временные файлы
            if os.path.exists('../static'):
                import shutil
                shutil.rmtree('../static')

    @patch('src.check_env.get_versions')
    @patch('src.check_env.check_static_directory')
    @patch('src.check_env.test_face_detection')
    @patch('src.check_env.print_results')
    def test_face_cascade_failed_to_load(self, mock_print_results, mock_test_face_detection, mock_check_static_directory, mock_get_versions):
        """Тест: ошибка загрузки каскада Хаара"""
        # Настройка моков
        mock_get_versions.return_value = {
            'python': '3.8.10',
            'numpy': '1.21.0',
            'opencv': '4.5.0'
        }
        
        mock_check_static_directory.return_value = {
            'exists': True,
            'path': '../static',
            'files': ['input.jpg'],
            'message': 'Directory "../static" exists'
        }
        
        mock_test_face_detection.return_value = {
            'success': False,
            'message': 'Failed to load face cascade classifier'
        }
        
        mock_print_results.return_value = 1
        
        # Создаем временную директорию static
        os.makedirs('../static', exist_ok=True)
        with open('../static/input.jpg', 'w') as f:
            f.write('dummy image content')
        
        try:
            # Создаем модуль check_env заново для теста
            if 'src.check_env' in sys.modules:
                del sys.modules['src.check_env']
            
            # Импортируем модуль
            import src.check_env
            
            # Вызываем main функцию напрямую
            exit_code = src.check_env.main()
            
            # Проверяем, что все функции были вызваны
            mock_get_versions.assert_called_once()
            mock_check_static_directory.assert_called_once()
            mock_test_face_detection.assert_called_once()
            mock_print_results.assert_called_once()
            
            # Проверяем, что функция вернула правильный код
            self.assertEqual(exit_code, 1)
            
        finally:
            # Очищаем временные файлы
            if os.path.exists('../static'):
                import shutil
                shutil.rmtree('../static')

if __name__ == '__main__':
    unittest.main()
