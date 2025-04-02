import sys

age = []
name = []
num = int(sys.stdin.readline())

for i in range(num):
    a, b = sys.stdin.readline().split()  # a는 age, b는 name
    age.append(int(a))  # age는 정수로 저장 (정렬을 위한 준비)
    name.append(b)  # name은 그대로 저장

# age를 기준으로 오름차순 정렬, 같은 age는 입력받은 순서대로 유지
x = sorted(zip(age, name), key=lambda x: x[0])

for i, j in x:
    print(i, j)
