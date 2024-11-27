# class Singleton:
#     __instance = None
#
#     def __init__(self):
#         if Singleton.__instance is not None:
#             raise Exception("This class is a singleton!")
#
#     @classmethod
#     @property
#     def get_instance(cls):
#         if cls.__instance is None:
#             cls.__instance = cls()
#         return cls.__instance


class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
