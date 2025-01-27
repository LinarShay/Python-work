import inspect


def introspection_info(obj):
    # Основная информация
    info = {
        'type': type(obj).__name__,  # Тип объекта
        'attributes': {},  # Атрибуты объекта
        'methods': [],  # Методы объекта
        'module': obj.__class__.__module__,  # Модуль объекта
    }

    # Получаем все атрибуты и методы объекта
    for name in dir(obj):
        try:
            # Получаем значение атрибута
            attr = getattr(obj, name)
            # Определяем, является ли атрибут методом
            if inspect.ismethod(attr) or inspect.isfunction(attr):
                info['methods'].append(name)
            else:
                info['attributes'][name] = type(attr).__name__
        except Exception:
            # Пропускаем атрибуты, которые нельзя прочитать
            continue

    # Дополнительная информация для некоторых типов
    if isinstance(obj, (int, float, str, list, dict, set, tuple)):
        info['length'] = len(obj) if hasattr(obj, '__len__') else None
    elif isinstance(obj, type):  # Если объект — это класс
        info['bases'] = [base.__name__ for base in obj.__bases__]
        info['subclasses'] = [sub.__name__ for sub in obj.__subclasses__()]
    elif hasattr(obj, '__doc__'):
        info['docstring'] = obj.__doc__.strip() if obj.__doc__ else None

    return info


# Пример работы функции с базовыми типами данных
number_info = introspection_info(42)
print("Introspection of 42:")
print(number_info)

string_info = introspection_info("Hello, World!")
print("\nIntrospection of 'Hello, World!':")
print(string_info)

list_info = introspection_info([1, 2, 3])
print("\nIntrospection of [1, 2, 3]:")
print(list_info)

dict_info = introspection_info({'key': 'value'})
print("\nIntrospection of {'key': 'value'}:")
print(dict_info)

set_info = introspection_info({1, 2, 3})
print("\nIntrospection of {1, 2, 3}:")
print(set_info)

tuple_info = introspection_info((1, 2, 3))
print("\nIntrospection of (1, 2, 3):")
print(tuple_info)


# Создание пользовательского класса для тестирования
class MyClass:
    """Пример пользовательского класса."""

    def __init__(self, value):
        self.value = value

    def my_method(self):
        """Пример метода."""
        return self.value


# Создание экземпляра класса
my_obj = MyClass(42)

# Интроспекция экземпляра класса
my_obj_info = introspection_info(my_obj)
print("\nIntrospection of my_obj (instance of MyClass):")
print(my_obj_info)

# Интроспекция самого класса
my_class_info = introspection_info(MyClass)
print("\nIntrospection of MyClass (class itself):")
print(my_class_info)