n=int(input("Enter upto which you want sum:"))
i=1
count=0
sum=0
while count<n:
    if i%2==0:
        sum+=i
        count+=1
        i+=1
    else:
        i+=1
print(sum)