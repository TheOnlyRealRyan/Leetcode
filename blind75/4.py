from collections import defaultdict

class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass
class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in res:
                res[tuple(count)] = [s]
            res[tuple(count)].append(s)
        print(list(res.values()))
            

strs = ["act","pots","tops","cat","stop","hat"]
Solution().groupAnagrams(strs)