

def areAnagram(str1, str2):
    counters1 = []
    counters2 = []
    for i in range(256):
        counters1.append(0)
        counters2.append(0)

    for s in str1:
        counters1[ord(s) - ord('a')] += 1
    for s in str2:
        counters2[ord(s) - ord('a')] += 1

    if len(str1) != len(str2):
        return 0

    for i in range(256):
        if counters1[i] != counters2[i]:
            return 0

    return 1


# Driver code
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"

# Function call
if (areAnagram(str1, str2)):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")
