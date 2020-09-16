class ListNode:
    def __init__(self, val=0, node_next=None):
        self.val = val
        self.next = node_next


class Solution:
    def detect_cycle(self, head: ListNode) -> ListNode:
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None


class LinkList:
    def __init__(self):
        self.head = None

    def init_list(self, pos, data):
        if len(data) == 0:
            return None
        self.head = ListNode(data[0])
        rear = self.head
        if pos == 0:
            cycle_entry = self.head

        counter = 0
        for i in data[1:]:
            node = ListNode(i)
            rear.next = node
            rear = rear.next
            counter += 1
            if counter == pos:
                cycle_entry = rear
        if pos > 0:
            rear.next = cycle_entry
        return self.head

    def print_node_pos(self, node, head):
        if node:
            pos_counter = 0
            ref = head
            while node != ref:
                ref = ref.next
                pos_counter += 1
        else:
            pos_counter = -1

        print(pos_counter, end='\n')


def main():
    linked_list_obj = LinkList()
    solution = Solution()
    data = [5, 2, 9]
    linked_list = linked_list_obj.init_list(2, data)
    cycle_entry_node = solution.detect_cycle(linked_list)
    linked_list_obj.print_node_pos(cycle_entry_node, linked_list)


if __name__ == '__main__':
    main()