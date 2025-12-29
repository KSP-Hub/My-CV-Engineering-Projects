from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import logging
import base64
import cv2
import numpy as np

# Настройка пути для импорта
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Импорт детектора QR-кодов
from qr_detector import QRDetector

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Инициализация детектора QR-кодов
detector = QRDetector()

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    logger.info("Запрос на загрузку получен")
    
    if 'file' not in request.files:
        logger.error("Файл не найден в запросе")
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        logger.error("Имя файла пустое")
        return jsonify({'error': 'No file selected'}), 400
    
    # Генерация уникального имени файла
    import uuid
    file_ext = file.filename.split('.')[-1]
    filename = f"upload_{uuid.uuid4().hex}.{file_ext}"
    filepath = os.path.join('static', filename)
    
    # Убедимся, что папка static существует
    os.makedirs('static', exist_ok=True)
    
    logger.info(f"Сохранение файла: {filepath}")
    try:
        file.save(filepath)
        logger.info("Файл успешно сохранён")
    except Exception as e:
        logger.error(f"Ошибка сохранения файла: {str(e)}")
        return jsonify({'error': 'File save failed'}), 500
    
    # Обработка изображения
    logger.info(f"Обработка изображения: {filepath}")

    # Используем сохраненный файл для чтения изображения
    try:
        image = cv2.imread(filepath)
        
        if image is None:
            logger.error("Не удалось прочитать изображение")
            # Удаляем поврежденный файл
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': 'Failed to read image'}), 500
        
        # Обнаружение и декодирование QR-кода
        success, data, bbox = detector.detect_and_decode(image)
        
        if not success:
            logger.warning("QR-код не найден на изображении")
            return jsonify({'error': 'No QR code detected'}), 400
        
        # Отрисовка рамки вокруг QR-кода
        if bbox is not None:
            image = detector.draw_detection(image, bbox)
        
        # Сохранение результата
        result_path = os.path.join('static', f'result_{filename}')
        cv2.imwrite(result_path, image)
        
        # Конвертация в base64 для отправки в браузер
        _, buffer = cv2.imencode('.jpg', image)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        
        logger.info(f"QR-код распознан: {data}")
        return jsonify({
            'data': data,
            'image': image_base64
        })
        
    except Exception as e:
        logger.error(f"Ошибка обработки изображения: {str(e)}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'QR code detection failed'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)