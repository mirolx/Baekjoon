import sys
x=[]
y=[]
num= int(sys.stdin.readline().rstrip()) 

for i in range(num):
    a, b= map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)
points=sorted(zip(x,y))
points.sort(key=lambda point:(point[1],point[0]))

for a,b in points:
    print(a,b)

