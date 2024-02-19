from collections import Counter
import heapq

class Solution:
    def minValue(self, s, k):
        freq_map = Counter(s)

        freq = list(freq_map.values())
        freq = [-i for i in freq]
        freq.sort()

        while k > 0:
            cur = -heapq.heappop(freq)
            cur -= 1
            k -= 1
            heapq.heappush(freq,-cur)
        return sum([i**2 for i in freq])