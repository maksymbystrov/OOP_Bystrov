import os
print(f"Змінна IT_TEST = {os.environ.get('IT_TEST', 'Помилка: Не знайдено!')}")