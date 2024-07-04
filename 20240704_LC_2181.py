class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        out_last = out
        last_zero = False
        head = head.next
        while head:
            if head.val == 0:
                last_zero = True
            else:
                if last_zero:
                    out_last.next = ListNode(head.val)
                    out_last = out_last.next
                    last_zero = False
                else:
                    out_last.val += head.val
            head = head.next
        return out