# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(arr, n):
    if n == 0:
        return None

    head = ListNode(arr[0])
    cur = head
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next

    return head

def printLinkedList(head):
    cur = head

    while cur is not None:
        print(str(cur.val) + "->", end='')
        cur = cur.next

    print("NULL")


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return

        if node.next is None:
            node = None

        next_val = node.next
        node.val = next_val.val
        node.next = next_val.next

# solution = Solution()
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# res = solution.intersect(nums1, nums2)
# print(res)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    head = createLinkedList(arr, n)
    node = head.next.next
    printLinkedList(head)
    solution = Solution()
    solution.deleteNode(node)
    printLinkedList(head)
