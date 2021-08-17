


def myFunc(mylist):
        participants = []
        total=0
        for i in range(0, len(mylist)):
                a=mylist[i] 
                participants.append(( sum(a), i+1))
                total+=sum(a)
        avg=total/len(mylist)
        participants.sort(key=lambda x: x[0],reverse = True)

        for i in range(0, len(participants)):
                print("Participant"+str(i+1)+" = "+str(participants[i][1]))

        print("Participant"+str(participants[0][1])+"scored top = "+str(participants[0][0]))
        print("Participant"+str(participants[len(mylist)-1][1])+"scored lowest = "+str(participants[len(mylist)-1][0]))

        print(participants)









mylist=[]
n = int(input())
for i in range(n):
    a=input().split()
   
    for j in range(0, len(a)):
        a[j] = int(a[j])
       
    mylist.append(a)
        
myFunc(mylist)
