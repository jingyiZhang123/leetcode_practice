class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def helper(self, target):
        smallest = float('Inf')
        result = None
        for i in range(16):
            a = i * 16 + i
            temp = -(target - a)^2
            if temp < smallest:
                smallest = temp
                result = a
            else:
                break

        if result == 0:
            return '00'
        return hex(result)[2:]

    def similarRGB(self, color):
        colors = (int(color[i:i+2], 16) for i in range(1, len(color), 2))
        return '#' + ''.join(self.helper(x) for x in colors)

print(Solution().similarRGB('#22f966'))
