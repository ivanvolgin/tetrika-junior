
#РЕШЕНИЕ:
# В начале я думал над тем, можно ли каким то образом решить эту задачу без использования inspect:
# Это было бы возможно при условии, если бы у нас strict использовался только для одной функции, сигнатура которой
# была бы нам известна и она была бы неизменна, тогда бы решение могло выглядеть так:

# def strict(func):
#     def wrapper(*args, **kwargs): #
#     # В обертке указываем, точно те параметры, которые определены в сигнатуре func.
#
#     # P.S. В этом и заключается основная проблема такого подхода, потому что декоратор становится жестко привязанным к
#     # сигнатуре декорируемой функции, и если ее сигнатура изменится - все сломается.
#
#         annot = func.__annotations__

#         # Далее делаем проверки:
#         for param in (a, b):
#
#         if not isinstance(a, annot["a"]):
#             raise TypeError(f"Argument "a" must be {annot["a"].__name__}, got {type(a).__name__}")

#         if not isinstance(b, annot[b]):
#             raise TypeError(f"Argument "b" must be {annot["b"].__name__}, got {type(b).__name__}")
#
#         # В конце, если все проверки прошли успешно - возвращаем вызов func
#         return func(a, b)
#
#     return wrapper
# Это был пример плохого решения, но мы хотим чтобы наш декоратор был универсальным и работал для любых функций с любыми сигнатурами.
#
# Рабочее универсальное решение с получением сигнатуры func с помощью inspect.signature:
from inspect import signature

def strict(func):
    sig = signature(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            annot = sig.parameters[name].annotation
            if annot is not sig.empty and not isinstance(value, annot):
                raise TypeError(f"Argument {name} must be {annot.__name__}, got {type(value).__name__}")

        return func(*args, **kwargs)

    return wrapper

