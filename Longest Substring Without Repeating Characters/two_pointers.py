class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)
        visited = set()
        p1 = 0
        p2 = 0
        length = 0

        while p1 < len(s):
            item = s[p1]
            if item not in visited:
                visited.add(item)
                p1+=1
                length = max(length,p1-p2)
            else:
                while s[p2] != item :
                    visited.remove(s[p2])
                    p2+=1
                visited.remove(s[p2])
                p2+=1
        return length