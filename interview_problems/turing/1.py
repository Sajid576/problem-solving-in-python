import collections

def canPermutePalindrome( s):
        
        count = collections.Counter(s)
        chance = 1
        for char in count:
            if count[char]%2 != 0:
                chance -= 1
                if chance < 0:
                    return False
        return True


if(canPermutePalindrome("aab")==False):
        print("Palindrome permutation not possible")
else:
        print("Palindrome permutation possible")