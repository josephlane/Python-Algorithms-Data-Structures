import cytypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if k < 0 or k >= self.n:
            return IndexError('K is out of bounds!')

        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity) #2x if capacity isn't enough

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap


    def make_array(self, new_cap):
        return (new_cap * cytype.py_object)() #this line essentially creates the raw memory array



arr = DynamicArray()
arr.append(1)
len(arr)
        
            
            
