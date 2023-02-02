from Crypto.PublicKey import RSA

with open("mail.pem") as file:
    data = file.read()

print(RSA.import_key(data).d)
