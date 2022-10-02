class Jar:
    def __init__(self, capacity=12):
        # self._capacity = capacity
        # self._size = capacity
        # print(capacity)
        if capacity >= 0:
            self._capacity = int(capacity)
            self._size = 0
        else:
            raise ValueError

    def __str__(self):
        # print(self.size)
        return("🍪" * self.size)

    def deposit(self, n):
        # print(self._capacity)
        # print(n)
        total = n + self._size
        # print(total)
        if n < 0 or total > self._capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n < 0 or n > self._size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

# def main():
#     jar = Jar()
#     print(jar.capacity)
#     print(jar.size)
#     print(jar)

#     jar = Jar(12)
#     jar.deposit(2)
#     print(jar.capacity)
#     print(jar.size)
#     print(jar)

#     jar.withdraw(2)
#     print(jar.capacity)
#     print(jar.size)
#     print(jar)

#     jar.deposit(12)
#     print(jar.capacity)
#     print(jar.size)
#     print(jar)

#     jar = Jar(4)
#     jar.deposit(4)
#     jar.withdraw(1)
#     print(jar.capacity)
#     print(jar.size)
#     print(jar)

#     jar.deposit(2)
#     print(jar.capacity)
#     print(jar.size)
#     print(jar)

# if __name__ == '__main__':
#     main()