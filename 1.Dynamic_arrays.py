import ctypes

class CustomList:

    def __init__(self):
        self.capacity = 1
        self.length = 0
        # Create a C type array with capacity -> self.capacity
        self.array = self.__create_array(self.capacity)

    def __len__(self):
        return self.length

    def append(self, value):
        # Check if array is full
        if self.length == self.capacity:
            self.__resize(self.capacity * 2)
        self.array[self.length] = value
        self.length += 1

cl = CustomList()
cl.append(10)
