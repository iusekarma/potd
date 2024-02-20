class Solution:
    def wordBreak(self, n, s, dictionary):
        for r in range(1,len(s)+1):
            if s[:r] in dictionary:
                if r == len(s):
                    return 1
                out = self.wordBreak(n,s[r:],dictionary)
                if out == 1:
                    return out
        return 0