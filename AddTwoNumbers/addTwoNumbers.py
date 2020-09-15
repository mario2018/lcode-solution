# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        if (len(data) == 0) : return None
        self.head = ListNode(data[0])
        r = self.head
        p = self.head

        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printList(self, head):
        if head:
            node = head
        else:
            return
        while node:
            print(node.val, end=' ')
            node = node.next
        print('\n')

def main():
    l = LinkList()
    s = Solution()
    data1 = [2,4,3]
    data2 = [5,6,4]
    l1 = l.initList(data1)
    l2 = l.initList(data2)
    l3 = s.addTwoNumbers(l1, l2)
    l.printList(l3)

if __name__ == '__main__':
    main()

        