# demonstrate deletion in sigly llist 

class Node:

    def __init__(self,data):
        self.data = data
        self.next= None

class linkedlist:
# inititalising head
    def __init__(self):
        self.head= None

#inserting node in begning 

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

# deleting a node with key(data)

    def delnode(self, key):
        temp=self.head
        #if key is the first value 
        if (temp is not None):
            if (temp.data==key):
                self.head=temp.next
                temp=None
                return

        # if we have to loop to find key in llist 

        while (temp is not None ):
            if (temp.data==key):
                break
            prev= temp
            temp=temp.next

        # if key is not in list 

        if (temp==None):
            return

        # setting keys previous number to keys next number so that key is deleted 
        prev.next = temp.next
  
        temp = None
  
    # print linked list 

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
llist.delnode(6)
llist.printlist()

