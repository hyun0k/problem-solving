import collections

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """[summary]
        연결리스트를 Deque로 바꿔서 풀이.
        """
        # q = []
        q = collections.deque()    # Deque 사용. 

        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            # if q.pop(0) != q.pop():
            if q.popleft() != q.pop():
                return False
        
        return True

# solution = Solution()
# head = [1, 2, 2, 1]
# print(solution.isPalindrome(head))
        