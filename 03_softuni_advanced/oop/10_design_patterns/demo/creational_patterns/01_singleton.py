class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
