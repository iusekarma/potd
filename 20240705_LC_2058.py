class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crits = []
        index = 1
        last = head
        cur = head.next
        while cur.next:
            if (cur.val < last.val and cur.val < cur.next.val) or (cur.val > last.val and cur.val > cur.next.val):
                crits.append(index)
            cur = cur.next
            last = last.next
            index += 1
        
        if len(crits)<2:
            return [-1,-1]
        
        maxd = crits[-1] - crits[0]
        mind = float('inf')

        for i in range(len(crits)-1):
            mind = min(mind,crits[i+1]-crits[i])

        return [mind,maxd]