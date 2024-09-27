from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap["".join(sorted(s))].append(s)
        return hashmap.values()
