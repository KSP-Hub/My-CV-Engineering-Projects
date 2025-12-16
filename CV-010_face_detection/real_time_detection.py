"""
CV-010: Real-time Face Detection
Автор: Stetson Perceptron
Дата: 2025-12-09

Реализация детекции лиц в реальном времени с веб-камеры.
"""


import cv2
import os

class RealTimeFaceDetector:
    def __init__(self):
        """Инициализация детектора лиц"""
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        
        if not os.path.exists(cascade_path):
            raise FileNotFoundError(f"Файл каскада не найден: {cascade_path}")
        
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        if self.face_cascade.empty():
            raise ValueError("Не удалось загрузить каскад Хаара")
    
    def start_camera_detection(self):
        """Запуск детекции с веб-камеры"""
        # Инициализация камеры
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Ошибка: Не удалось подключиться к камере")
            return
        
        print("🎥 Детекция лиц в реальном времени запущена. Нажмите 'q' для выхода.")
        
        while True:
            # Захват кадра
            ret, frame = cap.read()
            
            if not ret:
                print("❌ Ошибка: Не удалось захватить кадр")
                break
            
            # Преобразование в оттенки серого
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Детекция лиц
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            
            # Рисование bounding boxes
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, f'Face', (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
            # Отображение количества лиц
            cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Показ кадра
            cv2.imshow('Real-time Face Detection', frame)
            
            # Выход по нажатию 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Освобождение ресурсов
        cap.release()
        cv2.destroyAllWindows()
        print("⏹️ Детекция остановлена.")

if __name__ == "__main__":
    try:
        detector = RealTimeFaceDetector()
        detector.start_camera_detection()
    except Exception as e:
        print(f"❌ Ошибка: {str(e)}")
