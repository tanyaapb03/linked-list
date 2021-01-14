#get node by index 
# 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class  linkedlist():
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node= Node(new_data)
        new_node.next=self.head
            
        self.head=new_node
        
    def findnode(self,inum):
        current= self.head
        index=0
        if inum==None:
            return 

        
        while (current is not None ):
            if (index==inum):
                return current.data
            index=index+1
            current=current.next
        
    
    def printlist(self):
        temp= self.head
        while (temp):
            print("%d" % (temp.data)),
            temp= temp.next

llist=linkedlist()
llist.push(2)
llist.push(6)
llist.push(8)
llist.push(9)

llist.printlist()
print ("the ans for position is ")
print(llist.findnode(0))
x=input(" please enter the index to  be found ")
print (llist.findnode(int(x)))


