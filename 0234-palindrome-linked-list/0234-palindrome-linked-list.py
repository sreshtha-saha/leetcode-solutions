class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True