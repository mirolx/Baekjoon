import sys
x=[]
num= int(sys.stdin.readline()) #수 입력받음

for i in range(num):
    x.append(int(sys.stdin.readline())) 
x.sort()

for i in x:
    print(i)

