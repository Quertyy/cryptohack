def main(s: str, i: int):
    for j in s:
        print(chr(ord(j) ^ i))

main("label", 13)