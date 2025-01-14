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

    def pop(self, index=None):
        if self.length == 0:
            return "Empty List"
        if index is None:
            index = self.length - 1
        if 0 <= index < self.length:
            item = self.array[index]
            self.__delete_item(index)
            return item
        return "IndexError"
        
    def clear(self):
        self.length = 0
        self.capacity = 1
        self.array = self.__create_array(self.capacity)

cl = CustomList()
cl.append(10)
