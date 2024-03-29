def power(a, b):
    if b == 0: return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return power(a, b // 2) ** 2 % p

n, k = map(int, input().split())
p = 10 ** 9 + 7

fac = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    fac[i] = fac[i - 1] * i % p
a, b = fac[n], (fac[k] * fac[n - k]) % p

print(power(a, p) % p * (power(b, p - 2) % p) % p)