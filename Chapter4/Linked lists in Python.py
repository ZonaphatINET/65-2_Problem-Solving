# Node class
class Node:
# ตัวสร้างเพื่อเริ่มต้นอ็อบเจ็กต์โหนด
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # ฟังก์ชั่นเพื่อเริ่มต้นหัว
    def __init__(self):
        self.head = None

    # ฟังก์ชั่นเพื่อแทรกโหนดใหม่ที่จุดเริ่มต้น
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # ได้รับการอ้างอิงถึงหัวของรายการและคีย์
    # ลบการปรากฏครั้งแรกของคีย์ในรายการที่เชื่อมโยง
    def deleteNode(self, key):

##########################################################################

        # โหนดหัวเก็บ
        temp = self.head
 
        # ถ้าโหนดหัวตัวเองถือคีย์ที่จะลบ
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # ค้นหาคีย์ที่จะลบติดตามโหนดก่อนหน้าเนื่องจากเราจําเป็นต้องเปลี่ยน 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # ถ้าคีย์ไม่มีอยู่ในรายการที่เชื่อมโยง
        if(temp == None):
            return
 
        # ยกเลิกการเชื่อมโยงโหนดจากรายการที่เชื่อมโยง
        prev.next = temp.next
 
        temp = None

##########################################################################

    # ฟังก์ชั่นยูทิลิตี้เพื่อพิมพ์ LinkedList ที่เชื่อมโยง
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next

    #def printReversed():

    def printReversed_After_Deletion_1(self):#
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

        self.printList()    

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    print ("Created Linked List: ")
    llist.printList()
    print ("Created Linked List Reversed: ")
    #llist.printReversed()
    llist.deleteNode(1)
    print ("Linked List after Deletion of 1:")
    llist.printList()
    print ("Linked List after Deletion of 1 Reversed:")
    llist.printReversedDeletionOf1()