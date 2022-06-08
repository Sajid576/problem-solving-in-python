# Function to check if x is power of 2*/
def isPowerofTwo(n):

    if (n == 0):
        return 0
    if ((n & (~(n - 1))) == n):
        return 1
    return 0


def result(t):
    summ = 0

    for i in range(1, t+1):
        if(isPowerofTwo(i)):
            summ -= i
        else:
            summ += i
    return summ


# drive code
N = int(input())

for i in range(N):
    T = input()
    print(result(int(T)))
