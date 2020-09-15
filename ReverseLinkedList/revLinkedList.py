# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	# solution faster (iterative)
    	prev, curr = None, head

    	while curr:
    		curr.next, prev, curr = prev, curr, curr.next

    	return prev

        # ####################################
    	# solution not faster enough (iterative)
    	# new_head = None

    	# while head:
    	# 	temp = head.next
    	# 	head.next = new_head
    	# 	new_head = head
    	# 	head = temp

    	# return new_head

        # ####################################
    	# solution (recursive)
    	# NEED pay attention to the handling of the first and second node
    	# if (head == None or head.next == None) : return head

    	# prev = self.reverseList(head.next)
    	# head.next.next = head
    	# head.next = None

    	# return prev


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
    	if (len(data) == 0):return None
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
    data = [1]
    l1 = l.initList(data)
    lRev = s.reverseList(l1)
    l.printList(lRev)

if __name__ == '__main__':
    main()