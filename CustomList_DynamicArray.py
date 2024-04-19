import ctypes

#creating own list
class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()

    #print
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result+str(self.A[i])+", "
        return "["+result[:-2]+"]"

    #len
    def __len__(self):
        return self.n

    #representing
    def __repr__(self):
        return self.__str__()

    #adding element
    def append(self, val):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = val
        self.n+=1

    def __resize(self, new_size):
        B = self.__make_array(new_size)
        self.size = new_size
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    #getting elements using index
    def __getitem__(self, index):
        if index >= self.n:
            return "IndexError - Index Out Of Range"
        if index < 0:
            try:
                return self.A[self.n+index]
            except:
                return []
        return self.A[index]

    #pop element
    def pop(self):
        if self.n == 0:
            return "Empty List"
        index = self.n-1
        self.n-=1
        return self.A[index]

    #clear
    def clear(self):
        self.n = 0
        self.size = 1
        
    
