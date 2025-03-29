import sys
x=[]
y=[]
num= int(sys.stdin.readline()) 

for i in range(num):
    a, b= map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)
points=sorted(zip(x,y))

for a,b in points:
    print(a,b)

