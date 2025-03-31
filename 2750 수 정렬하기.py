import sys
x=[]

num= int(sys.stdin.readline())
for i in range(num):
    a= int(sys.stdin.readline())
    x.append(a)
    x.sort()
for i in x:
    print(i)