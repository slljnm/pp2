s = input()
ans = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(ans)