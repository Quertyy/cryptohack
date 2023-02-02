p = 29
ints = [14, 6, 11]

answer = [x for x in range(p) if pow(x, 2, p) in ints]

print(min(answer))