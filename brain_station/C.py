

def palindromes(start, end):
    if(start > end):
        temp = start
        start = end
        end = temp
    count = 0
    for i in range(start, end + 1):
        if str(i) == str(i)[::-1]:
            count += 1
    return count


# drive code
c = int(input())

for i in range(c):
    x, y = input().split()
    cnt = palindromes(int(x), int(y))
    print('Case ' + str(i+1)+': ' + str(cnt))
