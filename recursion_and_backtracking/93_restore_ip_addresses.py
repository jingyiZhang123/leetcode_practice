"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):
    def _restore(self, soFar, rest):
        if not rest:
            if len(soFar) == 4:
                self.result.append(soFar)
            return
        if len(soFar) >= 4:
            return
        for i in range(0, min(3, len(rest))):
            next = rest[:i+1]
            if int(next) > 255 or (len(next) > 1 and next[0] == '0' ):
                continue
            remaining = rest[i+1:]
            self._restore(soFar+[next], remaining)

    def restoreIpAddresses(self, s):
        self.result = []
        self._restore([], s)
        return ['.'.join(x) for x in self.result]


print(Solution().restoreIpAddresses('0000'))








