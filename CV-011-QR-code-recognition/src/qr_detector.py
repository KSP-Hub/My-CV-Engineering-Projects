import cv2

class QRDetector:
    """
    Класс для детекции и декодирования QR-кодов с использованием OpenCV.
    """
    
    def __init__(self):
        """
        Инициализация детектора QR-кодов.
        """
        self.detector = cv2.QRCodeDetector()
    
    def detect_and_decode(self, frame):
        """
        Обнаруживает и декодирует QR-код на изображении.
        
        Args:
            frame: Кадр из видеопотока (numpy array)
            
        Returns:
            tuple: (успех, данные, точки границы) или (False, None, None)
        """
        try:
            # Проверка, что изображение не пустое
            if frame is None or frame.size == 0:
                print("Ошибка: Пустое изображение")
                return False, None, None
            
            # Попробуем декодировать как есть
            data, bbox, _ = self.detector.detectAndDecode(frame)
            
            if bbox is not None and data:
                return True, data, bbox
            
            # Если не получилось, попробуем в градациях серого
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            data, bbox, _ = self.detector.detectAndDecode(gray)
            
            if bbox is not None and data:
                return True, data, bbox
            
            # Если все еще не получается, попробуем с бинаризацией
            _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            data, bbox, _ = self.detector.detectAndDecode(binary)
            
            if bbox is not None and data:
                return True, data, bbox
            
            # Попробуем с инвертированным изображением
            inverted = cv2.bitwise_not(binary)
            data, bbox, _ = self.detector.detectAndDecode(inverted)
            
            if bbox is not None and data:
                return True, data, bbox
            
            # Попробуем с размытием для уменьшения шума
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            _, binary_blurred = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
            data, bbox, _ = self.detector.detectAndDecode(binary_blurred)
            
            if bbox is not None and data:
                return True, data, bbox
            
            return False, None, None
            
        except Exception as e:
            print(f"Ошибка при детекции QR-кода: {e}")
            return False, None, None
    
    def draw_detection(self, frame, bbox, color=(0, 255, 0)):
        """
        Рисует рамку вокруг обнаруженного QR-кода.
        
        Args:
            frame: Кадр для отрисовки
            bbox: Координаты границы QR-кода
            color: Цвет рамки в формате BGR
            
        Returns:
            Обработанный кадр
        """
        try:
            # Преобразуем координаты в целые числа
            bbox = bbox.astype(int)
            
            # Рисуем рамку
            n_lines = len(bbox)
            for i in range(n_lines):
                point1 = tuple(bbox[i][0])
                point2 = tuple(bbox[(i + 1) % n_lines][0])
                cv2.line(frame, point1, point2, color, 2)
                
            return frame
            
        except Exception as e:
            print(f"Ошибка при отрисовке рамки: {e}")
            return frame