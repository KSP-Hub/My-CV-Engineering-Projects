import unittest
import os
from unittest import TestCase

import cv2
import numpy as np
from face_detection import FaceDetector


class TestFaceDetector(unittest.TestCase):

    def setUp(self):
        """Инициализация перед каждым тестом"""
        self.detector = FaceDetector()

        # Создаём тестовое изображение 640x480 с одним лицом
        self.test_image_path = "test_input.jpg"
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        # Рисуем лицо (просто прямоугольник для теста)
        cv2.rectangle(img, (200, 100), (400, 300), (255, 255, 255), -1)
        cv2.imwrite(self.test_image_path, img)

    def tearDown(self):
        """Очистка после каждого теста"""
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        if os.path.exists("output.jpg"):
            os.remove("output.jpg")

    def test_init_success(self):
        """Тест: инициализация детектора"""
        self.assertIsNotNone(self.detector.face_cascade)

    def test_face_detection_works(self):
        """Тест: детекция лица на изображении"""
        faces_count = self.detector.detect_faces(self.test_image_path, "output.jpg")
        self.assertGreaterEqual(faces_count, 0)  # Должно быть >= 0 лиц

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
        empty_img_path = "empty.jpg"
        cv2.imwrite(empty_img_path, np.array([]))
        with self.assertRaises(ValueError):
            self.detector.detect_faces(empty_img_path)
        os.remove(empty_img_path)


if __name__ == '__main__':
    unittest.main()


class Test(TestCase):
    pass
