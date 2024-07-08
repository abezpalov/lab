class Prime:

    def __init__(self, max_quantity):
        self.prime_digits = set()
        self.max_quantity = max_quantity
        self.quantity = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.quantity >= self.max_quantity:
            raise StopIteration

        while True:
            self.current += 1
            for d in self.prime_digits:
                if self.current % d == 0:
                    break
            else:
                self.prime_digits.add(self.current)
                self.quantity += 1
                return self.current


if __name__ == '__main__':
    for n, i in enumerate(Prime(50000), 1):
        print(n, i)
