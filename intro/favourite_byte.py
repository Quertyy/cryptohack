import base64
from pwn import xor

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_string = bytes.fromhex(hex_string)
for i in range(1,256):
    results = [chr(x ^ i) for x in bytes_string]
    flag = ''.join(results)
    if 'crypto' in flag:
        print(flag)
        break