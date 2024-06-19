
# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
# При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)

class EvenNumbers:

    def __iter__(self):
        return self

    def __init__(self, end):
        self.end = end
        self.start = 9

    def __next__(self):
        if self.start % 2 == 0:
            self.start += 1
        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            raise StopIteration()

en = EvenNumbers(25)
print(en)
for i in en:
    print(i)