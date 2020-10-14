"""
    Problem: https://open.kattis.com/problems/qaly
"""
# Read input
numbers = int(input())
n = 0

for _ in range(numbers):
    i, j = map(float, input().split())
    n += i*j
    
print(n)