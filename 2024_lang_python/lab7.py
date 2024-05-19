import numpy as np


class Matrix:

    def __init__(self, n: int):
        self.n = n
        self.values = 2 * np.random.random((self.n, self.n)) - 1

    def __str__(self):
        return str(self.values)

    def modify(self):
        for j in range(self.n):
            max_value = self.values[0][j]
            max_i = 0
            for i in range(1, self.n):
                if np.abs(self.values[i][j]) < np.abs(max_value):
                    max_i = i
                    max_value = self.values[i][j]
            self.values[max_i][j] = 0.0

    def make_c(self, b):
        e = np.diag(np.ones(self.n))
        result = (self.values + 15 * e) * (2 * self.values - b.values).T / np.abs(b.values).max()
        return result

    def make_d(self, b):
        result = 2 * ((self.values * b.values) * (self.values * b.values) - (self.values + b.values).T
                      / np.abs(self.values).min())
        return result


if __name__ == '__main__':

    a = Matrix(5)
    b = Matrix(5)
    print(a)
    print(b)

    c = a.make_c(b)
    print(c)

    d = a.make_d(b)
    print(d)

    a.modify()
    print(a)
