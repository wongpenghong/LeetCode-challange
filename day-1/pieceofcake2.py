"""
	Problem: https://open.kattis.com/problems/pieceofcake2
"""

n, h, v = map(int, input().split())

sliceone = h * v * 4
slicetwo = h * (n-v) * 4
slicethree = (n-h) * v * 4
slicefour = (n-h) * (n-v) * 4

print(max(sliceone, slicetwo, slicethree, slicefour))