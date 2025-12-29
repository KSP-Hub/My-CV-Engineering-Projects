import pytest
import os
import sys
from unittest.mock import patch, MagicMock


class TestQRWebApp:
    """
    Unit-тесты для веб-приложения распознавания QR-кодов.
    """
    
    def setup_method(self):
        """
        Настройка тестового клиента.
        """
        # Импортируем приложение
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        from qr_web_app import app
        self.app = app
    
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
            
            with self.app.test_client() as client:
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
            
            with self.app.test_client() as client:
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
