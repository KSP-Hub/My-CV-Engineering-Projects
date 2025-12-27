from flask import Flask, render_template, request, jsonify
import os
import logging

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Импорт ядра детекции лиц
from face_detection_core import FaceDetector

# Добавляем импорт версии
try:
    with open('../.version/VERSION', 'r') as f:
        VERSION = f.read().strip()
except FileNotFoundError:
    VERSION = '1.0.0'

def detect_faces_in_image(image_path):
    """Детекция лиц с использованием ядра face_detection_core"""
    try:
        # Инициализация детектора с конфигурацией
        detector = FaceDetector()
        
        # Параметры для веб-интерфейса
        max_width = 800
        output_path = "static/output.jpg"
        
        # Обработка изображения
        result = detector.detect_faces(
            image_path=image_path,
            output_path=output_path,
            resize_for_web=True
        )
        
        return result
        
    except Exception as e:
        print(f"[ERROR] Ошибка при детекции лиц: {str(e)}")
        raise

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', version=VERSION)

@app.route('/upload', methods=['POST'])
def upload():
    print("[DEBUG] Запрос получен")  # Отладка
    if 'file' not in request.files:
        print("[DEBUG] Файл не найден в запросе")
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        print("[DEBUG] Имя файла пустое")
        return jsonify({'error': 'No file selected'}), 400
    
    # Генерация уникального имени файла
    import uuid
    file_ext = file.filename.split('.')[-1]
    filename = f"upload_{uuid.uuid4().hex}.{file_ext}"
    filepath = os.path.join('../static', filename)
    
    # Убедимся, что папка static существует
    os.makedirs('../static', exist_ok=True)
    
    print(f"[DEBUG] Сохранение файла: {filepath}")
    try:
        file.save(filepath)
        print("[DEBUG] Файл успешно сохранён")
    except Exception as e:
        print(f"[DEBUG] Ошибка сохранения файла: {str(e)}")
        return jsonify({'error': 'File save failed'}), 500
    
    # Обработка изображения
    print(f"[DEBUG] Обработка изображения: {filepath}")
    
    try:
        # Добавляем логирование начала обработки
        print(f"[DEBUG] Начало детекции лиц...")
        
        result = detect_faces_in_image(filepath)
        
        # Добавляем логирование результата
        print(f"[DEBUG] Детекция завершена: {result['count']} лиц")
        print(f"[DEBUG] Изображение обработано и закодировано")
        
        return jsonify(result)
    except Exception as e:
        print(f"[DEBUG] Ошибка обработки изображения: {str(e)}")
        import traceback
        print(f"[DEBUG] Traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Face detection failed'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)