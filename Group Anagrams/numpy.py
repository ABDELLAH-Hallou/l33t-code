from collections import defaultdict
import numpy
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        s = numpy.array([''.join(sorted(s)) for s in strs])
        sort_index = numpy.argsort(s)
        for i in sort_index:
            if "".join(sorted(strs[i])) == s[i]:
                hashmap[str(s[i])].append(strs[i])
        return hashmap.values()
