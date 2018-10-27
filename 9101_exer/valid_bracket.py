class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        s = [c for c in reversed(s)]
        close_bracket = {')':'(', ']':'[', '}':'{'}
        open_bracket = []
        while s:
            
            c = s.pop()
            if c in close_bracket:
                if not open_bracket:
                    return False
                ob = open_bracket.pop()
                cb = close_bracket.get(c, None)
                if cb is None:
                    return False

                if ob != cb:
                    return False
            else:
                open_bracket.append(c)
        
        if open_bracket:
            return False
        return True

print(Solution().isValidParentheses("[(])"))
