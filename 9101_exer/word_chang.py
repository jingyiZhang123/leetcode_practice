class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        
        height = len(words)
        width = len(words[0])
        
        for i in range(len(words)):
            cur_len = len(words[i])
            if(cur_len != height):
                return False
            for j in range(cur_len):
                if words[i][j] != words[j][i]:
                    return False
                
        return True
print(Solution().validWordSquare([
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]))