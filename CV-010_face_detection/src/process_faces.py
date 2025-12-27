"""
Script for processing images with face detection and generating results
"""

import os
import sys
import cv2
import numpy as np
from face_detection_core import FaceDetector

# Путь к входному изображению
input_image_path = "D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/assets/input.jpg"

# Проверка существования входного файла
if not os.path.exists(input_image_path):
    print(f"Файл изображения не найден: {input_image_path}")
    sys.exit(1)

# Создание экземпляра детектора
config = None  # Используем конфигурацию по умолчанию
detector = FaceDetector(config)

# Обработка изображения без добавления подписи о проценте распознанных лиц
result = detector.detect_faces(
    image_path=input_image_path,
    output_path="results/output_python.jpg",
    resize_for_web=True
)

print(f"✅ Найдено лиц: {result['count']}")
print(f"💾 Результат сохранен в: results/output_python.jpg")
