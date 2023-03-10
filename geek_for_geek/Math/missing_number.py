'''
https://www.geeksforgeeks.org/find-the-missing-number/

'''



def MissingNumber(array):
        d=dict()
        # removing duplicates
        for i in range(len(array)):
            d[array[i]]=True
        array=[]
        for key in d:
            array.append(key)
        print(array)
        n=len(array)
        total = (n + 1)*(n + 2)/2
        sum_of_A = sum(array)
        return total - sum_of_A
 
 
miss= MissingNumber([6,4,3,2,1,3,7,9,5,10,10,10])
print(miss)
print("----More efficient---------")

def MissingNumber(array):
        d=dict()
        # removing duplicates
        for i in range(len(array)):
            d[array[i]]=True
        array=[]
        for key in d:
            array.append(key)
        print(array)
        
        n=len(array)
        total =  1
        for i in range(2, n + 2):
            total += i
            total -= array[i - 2]
        return total
 
 
miss= MissingNumber([6,4,3,2,1,3,7,9,5,10,10,10])
print(miss)
