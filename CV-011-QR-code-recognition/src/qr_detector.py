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
            data, bbox, _ = self.detector.detectAndDecode(frame)
            
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