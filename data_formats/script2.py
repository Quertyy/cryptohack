from asn1crypto.x509 import Certificate

with open("rsa.der", "rb") as file:
    cert = Certificate.load(file.read())

n = cert.public_key.native["public_key"]["modulus"]
e = cert.public_key.native["public_key"]["public_exponent"]
print(f'{n}\n')
print(e)