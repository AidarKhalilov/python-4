# Задача 2.1. Все переменные объекты объекта класса
# Задача 2.2. Вызвать метод по имени
class simple:
    something = 10

    def __init__(self):
        pass

    def getResult(self):
        return self.something

    def setResult(self, something):
        self.something = something


a = simple()
print(dir(a))
print(getattr(a, 'getResult')())