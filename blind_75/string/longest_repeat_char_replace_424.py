from typing import List
from my_test import test

# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/363071/Simple-Python-two-pointer-solution


def characterReplacement(s: str, k: int) -> int:


test(characterReplacement("ABAB", 2), 4)
test(characterReplacement("AABABBA", 1), 4)
