"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""

bits = [(8,0), (4,0), (2,0), (1,0),
        (0,32), (0,16), (0,8), (0,4), (0,2), (0,1)]
class Solution(object):
    def _read(self, soFar, rest, level):
        if level == 0:
            self.result.append(soFar)
            return
        if not rest:
            return

        for i in range(len(rest)):
            next = rest[i]
            remaining = rest[i+1:]
            self._read(soFar+[next], remaining, level - 1)


    def readBinaryWatch(self, num):
        if not num:
            return ['0:00']
        self.result = []
        self._read([], bits, num)
        result = []
        for i in self.result:
            temp = [sum(x) for x in list(zip(*i))]
            if temp[0] <= 11 and temp[1] <= 59:
                temp = '%d:%02d'%(temp[0], temp[1])
                result.append(temp)

        return result


a = Solution().readBinaryWatch(0)
for i in a:
    print(i)









