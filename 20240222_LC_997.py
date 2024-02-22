class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc = [0] * (n+1)
        out= [0] * (n+1)

        for a,b in trust:
            out[a] += 1
            inc[b] += 1
        
        for i in range(1,n+1):
            if out[i] == 0 and inc[i] == n-1:
                return i
        
        return -1