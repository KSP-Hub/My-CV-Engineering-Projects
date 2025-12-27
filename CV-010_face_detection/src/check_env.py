import sys
import numpy
import cv2
import os
from contextlib import contextmanager

def get_versions():
    """Возвращает версии Python, NumPy и OpenCV"""
    return {
        'python': sys.version,
        'numpy': numpy.__version__,
        'opencv': cv2.__version__
    }

def check_static_directory(base_path=None):
    """Проверяет наличие директории static и её содержимое"""
    if base_path is None:
        base_path = os.path.dirname(__file__)
    
    static_dir = os.path.join(base_path, '..', 'static')
    
    if os.path.exists(static_dir) and os.path.isdir(static_dir):
        files = os.listdir(static_dir)
        return {
            'exists': True,
            'path': static_dir,
            'files': files,
            'message': f'Directory "{static_dir}" exists'
        }
    else:
        return {
            'exists': False,
            'path': static_dir,
            'files': [],
            'message': f'Directory "{static_dir}" does not exist!'
        }

def test_face_detection(base_path=None):
    """Тестирует детекцию лиц с использованием каскада Хаара"""
    if base_path is None:
        base_path = os.path.dirname(__file__)
    
    try:
        # Используем встроенный каскад Хаара из OpenCV
        cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
        if not os.path.exists(cascade_path):
            return {
                'success': False,
                'message': f'Cascade classifier file not found at {cascade_path}'
            }
        
        face_cascade = cv2.CascadeClassifier(cascade_path)
        if face_cascade.empty():
            return {
                'success': False,
                'message': 'Failed to load face cascade classifier'
            }
        
        # Test with a sample image if exists
        test_image = os.path.join(base_path, '..', '..', 'tests', 'unit', 'test_images', 'test.jpg')
        if os.path.exists(test_image):
            img = cv2.imread(test_image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            return {
                'success': True,
                'message': f'Face cascade classifier loaded successfully. Found {len(faces)} faces in test image'
            }
        else:
            return {
                'success': True,
                'message': 'Face cascade classifier loaded successfully. No test.jpg image found - skipping detection test'
            }
            
    except Exception as e:
        import traceback
        return {
            'success': False,
            'message': f'Face detection test failed: {str(e)}\n{traceback.format_exc()}'
        }

def run_all_tests(base_path=None):
    """Запускает все тесты и возвращает результаты"""
    if base_path is None:
        base_path = os.path.dirname(__file__)
    
    results = {
        'versions': get_versions(),
        'static_dir': check_static_directory(base_path),
        'face_detection': test_face_detection(base_path)
    }
    
    # Проверяем общий статус
    results['overall_success'] = all([
        results['static_dir']['exists'],
        results['face_detection']['success']
    ])
    
    return results


def print_results(results):
    """Печатает результаты тестов в консоль"""
    print('Python version:', results['versions']['python'])
    print('NumPy version:', results['versions']['numpy'])
    print('OpenCV version:', results['versions']['opencv'])
    
    print(f'\n{results['static_dir']['message']}')
    if results['static_dir']['files']:
        print(f'Files in static/: {results['static_dir']['files']}')
    else:
        print('No files in static/ directory')
    
    print(f'\n{results['face_detection']['message']}')
    
    if results['overall_success']:
        print('\n[SUCCESS] All tests passed!')
    else:
        print('\n[FAILURE] Some tests failed!')
    
    return 0 if results['overall_success'] else 1

@contextmanager
def temporary_path_addition(path):
    """Контекстный менеджер для временного добавления пути в sys.path"""
    import sys
    sys.path.insert(0, path)
    try:
        yield
    finally:
        sys.path.remove(path)

def main(run_tests=True):
    """Основная функция для запуска проверки окружения
    
    Args:
        run_tests (bool): Запускать ли тесты при импорте. По умолчанию True.
                При установке в False модуль можно импортировать без выполнения кода.
    
    Returns:
        int: Код выхода (0 для успеха, 1 для ошибки)
    """
    if not run_tests:
        return 0
        
    # Определяем директорию проекта
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Добавляем корень проекта в sys.path для импорта модулей
    with temporary_path_addition(project_dir):
        results = run_all_tests()
        exit_code = print_results(results)
        return exit_code

# Запуск при прямом вызове скрипта
# if __name__ == '__main__':
    # exit_code = main()
    # sys.exit(exit_code)
    # Убран вызов sys.exit для возможности тестирования

# Экспорт основных функций
__all__ = ['get_versions', 'check_static_directory', 'test_face_detection', 'run_all_tests', 'print_results', 'main']