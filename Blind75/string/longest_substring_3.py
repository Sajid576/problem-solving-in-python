from typing import List
from my_test import test

# Sliding window approach
# https://towardsdatascience.com/leetcode-problem-3-python-3ec4ae0ae13


def lengthOfLongestSubstring(s: str) -> int:
    letter_to_indx = {}
    substr_begin = 0
    max_length = 0
    for i in range(len(s)):
        if(s[i] in letter_to_indx):
            substr_begin = max(letter_to_indx[s[i]]+1, substr_begin)
        letter_to_indx[s[i]] = i
        max_length = max(max_length, i - substr_begin+1)

    return max_length


test(lengthOfLongestSubstring("abcabcbb"), 3)
test(lengthOfLongestSubstring("bbbbb", ), 1)
test(lengthOfLongestSubstring("pwwkew"), 3)
test(lengthOfLongestSubstring(" "), 1)
test(lengthOfLongestSubstring("dvdf"), 3)
test(lengthOfLongestSubstring("abcde"), 5)
test(lengthOfLongestSubstring("abba"), 2)
