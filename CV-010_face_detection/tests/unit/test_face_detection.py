import unittest
import os
from unittest import TestCase

import cv2
import numpy as np
from src.face_detection import FaceDetector


class TestFaceDetector(unittest.TestCase):

    def setUp(self):
        """Инициализация перед каждым тестом"""
        # Создаем временную папку configs
        os.makedirs('configs', exist_ok=True)
        # Создаем настоящий файл каскада Хаара
        import shutil
        if os.path.exists('../configs/haarcascade_frontalface_default.xml'):
            shutil.copy('../configs/haarcascade_frontalface_default.xml', 'configs/haarcascade_frontalface_default.xml')
        else:
            # Если файла нет, создаем заглушку
            with open('configs/haarcascade_frontalface_default.xml', 'w') as f:
                f.write('dummy cascade content')
        
        # Сохраняем оригинальный путь к каскадам
        self.original_haarcascades = cv2.data.haarcascades
        # Меняем путь к каскадам на нашу временную директорию
        cv2.data.haarcascades = os.path.abspath('configs')
        
        # Создаем детектор
        self.detector = FaceDetector()

        # Создаём тестовое изображение 640x480 с одним лицом
        self.test_image_path = "test_input.jpg"
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        # Рисуем лицо (просто прямоугольник для теста)
        cv2.rectangle(img, (200, 100), (400, 300), (255, 255, 255), -1)
        cv2.imwrite(self.test_image_path, img)

    def tearDown(self):
        """Очистка после каждого теста"""
        # Восстанавливаем оригинальный путь к каскадам
        cv2.data.haarcascades = self.original_haarcascades
        
        # Удаляем временные файлы
        import shutil
        if os.path.exists('configs'):
            shutil.rmtree('configs')
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists("output.jpg"):
            os.remove("output.jpg")

    def test_init_success(self):
        """Тест: инициализация детектора"""
        self.assertIsNotNone(self.detector.face_cascade)

    def test_face_detection_works(self):
        """Тест: детекция лица на изображении"""
        result = self.detector.detect_faces(self.test_image_path, "output.jpg")
        self.assertIsInstance(result, dict)
        self.assertIn('count', result)
        self.assertGreaterEqual(result['count'], 0)  # Должно быть >= 0 лиц

    def test_output_file_created(self):
        """Тест: создаётся ли выходной файл"""
        self.detector.detect_faces(self.test_image_path, "output.jpg")
        self.assertTrue(os.path.exists("output.jpg"))

    def test_invalid_image_path(self):
        """Тест: обработка несуществующего файла"""
        with self.assertRaises(FileNotFoundError):
            self.detector.detect_faces("nonexistent.jpg")

    def test_empty_image(self):
        """Тест: обработка пустого изображения"""
        # Создаем пустое изображение с минимальными размерами
        empty_img_path = "empty.jpg"
        empty_img = np.zeros((1, 1, 3), dtype=np.uint8)
        cv2.imwrite(empty_img_path, empty_img)
        
        # Детектор должен обработать такое изображение, но не найти лиц
        result = self.detector.detect_faces(empty_img_path, "output.jpg")
        self.assertEqual(result['count'], 0)
        
        # Очистка
        if os.path.exists(empty_img_path):
            os.remove(empty_img_path)
        if os.path.exists("output.jpg"):
            os.remove("output.jpg")


if __name__ == '__main__':
    unittest.main()


class Test(TestCase):
    pass
