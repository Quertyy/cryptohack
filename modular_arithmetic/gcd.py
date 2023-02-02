def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(66528, 52920))

# p * u + q * v = gcd(p, q) = 1
# 26513 * u + 32321 * v = 1
# 26513u = 1 - 32321v
# 
# v > u

def extended_eucl(a, b):
    if b == 0 :
        return 1,0
    else :
        u, v = extended_eucl(b, a % b)
        return v, u - (a//b) * v

print(extended_eucl(26513, 32321))