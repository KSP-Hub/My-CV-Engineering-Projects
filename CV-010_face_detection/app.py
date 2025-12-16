from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
import os

def detect_faces_in_image(image_path):
    """Функция детекции лиц, переиспользует логику из face_detection.py"""
    # Используем абсолютный путь к каскаду
    cascade_path = 'D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    if face_cascade.empty():
        raise Exception(f'Не удалось загрузить каскад Хаара: {cascade_path}')
    
    img = cv2.imread(image_path)
    
    # Уменьшаем размер изображения для ускорения обработки
    max_width = 800
    height, width = img.shape[:2]
    if width > max_width:
        new_width = max_width
        new_height = int(height * (max_width / width))
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Рисуем рамки
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Убедимся, что папка static существует
    os.makedirs('static', exist_ok=True)
    
    # Сохраняем результат
    result_path = "static/output.jpg"
    cv2.imwrite(result_path, img)
    
    # Кодируем изображение для отправки в HTML
    _, buffer = cv2.imencode('.jpg', img)
    img_str = base64.b64encode(buffer).decode()
    
    return {
        'count': len(faces),
        'image': img_str
    }

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

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
    filepath = os.path.join('static', filename)
    
    # Убедимся, что папка static существует
    os.makedirs('static', exist_ok=True)
    
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