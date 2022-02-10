def d(n):
    n = str(n)
    ans = 0
    for i in range(len(n)):
        ans += int(n[i])
    ans += int(n)
    return ans

selfnum = list(range(1,10001))

for i in range(1,10001):
    try:
        if d(i) <= 10000:
            selfnum.remove(d(i))
    except:
        continue

for j in range(len(selfnum)):
    print(selfnum[j])