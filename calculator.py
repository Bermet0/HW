class Calculator:

    def __init__(self, num, nume):
        self._num = num
        self._nume = nume

    def __add__(self):
        return self._num + self._nume

    def __sub__(self):
        return self._num - self._nume

    def __mul__(self):
        return self._num * self._nume

    def __truediv__(self):
        if self._nume == 0:
            return 'Error'
        else:
            return self._num / self._nume

num = 5
nume = 10

print('+:', num + nume)
print('-:', num - nume)
print('*:', num * nume)
print('/:', num / nume)
