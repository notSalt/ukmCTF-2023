somecode = 'pizza'
message = 'ukmCTF{f1x3d_1t_4_y0u}'

def str_xor(secret, key):
  new_key = key
  i = 0
  while len(new_key) < len(secret):
    new_key = new_key + key[i]
    i = (i + 1) % len(key)
  return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(secret, new_key)])

encoded = str_xor(message, somecode)
for x in encoded:
  print("chr(" + hex(ord(x)) + ") +", end = " ")
print()

flag = chr(0x5) + chr(0x2) + chr(0x17) + chr(0x39) + chr(0x35) + chr(0x36) + chr(0x12) + chr(0x1c) + chr(0x4b) + chr(0x19) + chr(0x43) + chr(0xd) + chr(0x25) + chr(0x4b) + chr(0x15) + chr(0x2f) + chr(0x5d) + chr(0x25) + chr(0x3) + chr(0x51) + chr(0x5) + chr(0x14)

decoded = str_xor(flag, somecode)
print(decoded)