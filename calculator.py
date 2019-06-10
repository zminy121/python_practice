class Count:
    def __init__(self, a, b):
        self._a = int(a)
        self._b = int(b)

    def add(self):
        return self._a + self._b

    def sub(self):
        return self._a - self._b