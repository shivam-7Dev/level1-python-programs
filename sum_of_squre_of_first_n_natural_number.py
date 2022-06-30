from re import I


n=int(input("Enter upto which yo want sum:"))
i=1
sum=0
while i<=n:
    sum+=i*i
    i+=1
print(sum)