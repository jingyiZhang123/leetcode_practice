class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        result = []
        s = [c for c in s]
        length = len(s)
        
        for i in range(length - 1):
            if s[i] == s[i+1] == '+':
                temp = [x for x in s]
                temp[i] = temp[i+1] = '-'
                result.append(''.join(temp))
        return result

print(Solution().generatePossibleNextMoves("++++"))