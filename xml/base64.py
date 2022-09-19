import base64

string=b"admin"

encoded=base64.b64encode(string)
decoded=base64.b64decode(string)

print(encoded)
print(decoded)

