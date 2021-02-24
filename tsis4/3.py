import re

n=input()
v = 'aeiou'
c = 'bcdfghjklmnpqrstvwxyz'
re_pat = '(?<=[' + c + '])([' + v + ']{2,})[' + c + ']'

match = re.findall(re_pat, n, re.IGNORECASE)
if match:
    print(*match, sep='\n')
else:
    print('-1')