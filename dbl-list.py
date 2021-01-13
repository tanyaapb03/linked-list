# create a  doubly linked list 
import gc
class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        self.prev=None 

class linkedlist:
    def __init__(self):
        self.head=None 
        

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev= new_node
        self.head= new_node
    
    def dellist(self,dele):
        # bae case ie no values 
        #the one to be deleted in head node
        # the one to be deleted is not last node
        # the one to be deleted is not head node

        if self.head==None and dele==None:
            return 
        
        if self.head== dele :
            self.head=dele.next

        if dele.prev is not None:
            dele.prev.next=dele.next
        if dele.next is not None :
            dele.next.prev=dele.prev

    gc.collect()

    







    def printlist(self):
        n=self.head
        while (n is not None):
            print (n.data)
            n=n.next




llist=linkedlist()
llist.push(3)
llist.push(4)
llist.push(6)

print(llist.printlist())

llist.push(5)

print(llist.printlist())
llist.dellist(5)
print(llist.printlist())