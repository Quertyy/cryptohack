from Crypto.PublicKey import RSA

with open("bruce_ssh_key.pub") as file:
    data = file.read()

print(RSA.import_key(data).n)

