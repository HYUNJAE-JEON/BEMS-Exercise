'''
while문을 적을 때는 변수의 값이 어떻게 변화하는지 수시로 체크해야한다.


파라미터는 기본갑슬 할당할 수 있다.
'''
from functools import reduce

reduce(list.__add__, [[1,2,3],[4,5],[6,7,8]])

reduce(+, [[1,2,3],[4,5],[6,7,8]])

'''
list는 + 연산자를 받아들일 수 없기 때문에 __add__를 쓰는 것이 좋다.
'''

for _ in range(n) :
'''
언더스코어는 다음의 경우의 수에 사용된다.

인터프리터(Interpreter)에서 마지막 값을 저장할 때
값을 무시하고 싶을 때 (흔히 “I don’t care"라고 부른다.)
변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
국제화(Internationalization, i18n)/지역화(Localization, l10n) 함수로써 사용할 때
숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때

'''