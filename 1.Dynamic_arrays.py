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

    def find(self, value):
        for i in range(self.length):
            if self.array[i] == value:
                return i
        return "ValueError - not in list"

    def count(self, value):
        occurrence = 0
        for i in range(self.length):
            if self.array[i] == value:
                occurrence += 1
        return occurrence

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return "IndexError"
        if self.length == self.capacity:
            self.__resize(self.capacity * 2)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.length += 1

    def remove(self, value):
        index = self.find(value)
        if type(index) == int:
            self.__delete_item(index)
        else:
            return index

    def reverse(self):
        for i in range(self.length // 2):
            self.array[i], self.array[self.length - 1 - i] = self.array[self.length - 1 - i], self.array[i]

    def sort(self):
        # Convert the CustomList to a Python list for sorting
        python_list = [self.array[i] for i in range(self.length)]
        # Use Timsort (Python's built-in sort)
        python_list.sort()
        # Update the CustomList with the sorted values
        for i in range(self.length):
            self.array[i] = python_list[i]

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def slice(self, start=0, end=None, step=1):
        if end is None:
            end = self.length
        if start < 0 or end > self.length or step <= 0:
            return "IndexError"
        sliced_list = CustomList()
        for i in range(start, end, step):
            sliced_list.append(self.array[i])
        return sliced_list

    def __resize(self, new_capacity):
        # Create a new array with a larger capacity
        new_array = self.__create_array(new_capacity)
        self.capacity = new_capacity
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        result = ""
        for i in range(self.length):
            result += str(self.array[i]) + ","
        return "[" + result[:-1] + "]"

    def __getitem__(self, index):
        if 0 <= index < self.length:
            return self.array[index]
        elif -self.length <= index < 0:
            return self.array[self.length + index]
        else:
            return "IndexError"

    def __delete_item(self, index):
        if 0 <= index < self.length:
            for i in range(index, self.length - 1):
                self.array[i] = self.array[i + 1]
            self.length -= 1
        else:
            return "IndexError"

    def __create_array(self, capacity):
        return (capacity * ctypes.py_object)()

# Example usage:
cl = CustomList()
cl.append(10)
cl.append(20)
cl.append(30)
cl.insert(1, 15)
print(cl)  # [10,15,20,30]
cl.remove(15)
print(cl)  # [10,20,30]
print(cl.pop())  # 30
print(cl)  # [10,20]
cl.reverse()
print(cl)  # [20,10]
cl.extend([40, 50, 60])
print(cl)  # [20,10,40,50,60]
sliced = cl.slice(1, 4)
print(sliced)  # [10,40,50]
cl.sort()
print(cl)  # [10,20,40,50,60]
print(cl.count(20))  # 1
