import unittest
import os
import sys
from unittest.mock import patch, MagicMock

# Добавляем путь к src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

# Импортируем модуль после добавления пути
import context_loader

class TestContextLoader(unittest.TestCase):
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        pass
    
    def tearDown(self):
        """Очистка после каждого теста"""
        pass
    
    @patch('context_loader.setup_logging')
    @patch('context_loader.load_config')
    @patch('context_loader.initialize_database')
    @patch('context_loader.create_directories')
    def test_load_context_success(self, mock_create_directories, mock_initialize_database, mock_load_config, mock_setup_logging):
        """Тест: успешная загрузка контекста"""
        # Настройка моков
        mock_create_directories.return_value = {'success': True}
        mock_initialize_database.return_value = {'success': True}
        mock_load_config.return_value = {'debug': True}
        mock_setup_logging.return_value = {'level': 'DEBUG'}
        
        # Вызываем функцию
        result = context_loader.load_context()
        
        # Проверяем результат
        self.assertTrue(result['success'])
        self.assertIn('context', result)
        self.assertEqual(result['context']['config']['debug'], True)
        
        # Проверяем, что все функции были вызваны
        mock_create_directories.assert_called_once()
        mock_initialize_database.assert_called_once()
        mock_load_config.assert_called_once()
        mock_setup_logging.assert_called_once()
    
    @patch('context_loader.setup_logging')
    @patch('context_loader.load_config')
    @patch('context_loader.initialize_database')
    @patch('context_loader.create_directories')
    def test_load_context_directory_creation_fails(self, mock_create_directories, mock_initialize_database, mock_load_config, mock_setup_logging):
        """Тест: ошибка при создании директорий"""
        # Настройка моков
        mock_create_directories.return_value = {'success': False, 'error': 'Directory creation failed'}
        
        # Вызываем функцию
        result = context_loader.load_context()
        
        # Проверяем результат
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        self.assertIn('Directory creation failed', result['error'])
        
        # Проверяем, что другие функции не были вызваны
        mock_initialize_database.assert_not_called()
        mock_load_config.assert_not_called()
        mock_setup_logging.assert_not_called()
    
    @patch('context_loader.setup_logging')
    @patch('context_loader.load_config')
    @patch('context_loader.initialize_database')
    @patch('context_loader.create_directories')
    def test_load_context_database_init_fails(self, mock_create_directories, mock_initialize_database, mock_load_config, mock_setup_logging):
        """Тест: ошибка инициализации базы данных"""
        # Настройка моков
        mock_create_directories.return_value = {'success': True}
        mock_initialize_database.return_value = {'success': False, 'error': 'Database init failed'}
        
        # Вызываем функцию
        result = context_loader.load_context()
        
        # Проверяем результат
        self.assertFalse(result['success'])
        self.assertIn('error', result)
        self.assertIn('Database init failed', result['error'])
        
        # Проверяем, что другие функции были вызваны
        mock_create_directories.assert_called_once()
        mock_initialize_database.assert_called_once()
        mock_load_config.assert_not_called()
        mock_setup_logging.assert_not_called()

if __name__ == '__main__':
    unittest.main()