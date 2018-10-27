class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        def helper(n_ob, n_cb, cur_path, result):
            
            if n_ob == n_cb == 0:
                result.append(cur_path)
                return
            if n_ob > 0:
                helper(n_ob-1, n_cb, cur_path+"(", result)
            if n_cb > n_ob:
                helper(n_ob, n_cb-1, cur_path+")", result)
            

        
        result = []
        helper(n, n, "", result)
        return result
        
        

print(Solution().generateParenthesis(3))

