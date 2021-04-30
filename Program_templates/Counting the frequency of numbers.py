 #without dictionary
def solution(data,n):
    
    for item in data: 
        print("key: "+item+" , value: "+data.count(item))
      

    
 #with dictionary
def solution(data,n):
   
    freq = {} 
    for item in data: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1

    for key, value in freq.items():
        print(key+" "+value)

    print(freq)

solution([1,2,2,3,3,3,4,5,5],1)