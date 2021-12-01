def pypart2(n):

    # number of spaces
    k = n - 1

    m = 1
    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        ch = 'A'
        for j in range(0, m):

            # printing stars
            #print("*", end="")
            print(str(ch), end="")
            if(j < (m//2)):
                ch = ord(ch) + 1
            else:
                ch = ord(ch) - 1
            ch = chr(ch)

        m = m+2
        # ending line after each row
        print("\r")


# Driver Code
n = 5
pypart2(n)
