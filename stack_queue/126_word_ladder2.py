"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

1.Only one letter can be changed at a time
2.Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""

from collections import deque, defaultdict
from string import ascii_lowercase
from copy import deepcopy

class Solution(object):
    def _find_close_words(self, word, wordList, wordlen):
        result = set()
        for i in range(wordlen):
            for c in ascii_lowercase:
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    result.add(next_word)
        return result

    def get_info(self, begin, target, wordList):
        info = defaultdict(set)
        word_len = len(begin)
        stack = deque([(begin, 0)])
        while stack:
            word, distance = stack.pop()
            for i in range(word_len):
                for c in ascii_lowercase:
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        stack.appendleft((next_word, distance+1))
                        info[distance+1].add(next_word)
                        if next_word == target:
                            return info, distance+1
        return None

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # wordList.append(endWord)
        wordList = set(wordList)
        word_len = len(beginWord)

        temp = self.get_info(beginWord, endWord, deepcopy(wordList))
        if not temp:
            return []
        info, min_dis = temp[0], temp[1]
        info[min_dis] = set([endWord])
        for i in range(min_dis-1, 0, -1):
            successor = set()
            for word in info[i+1]:
                temp = self._find_close_words(word, wordList, word_len)
                successor |= temp
            info[i] &= successor

        info[0] = set([beginWord])

        tree = defaultdict(list)
        for i in range(0, min_dis):
            for word1 in info[i]:
                for word2 in info[i+1]:
                    diff = 0
                    for j in range(word_len):
                        if word1[j] != word2[j]:
                            diff += 1
                            if diff >= 2:
                                break
                    else:
                        if diff == 1:
                            tree[word1].append(word2)
        stack = [(beginWord, [beginWord])]
        result = []
        while stack:
            word, path = stack.pop()
            if word in tree:
                for next_word in tree[word]:
                    if next_word == endWord:
                        result.append(path+[endWord])
                    stack.append((next_word, path+[next_word]))
        return result



print(Solution().findLadders("hit", 'cog', ["hot","dot","dog","lot","log"]))

from queue import PriorityQueue
from random import randint

q = PriorityQueue()
for i in range(10):
    q.put(randint(0,100))

for i in range(10):
    aa = q.get()
    print(aa)












