import cv2
import sys
from qr_detector import QRDetector

class SimpleQRApp:
    """
    Простое приложение для распознавания QR-кодов с веб-камеры.
    """
    
    def __init__(self):
        """
        Инициализация приложения.
        """
        self.detector = QRDetector()
        self.cap = None
        
    def start(self):
        """
        Запуск приложения.
        """
        try:
            # Инициализация камеры
            self.cap = cv2.VideoCapture(0)
            
            if not self.cap.isOpened():
                print("Ошибка: Не удается открыть камеру")
                return
            
            print("QR-детектор запущен. Наведите камеру на QR-код.")
            print("Нажмите ESC для выхода.")
            
            while True:
                # Захват кадра
                ret, frame = self.cap.read()
                
                if not ret:
                    print("Ошибка: Не удается получить кадр")
                    break
                
                # Обнаружение и декодирование QR-кода
                success, data, bbox = self.detector.detect_and_decode(frame)
                
                if success:
                    # Отрисовка рамки вокруг QR-кода
                    frame = self.detector.draw_detection(frame, bbox)
                    
                    # Отображение данных
                    cv2.putText(frame, f"Data: {data}", (10, 30), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    
                    print(f"QR-код распознан: {data}")
                
                # Отображение кадра
                cv2.imshow('QR Code Detector', frame)
                
                # Проверка нажатия клавиши
                key = cv2.waitKey(1) & 0xFF
                if key == 27:  # ESC
                    break
                    
        except Exception as e:
            print(f"Ошибка при работе приложения: {e}")
            
        finally:
            self.cleanup()
    
    def cleanup(self):
        """
        Очистка ресурсов.
        """
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()

# Точка входа
if __name__ == "__main__":
    app = SimpleQRApp()
    try:
        app.start()
    except KeyboardInterrupt:
        print("\nПриложение остановлено пользователем")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
    finally:
        app.cleanup()