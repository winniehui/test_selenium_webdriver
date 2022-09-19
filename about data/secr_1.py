import hashlib

md5_1 = hashlib.md5()
md5_1.update(b"I'm using md5 in python")
print(md5_1.hexdigest())

md5_2 = hashlib.md5()
md5_2.update(b"I'm using md5")
md5_2.update(b" in python")
print(md5_2.hexdigest())

#使用SHA-1加密
sha1 = hashlib.sha1()
sha1.update(b"I'm using md5 in python")
print(sha1.hexdigest())