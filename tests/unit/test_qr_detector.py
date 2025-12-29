import unittest
import cv2
import numpy as np
from unittest.mock import Mock, patch
from src.qr_detector import QRDetector


class TestQRDetector(unittest.TestCase):
    """
    Unit-тесты для класса QRDetector с полным мокированием.
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
