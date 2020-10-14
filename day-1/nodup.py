"""
	Problem: https://open.kattis.com/problems/nodup
"""

listOfWord = [word for word in input().split()]
listOfAnswer = set()

for x in listOfWord:
	# add set can't add same character
    listOfAnswer.add(x)
if len(listOfWord) == len(listOfAnswer):
    print("yes")
else:
    print("no")
    