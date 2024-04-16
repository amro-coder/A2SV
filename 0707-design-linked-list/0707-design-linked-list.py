class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def get(self, index: int,t=0) -> int:
        if index>=self.length:
            return -1
        node=self.head
        for i in range(index):
            node=node.next
        return node.value if t==0 else node

    def addAtHead(self, val: int) -> None:
        node=Node(val)
        node.next=self.head
        self.head=node
        if not self.tail:
            self.tail=node
        self.length+=1

    def addAtTail(self, val: int) -> None:
        node=Node(val)
        if self.tail:
            self.tail.next=node
        self.tail=node
        if not self.head:
            self.head=node
        self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length:
            return 
        if index==self.length:
            self.addAtTail(val)
        elif index==0:
            self.addAtHead(val)
        else:
            node=self.get(index-1,1)
            newNode=Node(val)
            newNode.next=node.next
            node.next=newNode
            self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.length:
            return 
        if index==0:
            self.head=self.head.next
        else:                
            node=self.get(index-1,1)
            node.next=node.next.next
            if index==self.length-1:
                self.tail=node
            
        self.length-=1
        


            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)