"""

    Module: sys
    Function: getsizeof()
    Desc: getsizeof() is used to get the size of an object in bytes.
    
    Syntax: 
    sys.getsizeof(object, default) 
    sys.getsizeof(object) 

    Args:
        object: The object whose size is to be determined.
        default: 
    return:
        return the size of object in bytes (int).

"""
import sys

myList = [1, 2, 3, 4, 5]
size = sys.getsizeof(myList)
print(f"size of myList: {size} bytes")
