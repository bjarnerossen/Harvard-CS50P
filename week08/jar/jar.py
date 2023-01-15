class Jar:


    def __init__(self, capacity=12, cookies=0):

        if capacity < 0:
            raise ValueError("Capacity must be a number > 0")

        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if not n > (self.capacity - self.cookies):
            self.cookies += n
        else:
            raise ValueError("Too many cookies.")

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError("Not enough cookies in the jar. Maybe consider a diet?")
        if n < 0:
            raise sys.exit(0)("Must withdraw a positive number of cookies")

        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def cookies(self):
        return self._cookies

    @capacity.setter
    def capacity(self, capacity):
        if not int(capacity) > 0:
            raise ValueError("Not a positive integer.")
        self._capacity = capacity

    @cookies.setter
    def cookies(self, cookies):
        if int(cookies) < 0:
            raise ValueError
        else:
            self._cookies = cookies