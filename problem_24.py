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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = dummyHead
        while p is not None and p.next is not None and p.next.next is not None:
            node1 = p.next
            node2 = p.next.next
            next = p.next.next.next
            p.next = node2
            node2.next = node1
            node1.next = next

            p = node1

        return dummyHead.next

# solution = Solution()
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# res = solution.intersect(nums1, nums2)
# print(res)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    head = createLinkedList(arr, n)
    printLinkedList(head)
    solution = Solution()
    head = solution.swapPairs(head)
    printLinkedList(head)
