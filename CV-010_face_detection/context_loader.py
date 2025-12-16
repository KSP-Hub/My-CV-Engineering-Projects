"""
Скрипт для загрузки полного контекста проекта
"""

import json
import os
from pathlib import Path

def load_project_context(project_root: str = ".") -> dict:
    """
    Загружает полный контекст проекта
    
    Args:
        project_root: Путь к корню проекта
    
    Returns:
        Словарь с полным контекстом
    """
    project_root = Path(project_root).resolve()
    
    context = {
        "project_info": {
            "name": "My-CV-Engineering-Projects",
            "root": str(project_root),
            "structure": {},
            "status": {}
        },
        "rules": "",
        "files": {}
    }
    
    # Загрузка статуса проекта
    status_file = project_root / "project-status.json"
    if status_file.exists():
        context["project_info"]["status"] = json.loads(status_file.read_text(encoding="utf-8"))
    
    # Загрузка правил
    rules_file = project_root / "rule_My-CV-Engineering-Projects.md"
    if rules_file.exists():
        context["rules"] = rules_file.read_text(encoding="utf-8")
    
    # Сбор структуры проекта
    for item in project_root.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            context["project_info"]["structure"][item.name] = [
                f.name for f in item.iterdir() if f.is_file()
            ]
    
    # Загрузка ключевых файлов
    key_files = [
        "README.md",
        "CV-010_face_detection/README.md",
        "CV-010_face_detection/face_detection.py"
    ]
    
    for file_path in key_files:
        full_path = project_root / file_path
        if full_path.exists():
            context["files"][file_path] = full_path.read_text(encoding="utf-8")
    
    return context

if __name__ == "__main__":
    ctx = load_project_context(".")
    
    # Сохранение контекста в файл
    output_file = project_root / "context.json"
    with open("context.json", "w", encoding="utf-8") as f:
        json.dump(ctx, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Полный контекст проекта сохранен в context.json")
    print(f"📁 Найдено компонентов: {len(ctx['files'])}")
    print(f"🎯 Текущая фаза: {ctx['project_info']['status'].get('current_phase', 'N/A')}")