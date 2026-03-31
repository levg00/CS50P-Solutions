class Jar:
    def __init__(self, capacity=12):
        size = 0
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return(self.size * "🍪")

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if size > self.capacity or size < 0:
            raise ValueError
        self._size = size


"""
def main():
    jar = Jar(10)
    while True:
        inp = input()
        match inp.strip().lower():
            case "deposit":
                jar.deposit(int(input("Deposit: ")))
                print(f"Size: {jar.size}")
            case "withdraw":
                jar.withdraw(int(input("Withdraw: ")))
                print(f"Size: {jar.size}")
            case "capacity":
                print(f"Capacity: {jar.capacity}")
            case "size":
                print(f"Size: {jar.size}")
            case "print":
                print(jar)
"""



if __name__ == "__main__":
    main()
