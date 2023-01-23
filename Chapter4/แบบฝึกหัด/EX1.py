# Node class
class Node:
# Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    #def deleteNode(self, key):
        '''เพิ่ม Code ให้สามารถลบ node แรก และ run ได้ปกติ'''

# Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next

    #def printReversed(self):
        '''เพิ่ม Code ให้สามารถกลับค่าของ Output ได้เช่น Output 1 2 3 เป็น 3 2 1'''

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    print ("Created Linked List: ")
    llist.printList()
    llist.deleteNode(1)
    print ("Linked List after Deletion of 1:")
    llist.printList()