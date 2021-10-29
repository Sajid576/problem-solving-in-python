

def findTuples(n,arr):
        new_arr = list(dict.fromkeys(arr))
        
        if(len(new_arr)<3):
                print("-1")
               
        else:
            new_arr.sort()
            print(new_arr)
            sol=[]
            for i in range(len(new_arr)-1):
                    if(new_arr[i+1]%new_arr[i]==0 and new_arr[i+2]%new_arr[i+1]==0 ):
                            sol.append([new_arr[i],new_arr[i+1],new_arr[i+2]] )
                            
        
            print(sol)
            if(len(sol)>0):
                    for i in range(len(sol)):
                             print(str(sol[i][0])+" "+str(sol[i][1])+" "+str(sol[i][2]) )
                            
                    return 
            else:
                print("-1")
                return


# arr = []
# n = int(input())

# strr = input()
# ele=strr.split(' ')
# element=[]
# for i in range(len(ele)):
#         element.append(  int(ele[i] ) )

# print(element)
element=[2,2,1,1,4,6]
n=6
findTuples(n,element)
