import pytest
import requests
import os
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from unittest.mock import patch, MagicMock

# Тесты для веб-интерфейса QR-кода

class TestQRWebApp:
    """
    Тесты для веб-приложения распознавания QR-кодов.
    """
    
    def setup_method(self):
        """
        Настройка тестового клиента.
        """
        self.base_url = 'http://localhost:5000'
    
    @pytest.mark.skip(reason="Requires server to be running")
    def test_home_page(self):
        """
        Тест доступности главной страницы.
        """
        response = requests.get(self.base_url)
        assert response.status_code == 200
        assert '<title>Распознавание QR-кодов — CV-011</title>' in response.text
    
    @pytest.mark.skip(reason="Requires server to be running")
    def test_upload_no_file(self):
        """
        Тест загрузки без файла.
        """
        response = requests.post(f'{self.base_url}/upload')
        assert response.status_code == 400
        assert 'No file uploaded' in response.json()['error']
    
    @pytest.mark.skip(reason="Requires server to be running")
    def test_upload_empty_file(self):
        """
        Тест загрузки пустого файла.
        """
        files = {'file': ('', b'')}
        response = requests.post(f'{self.base_url}/upload', files=files)
        assert response.status_code == 400
        assert 'No file selected' in response.json()['error']
    
    @pytest.mark.skip(reason="Requires server to be running")
    def test_upload_invalid_file(self):
        """
        Тест загрузки невалидного файла.
        """
        files = {'file': ('test.txt', b'invalid content')}
        response = requests.post(f'{self.base_url}/upload', files=files)
        assert response.status_code == 500
        assert 'Failed to read image' in response.json()['error']
    
    def test_mocked_qr_detection_success(self):
        """
        Тест успешного распознавания QR-кода (с моками).
        """
        with patch('src.qr_detector.QRDetector') as mock_detector_class:
            # Настройка моков
            mock_detector = MagicMock()
            mock_detector_class.return_value = mock_detector
            
            # Мок успешного обнаружения
            mock_detector.detect_and_decode.return_value = (True, 'Test Data', [[[10,10],[100,10],[100,100],[10,100]]])
            mock_detector.draw_detection.return_value = b'processed_image_data'
            
            # Имитация работы приложения
            import sys
            import os
            sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
            from qr_web_app import app
            with app.test_client() as client:
                # Создаем временный файл для теста
                with open('test_qr.png', 'wb') as f:
                    f.write(b'dummy_image_data')
                
                with open('test_qr.png', 'rb') as f:
                    response = client.post('/upload', 
                                         data={'file': f},
                                         content_type='multipart/form-data')
                
                # Очистка
                if os.path.exists('test_qr.png'):
                    os.remove('test_qr.png')
                
                assert response.status_code == 200
                json_data = response.get_json()
                assert 'data' in json_data
                assert json_data['data'] == 'Test Data'
                assert 'image' in json_data
    
    def test_mocked_qr_detection_failure(self):
        """
        Тест неудачного распознавания QR-кода (с моками).
        """
        with patch('src.qr_detector.QRDetector') as mock_detector_class:
            # Настройка моков
            mock_detector = MagicMock()
            mock_detector_class.return_value = mock_detector
            
            # Мок неудачного обнаружения
            mock_detector.detect_and_decode.return_value = (False, None, None)
            
            # Имитация работы приложения
            import sys
            import os
            sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
            from qr_web_app import app
            with app.test_client() as client:
                # Создаем временный файл для теста
                with open('test_no_qr.png', 'wb') as f:
                    f.write(b'dummy_image_data')
                
                with open('test_no_qr.png', 'rb') as f:
                    response = client.post('/upload', 
                                         data={'file': f},
                                         content_type='multipart/form-data')
                
                # Очистка
                if os.path.exists('test_no_qr.png'):
                    os.remove('test_no_qr.png')
                
                assert response.status_code == 400
                json_data = response.get_json()
                assert 'error' in json_data
                assert 'No QR code detected' in json_data['error']