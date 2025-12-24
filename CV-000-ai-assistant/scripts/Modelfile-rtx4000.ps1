@'
FROM deepseek-coder:6.7b-instruct-q4_K_M

# Ключевые настройки для Quadro RTX 4000 8GB
PARAMETER num_gpu 35  # Используем ~5.5GB VRAM из 8GB
PARAMETER num_thread 16  # Используем 16 потоков CPU (20 есть всего)
PARAMETER num_ctx 2048  # Уменьшаем контекст для экономии памяти
PARAMETER temperature 0.1  # Меньше креативности = быстрее
PARAMETER top_k 20
PARAMETER top_p 0.85
PARAMETER repeat_penalty 1.05

# Системный промпт для CV проектов
SYSTEM """
Ты - эксперт по компьютерному зрению и инженерии. 
Оборудование пользователя: Dell Precision 7920 с Quadro RTX 4000 (8GB).
Отвечай кратко, технично, с фокусом на OpenCV, PyTorch, TensorFlow.
Всегда на русском языке.
"""
'@ | Out-File -FilePath "Modelfile-rtx4000"

# Создаём оптимизированную модель
ollama create cv-rtx4000 -f "Modelfile-rtx4000"