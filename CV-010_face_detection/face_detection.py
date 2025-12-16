"""
CV-010: Детекция лиц OpenCV
Автор: Stetson Perceptron
Дата: 2025-11-28
Версия: 2.0

Описание:
Реализация детектора лиц с использованием Haar cascades.
Скрипт загружает изображение, детектирует лица и сохраняет результат с bounding boxes.

Требования:
- OpenCV
- NumPy

Использование:
python face_detection.py
"""

import cv2
import numpy as np
import os
import logging

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("face_detection.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class FaceDetector:
    def __init__(self):
        """Инициализация детектора лиц"""
        # Путь к предобученному каскаду Хаара
        self.cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        
        # Проверка существования файла каскада
        if not os.path.exists(self.cascade_path):
            raise FileNotFoundError(f"Файл каскада не найден: {self.cascade_path}")
        
        # Загрузка классификатора
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        
        if self.face_cascade.empty():
            raise ValueError("Не удалось загрузить каскад Хаара")
    
    def detect_faces(self, image_path, output_path="output.jpg"):
        """
        Детекция лиц на изображении
        
        Args:
            image_path (str): Путь к входному изображению
            output_path (str): Путь для сохранения результата
        
        Returns:
            int: Количество детектированных лиц
        """
        # Проверка существования файла изображения
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл изображения не найден: {image_path}")
        
        # Загрузка изображения
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Не удалось загрузить изображение")
        
        # Преобразование в оттенки серого
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Детекция лиц
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        logger.info(f"✅ Найдено {len(faces)} лиц")
        
        # Рисование bounding boxes
        for idx, (x, y, w, h) in enumerate(faces, start=1):
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, f'Face #{idx}', (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # Сохранение результата
        cv2.imwrite(output_path, img)
        logger.info(f"💾 Результат сохранен в: {output_path}")
        
        return len(faces)
    
    def display_result(self, image_path):
        """Отображение результата с возможностью сохранения"""
        img = cv2.imread(image_path)
        cv2.imshow('Face Detection Result', img)
        logger.info("Нажмите любую клавишу для закрытия окна...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    """Основная функция"""
    try:
        # Инициализация детектора
        detector = FaceDetector()
        
        # Пути к файлам
        input_image = "input.jpg"
        if not os.path.exists(input_image):
            # Пробуем найти input.jpg в папке static
            input_image = "static/input.jpg"
            
        output_image = "output.jpg"
        
        # Детекция лиц
        faces_count = detector.detect_faces(input_image, output_image)
        
        # Отображение результата
        detector.display_result(output_image)
        
        logger.info(f"🎉 Проект CV-010 успешно завершен! Найдено: {faces_count} лиц")
        
    except Exception as e:
        logger.error(f"❌ Ошибка: {str(e)}")
        logger.info("💡 Рекомендации по исправлению:")
        logger.info("- Проверьте, что файл 'input.jpg' существует в папке проекта")
        logger.info("- Убедитесь, что окружение 'cv_env' активировано")
        logger.info("- Проверьте установку OpenCV: conda list opencv")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)