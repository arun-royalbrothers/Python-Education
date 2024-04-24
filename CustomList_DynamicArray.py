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
    """def __getitem__(self, index):
        if index >= self.n:
            return "IndexError - Index Out Of Range"
        if index < 0:
            try:
                return self.A[self.n+index]
            except:
                return []
        return self.A[index]"""

    #adding slicing to the get_item   
    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                try:
                    return self.A[self.n+index]
                except:
                    return "Index out of range"
            if index >= self.n:
                return "Index out of range"
            return self.A[index]
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            #checking that is it's none and assign a value
            #for start check if it's none. if it's none assigning 0
            start = start if start is not None else 0
            #and also for stop, if it's none assigning self.n
            stop = stop if stop is not None else self.n
            #and for step assigning 1 as default
            step = step if step is not None else 1

            #creating a new array
            new_li = MyList()
            #checking that start and step is > self.n
            if start >= self.n:
                return new_li
            if stop > self.n:
                stop = self.n
            #running an loop and adding element to new_li
            for i in range(start, stop, step):
                new_li.append(self.A[i])
            return new_li
        else:
            return "Invalid Option"

    #finding element index
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        else:
            return "Not in the List"

    #inserting element using index
    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n+=1

    #delete an item
    def __delitem__(self, pos):
        if pos < 0:
            try:
                pos = self.n+pos
            except:
                return "Index out of range"
        for i in range(pos, self.n-1):
            self.A[i] = self.A[i+1]
        self.n-=1

    #remove an item by using value
    def remove(self, value):
        pos = self.find(value)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
    
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

    #concatenate array using + operator
    def __add__(self, other_li):
        new_li = MyList()
        #first appending the self.A element
        for i in range(self.n):
            new_li.append(self.A[i])
        #then appending the other_list element
        for i in range(len(other_li)):
            new_li.append(other_li[i])
        #then returning new_li
        return new_li
        
    
