import re
n=int(input())
for i in range(n):
    a=input()
    x=re.search(r"([-\+])?[0-9]*\.[0-9]+$", a)
    if x:
        print('True')
    else:
        print('False')
