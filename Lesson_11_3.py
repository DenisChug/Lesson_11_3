import inspect
import sys
from collections import defaultdict
from pprint import pprint

def introspection_info(obj):
    data = defaultdict(list)
    data['Тип'].append(type(obj))
    data['Модуль, путь'].append(sys.modules[__name__])
    for attr in dir(obj):
        get_attr = getattr(obj, attr)
        if callable(get_attr):
            data['Функции которые можно вызвать'].append(attr)
        if inspect.isbuiltin(get_attr):
            data['Встроенные функции и методы'].append(attr)
        if inspect.isfunction(get_attr):
            data['Функции'].append(attr)
        if inspect.ismethod(get_attr):
            data['Методы'].append(attr)
        if inspect.isclass(get_attr):
            data['Классы'].append(attr)
        if inspect.ismodule(get_attr):
            data['Модули'].append(attr)
        if attr.startswith('_'):
            data['Атрибуты'].append(attr)

    return data

number_info = introspection_info(42)
pprint(number_info)