# Декоратор logger для логирования вызова функции и её результата
def logger(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        args_str = ', '.join([str(arg) for arg in args])
        kwargs_str = ', '.join([f"{k}={v}" for k, v in kwargs.items()])
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"🔍 Вызывается функция '{func_name}' с аргументами: {all_args}")
        result = func(*args, **kwargs)
        print(f"✅ Функция '{func_name}' завершила выполнение. Результат: {result}")
        print("-" * 50)
        
        return result
    return wrapper

# Функция сложения двух чисел
@logger
def add(a, b):
    return a + b

# Функция деления двух чисел с обработкой деления на ноль
@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

# Функция приветствия
@logger
def greet(name):
    return f"Привет, {name}!"

# Декоратор require_role для проверки прав доступа
def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            user_role = user.get('role', '')
            user_name = user['name']
            if user_role not in allowed_roles:
                return f"🚫 Доступ запрещён: пользователь {user_name} (роль: {user_role}) не имеет прав"
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# Функция удаления базы данных (только для admin)
@require_role(["admin"])
def delete_database(user):
    return f"🗑 База данных успешно удалена пользователем {user['name']}"

# Тестирование декораторов
def main():
    print("=== Тестирование декоратора логирования ===")
    print("\n📌 Тест 1: Сложение чисел")
    add(5, 3)
    
    print("\n📌 Тест 2: Деление чисел")
    divide(10, 2)
    
    print("\n📌 Тест 3: Деление на ноль")
    divide(10, 0)
    
    print("\n📌 Тест 4: Приветствие")
    greet("Алиса")
    
    print("\n=== Тестирование декоратора доступа ===")
    users = [
        {"name": "Алекс", "role": "admin"},
        {"name": "Боб", "role": "manager"},
        {"name": "Чарли", "role": "user"}
    ]
    
    for user in users:
        print(f"\n👤 Пользователь: {user['name']} (роль: {user['role']})")
        print(delete_database(user))
        print("-" * 50)

# Запускаем тесты
if __name__ == "__main__":
    main()