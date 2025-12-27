"""
Скрипт для загрузки полного контекста проекта
"""

import json
import os
from pathlib import Path


def create_directories():
    """Создание необходимых директорий"""
    directories = ['static', 'configs', 'logs', 'output']
    result = {'success': True, 'created': [], 'failed': []}
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            result['created'].append(directory)
        except Exception as e:
            result['failed'].append({'dir': directory, 'error': str(e)})
            result['success'] = False
    
    return result

def load_config():
    """Загрузка конфигурации из файла"""
    try:
        with open('configs/config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        return {'success': True, 'config': config}
    except FileNotFoundError:
        return {'success': True, 'config': {}}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def initialize_database():
    """Инициализация базы данных"""
    try:
        # Здесь будет инициализация базы данных
        return {'success': True, 'message': 'Database initialized'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def setup_logging():
    """Настройка логгирования"""
    try:
        # Здесь будет настройка логгирования
        return {'success': True, 'level': 'INFO'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def load_context():
    """Загрузка полного контекста приложения"""
    # Создание директорий
    dirs_result = create_directories()
    if not dirs_result['success']:
        return {'success': False, 'error': f'Directory creation failed: {dirs_result}'}
    
    # Инициализация базы данных
    db_result = initialize_database()
    if not db_result['success']:
        return {'success': False, 'error': f'Database init failed: {db_result}'}
    
    # Загрузка конфигурации
    config_result = load_config()
    if not config_result.get('success', False):
        return {'success': False, 'error': f'Config load failed: {config_result}'}
    
    # Настройка логгирования
    logging_result = setup_logging()
    if not logging_result['success']:
        return {'success': False, 'error': f'Logging setup failed: {logging_result}'}
    
    return {
        'success': True,
        'context': {
            'directories': dirs_result,
            'database': db_result,
            'config': config_result['config'],
            'logging': logging_result
        }
    }

if __name__ == "__main__":
    ctx = load_context()
    if ctx['success']:
        print("✅ Контекст успешно загружен")
    else:
        print(f"❌ Ошибка загрузки контекста: {ctx['error']}")