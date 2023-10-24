import ctypes
from typing import Any


class CustomList :
    def __init__(self):
        self.size = 1    # kitne Items ko Store kar sakte ho 
        self.item = 0    # item kitne hain abhi alredy

    # Create A C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        # Create a C type array (static , referencial)with size capacity
        return(capacity*ctypes.py_object)()
    
# This Dunder Method return the length of list 
    def __len__(self):
        return self.item
    

    # This method added the data in the end 
    def append(self,new_item):
        if self.item == self.size :
            #resize
            self.__resize(self.size*2)
        #append
        self.A[self.item] = new_item
        self.item = self.item + 1

# Remove the last item of list The pop() method 
    def pop(self):
        if self.item  == 0:
            return "Empty List"
        else:
            self.item = self.item - 1 
            return self.A[self.item]
        

# Clear method mean remove the all item of list 

    def clear(self):
        self.item = 0 
        self.size = 1




    def __resize(self, new_capacity):
        #create newarray with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of A to B 
        for i in range(self.item) :
            print(i)
            B[i] = self.A[i] 
        self.A = B

# Indexing or find the element using index number 
    def __getitem__(self,index):
        if self.item >= 0 & index >=0 :
            return self.A[index]
        else:
            return 'IndexError Out Of range '
        

    def __str__(self):

        result=""
        for i in range(self.item):
            result = result + str(self.A[i]) + ","
        return  "[" + result[:-1] + "]"
    

        



    

    
obj = CustomList()
obj.append(1)
obj.append(2.4)
obj.append(2.4)
print("obj",obj)
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# obj.append(1)
# obj.append(1)
print("befor length",len(obj))

obj.clear()

print("obj",obj)
# print(obj[-1])
print("after-length",len(obj))




l = [1 ,2,3,4,5,6,6,7]
print(l.index(3))







