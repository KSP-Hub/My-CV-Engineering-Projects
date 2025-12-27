import unittest
import os
import sys
from unittest.mock import patch, MagicMock
import json

# Добавляем путь к src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

# Импортируем модуль после добавления пути
import importlib.util

# Динамический импорт модуля с дефисом в имени
spec = importlib.util.spec_from_file_location("CV-010-app", "D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/src/CV-010-app.py")
CV_010_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CV_010_app)

class TestCV010App(unittest.TestCase):
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        # Создаем временный файл версии
        os.makedirs('.version', exist_ok=True)
        with open('.version/VERSION', 'w') as f:
            f.write('2.0.0')
        
        # Создаем временную папку static
        os.makedirs('static', exist_ok=True)
        with open('static/input.jpg', 'w') as f:
            f.write('dummy image content')
        
        # Создаем приложение
        CV_010_app.app.config['TESTING'] = True
        self.client = CV_010_app.app.test_client()
    
    def tearDown(self):
        """Очистка после каждого теста"""
        import shutil
        if os.path.exists('.version'):
            shutil.rmtree('.version')
        if os.path.exists('static'):
            shutil.rmtree('static')
        
    @patch('CV_010_app.detect_faces_in_image')
    def test_upload_success(self, mock_detect_faces):
        """Тест: успешная загрузка и обработка изображения"""
        # Настройка мока
        mock_detect_faces.return_value = {
            'count': 2,
            'image': 'base64_encoded_image'
        }
        
        # Создаем тестовое изображение
        with open('static/input.jpg', 'rb') as f:
            data = {'file': (f, 'input.jpg')}
            
            # Отправляем запрос
            response = self.client.post('/upload', data=data, 
                                   content_type='multipart/form-data')
            
        # Проверяем ответ
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result['count'], 2)
        self.assertEqual(result['image'], 'base64_encoded_image')
        
        # Проверяем, что функция детекции была вызвана
        mock_detect_faces.assert_called()
    
    def test_upload_no_file(self):
        """Тест: отсутствие файла в запросе"""
        response = self.client.post('/upload', data={}, 
                               content_type='multipart/form-data')
        
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn('error', result)
        self.assertIn('No file uploaded', result['error'])
    
    def test_upload_no_filename(self):
        """Тест: отсутствие имени файла"""
        data = {'file': (None, '')}
        response = self.client.post('/upload', data=data, 
                               content_type='multipart/form-data')
        
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn('error', result)
        self.assertIn('No file selected', result['error'])
    
    @patch('CV_010_app.detect_faces_in_image')
    def test_upload_save_failure(self, mock_detect_faces):
        """Тест: ошибка сохранения файла"""
        # Моделируем ошибку сохранения файла
        with patch('CV_010_app.request.files') as mock_files:
            mock_file = MagicMock()
            mock_file.filename = 'test.jpg'
            mock_file.save.side_effect = Exception('Save failed')
            mock_files.__getitem__.return_value = mock_file
            
            data = {'file': (None, 'test.jpg')}
            response = self.client.post('/upload', data=data, 
                                   content_type='multipart/form-data')
            
        self.assertEqual(response.status_code, 500)
        result = json.loads(response.data)
        self.assertIn('error', result)
        self.assertIn('File save failed', result['error'])
    
    @patch('CV_010_app.detect_faces_in_image')
    def test_upload_detection_failure(self, mock_detect_faces):
        """Тест: ошибка детекции изображения"""
        # Моделируем ошибку детекции
        mock_detect_faces.side_effect = Exception('Detection failed')
        
        with open('static/input.jpg', 'rb') as f:
            data = {'file': (f, 'input.jpg')}
            response = self.client.post('/upload', data=data, 
                                   content_type='multipart/form-data')
            
        self.assertEqual(response.status_code, 500)
        result = json.loads(response.data)
        self.assertIn('error', result)
        self.assertIn('Face detection failed', result['error'])
    
    def test_index_page(self):
        """Тест: главная страница"""
        response = self.client.get('/')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Face Detection', response.data)
        self.assertIn(b'2.0.0', response.data)  # Проверяем версию

if __name__ == '__main__':
    unittest.main()