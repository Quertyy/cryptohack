from pwn import xor

encrypted = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
flag_start = "crypto{"

for j in flag_start:
    for i in range(1,256):
        results = [chr(x ^ i) for x in encrypted]
        flag = ''.join(results)
        if j in flag:
            print(flag)
            break