''''https://leetcode.com/problems/longest-palindromic-substring/'''

from typing import List
import myTest
# Expand around center point

def longestPalindrome(s: str) -> str:
        if(s=='' or s== None):
                return 
        n=len(s)
        left=right=n/2
        rev_len=1
        while(left>0 and right<n and s[left]==s[right]) :
                               

myTest.myTest(longestPalindrome("babad")  ,"aba" )
myTest.myTest(longestPalindrome("cbbd")  ,"bb" )
myTest.myTest(longestPalindrome("ac")  ,"a" )
myTest.myTest(longestPalindrome("a")  ,"a" )
