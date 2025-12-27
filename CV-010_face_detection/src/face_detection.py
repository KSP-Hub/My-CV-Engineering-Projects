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

import os
import logging
import cv2

# Импорт ядра детекции лиц
from .face_detection_core import FaceDetector

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("../face_detection.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# class FaceDetector определен в face_detection_core
# Все методы детекции перенесены в ядро
# Этот класс не нужен здесь, так как мы используем импорт из face_detection_core


    


def main():
    """Основная функция"""
    try:
        # Инициализация детектора из ядра
        detector = FaceDetector()
        
        # Пути к файлам
        input_image = "input.jpg"
        if not os.path.exists(input_image):
            # Пробуем найти input.jpg в папке static
            input_image = "static/input.jpg"
            
        output_image = "output.jpg"
        
        # Детекция лиц с использованием ядра
        result = detector.detect_faces(input_image, output_image)
        faces_count = result
        
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