import base64
from cryptography.fernet import Fernet

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
file = open("payload.txt", "r")
payload_dec = file.read()
payload = f.encrypt(payload_dec.encode())
print(payload)