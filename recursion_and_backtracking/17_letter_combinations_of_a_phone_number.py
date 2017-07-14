"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

mapping = {'2': 'abc',
           '3': 'def',
           '4': 'ghi',
           '5': 'jkl',
           '6': 'mno',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}

class Solution(object):
    def _comb(self, soFar, rest):
        if not rest:
            if soFar: self.result.append(soFar)
            return

        for char in mapping[rest[0]]:
            next = char
            remaining = rest[1:]
            self._comb(soFar+next, remaining)

    def letterCombinations(self, digits):
        self.result = []
        self._comb("", digits)
        return self.result

print(Solution().letterCombinations(''))


