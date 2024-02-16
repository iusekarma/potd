class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for e in arr:
            if e in dic:
                dic[e] += 1
            else:
                dic[e] = 1

        dic_t = {}
        for n,f in dic.items():
            if f in dic_t:
                dic_t[f].append(n)
            else:
                dic_t[f] = [n]

        while k > 0:
            for f in sorted(dic_t.keys()):
                for n in dic_t[f]:
                    dic[n] -= min(f,k)
                    k -= min(f,k)
                    if dic[n] <= 0:
                        del dic[n]
                    if k <= 0:
                        return len(dic.keys())
        return len(dic.keys())