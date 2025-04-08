import sys
input = sys.stdin.readline

S = set()

N, M = map(int, input().split())

for _ in range(N):
    S.add(input().strip())

B = [input().strip() for _ in range(M)]

count = sum([1 for b in B if b in S])
print(count)
