class node:
    def __init__(self, empName,empId):
        self.empId = empId
        self.empName = empName
        self.next = None
    
class singlylist:
    def __init__(self):
        self.head = None
    
    def add(self,value1,value2):
        n1 = node(value1,value2)

        if self.head is None:
            head = n1

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next=n1

    def printList(self):
        temp = self.head
        while temp is not None:
            print (temp.empId)
            print (temp.empName)
            temp = temp.next

if   __name__ == "__main__":
    list1 = singlylist()
    

    list1.head = node("Mrunal",1)
    list1.add("Neel",2)
    list1.add("Pramath",3)

    list1.printList()
    