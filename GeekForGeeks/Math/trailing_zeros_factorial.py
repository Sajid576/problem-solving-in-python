'''
    Trailing zeroes in factorial
    Input:
N = 5
Output:
1
Explanation:
5! = 120 so the number of trailing zero is 1.

    Input:
N = 4
Output:
0
Explanation:
4! = 24 so the number of trailing zero is 0.


Answer:  https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
'''

def calc_trailing_zeros(num):
     
        factorial=1
        # check if the number is negative, positive or zero
        if num < 0:
                print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
                print("The factorial of 0 is 1")
        else:
                for i in range(1,num + 1):
                    factorial = factorial*i
                print("The factorial of",num,"is",factorial)


for i in range(101):
    calc_trailing_zeros(i)               

def findTrailingZeros(n):
    # Negative Number Edge Case
    if(n < 0):
        return -1
 
    # Initialize result
    count = 0
    
    # Keep dividing n by
    # 5 & update Count
    while(n >= 5):
        n //= 5
        count += n
 
    return count
 
 
# Driver program
n = 10
print("Count of trailing 0s in "+str(n)+"! is  "+str( findTrailingZeros(n) ) )


