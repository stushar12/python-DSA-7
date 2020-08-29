import time
start_time=time.time()
class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None
		
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
		
    def insertEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode

    def reverse(self,middle):
        currentNode=self.head
        previousNode=None
        q=middle.nextNode
        if self.size%2==0:
            while(currentNode is not q):
                next=currentNode.nextNode
                currentNode.nextNode=previousNode
                previousNode=currentNode
                currentNode=next
            self.head=previousNode
        else:
            while(currentNode is not middle):
                nextNode=currentNode.nextNode
                currentNode.nextNode=previousNode
                previousNode=currentNode
                currentNode=nextNode
            self.head=previousNode

        return q


    def findmiddle(self):
        actualNode=self.head
        p=self.head
        q=self.head
        while p is not None:
            
            if p.nextNode is None:
                return q
                break
            elif p.nextNode.nextNode is None:
                return q
                break
            p=p.nextNode.nextNode
            q=q.nextNode

    def palindrome(self,p,middle):
        currentNode=self.head
        q=p
        flag=0
        if self.size == 1:
            flag=1
        else:
            if self.size%2==0:
                while currentNode is not None:
                    if currentNode.data == q.data:
                        currentNode=currentNode.nextNode
                        q=q.nextNode
                        flag=1
                    else:
                        flag=0
                        break
                
        
            else:
                while currentNode is not None:
                    if currentNode.data == q.data:
                        currentNode=currentNode.nextNode
                        q=q.nextNode
                        flag=1
                    else:
                        flag=0
                        break
        
        if flag:
            print("It is pallindrome")
        else:
            print("Not pallindrome")

		
    def traverseList(self):
	
        actualNode = self.head
		
        while actualNode is not None:
            print("%d " % actualNode.data,end=" ")
            actualNode = actualNode.nextNode


linkedlist=LinkedList()

linkedlist.insertEnd(1)
linkedlist.insertEnd(2)
linkedlist.insertEnd(3)
linkedlist.insertEnd(2)
linkedlist.insertEnd(1)




middle=linkedlist.findmiddle()

middle_next=linkedlist.reverse(middle)

linkedlist.palindrome(middle_next,middle)



print()
print(time.time()-start_time)
