class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cd = []
        for c in logs:
            if c == '../':
                if len(cd) > 0:
                    cd.pop()
            elif c == './':
                continue
            else:
                cd.append(c)
        return len(cd)