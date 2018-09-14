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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = dummyHead

        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

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
    head = solution.removeElements(head, 3)
    printLinkedList(head)
