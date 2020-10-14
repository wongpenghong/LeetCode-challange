"""
	Problem: https://open.kattis.com/problems/planina
"""

renum = 2

for _ in range(eval(input())):
    renum = renum + renum - 1

result = renum**2
print(result)