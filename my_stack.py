'''

@author: Jen Tat

'''
class ListNode:
    """
    Class of listNode is a data type which holds a value and a link to the next
    node in a list. This object is used in conjunction with linked list
    """
    
    def __init__(self, value):
        self._value = value
        self._link = None

    def value(self):
        return self._value

    def link(self):
        return self._link

    def newlink(self, node):
        self._link = node

    def __str__(self):
        return self._value

    
class Stack:
    
    
    def __init__(self):
        """
        Construct an empty stack with attributes
        length and top (instead of the firstnode)
        """

        self._count = 0
        self._top = None

    def top(self):
        return self._top

    def count(self):
        return self._count


    def empty(self):
        """
        Determine if the stack is empty.

        Returns
        True if stack is empty, False if not empty.
        """

        return self._count == 0

    
    def push(self, value):
        """
        Add a new item to the top of the stack.
        Similar code to the insertNewFirstNode function from LinkedList

        Parameters
        value is any data type, the value to add to stack
        """
    
        newNode = ListNode(value)

        if self._top == None:
            self._top = newNode

        else:
            newNode.newlink(self._top)
            self._top = newNode

        self._count += 1


    
    def pop(self):
        """
        Removes the top item from the stack and returns the value.
        If stack is empty returns None
        Similar code to the removeFirstNode function from LinkedList
        
        Returns
        The value of the top item. If empty return None.
        """
    
        if self._top == None:
            return None
        else:
            n = self._top
            self._top = self._top.link()
            self._count -= 1
            return n.value()


    
    def peek(self):
        """
        Return the value of the top item in the stack without removing it from the stack.

        Returns
        The value of the top item. If empty return None
        """
    
        if self._top == None:
            return None
        else:
            return self._top.value()


##    def __str__(self):
##        '''
##        Function returns the list contents as one line formatted [item, "string", etc]
##
##        Returns
##        A string in the format [item, item, item]
##        '''
##    
##        s = ""
##        n = self._top
##        
##        #iterate through list one item at a time until last item reached
##        while (n != None):
##            #check if last item in list has been reached
##            #if so, do not place a comma after the item
##            if n.link() != None:
##                
##                #check if item is type string. If so, place it in quotations
##                if type(n.value()) == str:
##                    s += "'" + str(n.value()) + "', "
##                else:
##                    s+= str(n.value()) + ", "
##            else:
##                #check if item is type string. If so, place it in quotations
##                if type(n.value()) == str:
##                    s += "'" + str(n.value()) + "'"
##                else:
##                    s+= str(n.value())
##                
##            #advance to next item in list
##            n = n.link()
##        
##        return("[" + s + "]")
    def __str__(self):
        """
        Provide the string representation for the stack to appear
        as a Python List. Used with Python's built in print function.
        [item, item, item]

        Returns
        String
        """
    
        n = self._top
        s = ""
        while (n != None):
            s += str(n.value())+ " "
            n = n.link()

        return s 

