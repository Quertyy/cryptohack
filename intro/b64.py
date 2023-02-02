import base64

s = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

hex_decode = bytes.fromhex(s)
print(hex_decode)
base64_encode = base64.b64encode(hex_decode)
print(base64_encode)