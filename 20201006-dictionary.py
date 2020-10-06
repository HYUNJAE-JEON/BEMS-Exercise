print("채팅을 시작합니다.")

i = 1
d = {"사랑해": "나도"}
for i in range(1, 10):
    say = input("당신 >>> ")
    print(" 심심이 >>> ", d.setdefault(say, say))
    i += 1

print(d)
