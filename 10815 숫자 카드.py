import sys
input=sys.stdin.readline

n = int(input())
cards = set(input().split())

m = int(input())
targets = input().split()

result = ["1" if i in cards else "0" for i in targets]


print(' '.join(result))
