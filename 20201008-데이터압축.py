import zlib
s = 'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s.encode())
print(len(t))
zlib.decompress(t).decode()
print(zlib.decompress(t).decode())
zlib.crc32(s.encode())
print(zlib.crc32(s.encode()))

# 들어갈 때는 encode 내보낼 때는 decode 하면 압축파일을 만들 수 있다.