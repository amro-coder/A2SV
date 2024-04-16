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
        self.printLinkedList()
        return node.value if t==0 else node

    def addAtHead(self, val: int) -> None:
        print(f"adding head {val}")
        node=Node(val)
        node.next=self.head
        self.head=node
        if not self.tail:
            self.tail=node
        self.length+=1
        self.printLinkedList()

    def addAtTail(self, val: int) -> None:
        print(f"adding tail {val}")
        node=Node(val)
        if self.tail:
            self.tail.next=node
        self.tail=node
        if not self.head:
            self.head=node
        self.length+=1
        self.printLinkedList()

    def addAtIndex(self, index: int, val: int) -> None:
        print(f"adding at index {index} value {val}")
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
        self.printLinkedList()

    def deleteAtIndex(self, index: int) -> None:
        print(f"deleting at index {index}")
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
        self.printLinkedList()
        
    def printLinkedList(self):
        return 
        # node=self.head
        # ans=[]
        # while node:
        #     ans.append(node.value)
        #     node=node.next
        # print(self.head.value,self.tail.value,self.length)
        # print(*ans)

            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)