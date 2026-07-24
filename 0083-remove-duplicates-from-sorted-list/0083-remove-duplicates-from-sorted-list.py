# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Handle empty list case
        if not head:
            return None
            
        current = head
        
        # Traverse the linked list
        while current and current.next:
            # If current value is equal to the next value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next  # Bypasses the duplicate
            else:
                current = current.next            # Move forward normally
                
        return head