# definition of node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


# definiton of LinkedList
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        node = Node(data, None)
    
        temp = self.head
        if temp == None:
            self.head = node
            return
        
        while temp.next:
            temp = temp.next
        temp.next = node
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at_index(self, index):
        if index<0 or index >= self.get_length():
            raise Exception("Not a valid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
            
    def insert_at_index(self, index, value):
        if index < 0 or index > self.get_length():
            raise Exception("Not a valid Index")
    
        if index == 0:
            self.insert_at_beginning(value)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = Node(value, itr.next)
                break
            count+=1
            itr = itr.next
            
    
    def print(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        
        llst = ''
        itr = self.head
        
        while itr:
            llst += str(itr.data)+'--->'
            itr = itr.next
            
        print(llst)
