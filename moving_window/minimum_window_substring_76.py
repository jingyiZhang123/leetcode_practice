"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        data_len, target_len = len(s), len(t)
        head = 0
        tail = -1
        targets = {x:0 for x in t}
        min_len = data_len + 1
        for i in t:
            targets[i] += 1
        min_head = 0
        min_tail = 0
        # print(all(not x for x in targets.values()))
        while head < (data_len - target_len + 1):
            if tail + 1 < data_len and any(x>0 for x in targets.values()):
                tail += 1
                if s[tail] in targets:
                    targets[s[tail]] -= 1
            else:
                if s[head] in targets:
                    targets[s[head]] += 1
                head += 1
            if all(x <= 0 for x in targets.values()):
                temp = tail - head + 1
                if temp < min_len:
                    min_len = temp
                    min_head = head
                    min_tail = tail
        if min_len == data_len + 1:
            return ""
        return s[min_head:min_tail+1]




ss = "ADOBECODEBANC"
tt = "ABC"
print(Solution().minWindow(ss, tt))














