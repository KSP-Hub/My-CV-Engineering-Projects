"""
CV-010: Ядро детекции лиц OpenCV
Автор: Stetson Perceptron
Дата: 2025-12-25
Версия: 1.0

Описание:
Общее ядро для детекции лиц, используемое как в консольной, так и в веб-версии.
"""

import cv2
import numpy as np
import os
import logging

# Настройка логгирования
logger = logging.getLogger(__name__)


class FaceDetectionConfig:
    """Конфигурация для детекции лиц"""
    def __init__(self):
        self.scale_factor = 1.1
        self.min_neighbors = 5
        self.min_size = (30, 30)
        self.max_image_width = 800


class FaceDetector:
    """Класс для детекции лиц с использованием Haar cascades"""
    def __init__(self, config=None):
        """Инициализация детектора лиц
        
        Args:
            config (FaceDetectionConfig): Конфигурация детектора
        """
        self.config = config or FaceDetectionConfig()
        
        # Путь к предобученному каскаду Хаара
        self.cascade_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'haarcascade_frontalface_default.xml')
        
        # Проверка существования файла каскада
        if not os.path.exists(self.cascade_path):
            # Попробуем найти в нескольких возможных местах
            possible_paths = [
                self.cascade_path,
                os.path.join(os.path.dirname(__file__), '..', 'haarcascade_frontalface_default.xml'),
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            ]
            
            cascade_found = False
            for path in possible_paths:
                if os.path.exists(path):
                    self.cascade_path = path
                    cascade_found = True
                    break
            
            if not cascade_found:
                raise FileNotFoundError(f"Файл каскада не найден по путям: {possible_paths}")
        
        # Загрузка классификатора
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        
        if self.face_cascade.empty():
            raise ValueError("Не удалось загрузить каскад Хаара")
    
    def detect_faces(self, image_path, output_path=None, resize_for_web=False):
        """Детекция лиц на изображении
        
        Args:
            image_path (str): Путь к входному изображению
            output_path (str, optional): Путь для сохранения результата
            resize_for_web (bool): Уменьшить изображение для веб-интерфейса
        
        Returns:
            dict: Результат детекции с количеством лиц и закодированным изображением
        """
        # Проверка существования файла изображения
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл изображения не найден: {image_path}")
        
        # Загрузка изображения
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Не удалось загрузить изображение")
        
        # Уменьшаем размер изображения для ускорения обработки, если нужно
        if resize_for_web:
            height, width = img.shape[:2]
            if width > self.config.max_image_width:
                new_width = self.config.max_image_width
                new_height = int(height * (self.config.max_image_width / width))
                img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

        # Преобразование в оттенки серого
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Детекция лиц
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=self.config.scale_factor,
            minNeighbors=self.config.min_neighbors,
            minSize=self.config.min_size,
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        logger.info(f"✅ Найдено {len(faces)} лиц")
        
        # Рисование bounding boxes
        for idx, (x, y, w, h) in enumerate(faces, start=1):
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, f'Face #{idx}', (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        result = {
            'count': len(faces),
            'faces': [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in faces]
        }
        
        # Сохранение результата, если указан путь
        if output_path:
            # Убедимся, что папка существует
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            cv2.imwrite(output_path, img)
            logger.info(f"💾 Результат сохранен в: {output_path}")
            
            # Добавляем путь к сохраненному файлу в результат
            result['output_path'] = output_path
        
        # Кодируем изображение для веб-интерфейса
        _, buffer = cv2.imencode('.jpg', img)
        img_str = base64.b64encode(buffer).decode()
        result['image'] = img_str
        
        return result
    
    def display_result(self, image_path):
        """Отображение результата с возможностью сохранения"""
        img = cv2.imread(image_path)
        cv2.imshow('Face Detection Result', img)
        logger.info("Нажмите любую клавишу для закрытия окна...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()