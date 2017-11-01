from collections import Counter

n=int(raw_input())

line=map(int,(raw_input().strip('').split()))
line.sort()

#Calculating Mean
sum=0
for i in range(0,n):
    sum=sum + line[i]
mean=float(sum/n)

#Calculating Median
sum=0
if(n%2==0):
    sum=line[n/2]+line[(n/2)-1]
    median=float(sum/2)
else:
    median=float(line[int(n/2)])

#Calculating Mode
arr=[]
data = Counter(line)
mode=data.most_common(1)[0][0]

print mean
print median
print mode