import math

n = int(input())
ans = 0

# a_harmonic_series
for i in range(1, n+1):
    ans += 1/i

print(ans)
print(math.log(n+1))

error_rate = (ans - math.log(n+1)) / math.log(n+1)
errors = ans - math.log(n+1)

print(errors)
print(error_rate)