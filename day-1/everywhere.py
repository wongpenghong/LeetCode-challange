"""
	Problem: https://open.kattis.com/problems/everywhere
"""

t = int(input())
for i in range(t):
    n = int(input())
    l = set()
    for j in range(n):
        l.add(input())
    print(len(l))