class A:
    pass

class B(A):
    pass

class C(A, B):
    pass


# Объяснение: Python должен решить, в каком порядке искать
# базовые классы (прямые и косвенные) при поиске атрибута/метода экземпляра.
# Он делает это путем линеаризации графа наследования, то есть путем
# преобразования графа базовых классов в последовательность с
# использованием алгоритма, называемого C3 или MRO . Алгоритм MRO —
# это уникальный алгоритм, который обеспечивает несколько желаемых свойств:
# 1. каждый класс-предок появляется ровно один раз
# 2. класс всегда появляется перед своим предком («монотонность»)
# 3. прямые родители одного и того же класса должны появляться в том же
#    порядке, в котором они перечислены в определении
#    класса («согласованный локальный порядок приоритета»)
# 4. если дочерние элементы класса A всегда появляются перед дочерними
#    элементами class B, то A должны появляться
#    перед B(«согласованный расширенный порядок приоритета»)