def foo(f):
    print("안녕하세요?")
    return f
@foo
def bar(y):
    return "%s 주간보고 드립니다. "%y

print(bar("전현재"))

# bar만 호출해도 @foo 가 있기 때문에 bar=foo(bar)와 같은 결과값을 나타낼 수 있다. foo를 호출하는 거라고 생각하면 된다.