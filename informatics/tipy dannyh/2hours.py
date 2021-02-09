first = list(map(int, input().strip().split()))
second = list(map(int, input().strip().split()))
res = (second[0]-first[0])*3600 + (second[1]-first[1])*60 + (second[2]-first[2])
print(res)