'''

인터프리터 = 통역
추상화된 형태로 만들어 주는 것을 객체지향적 (0101이 아니다)
동적 타이핑 = dynamically typed - 대화형 언어 - 타입을 선언하지 않는다. 한 줄 한 줄 통역하니까 정수쓸건지 실수 쓸건지
미리 얘기할 필요가 없다.

'''

'''
자동 가비지 컬렉션(GC) - 파이썬은 자동으로 코드를 정리해준다.

EXTENDABLE - 
Scalable - 조금씩 수정하면서 확장하는 것

파이썬은 멀티패러다임 언어이다.(함수형, 명령형, 객체지향형)
파이썬이 유지보수가 쉬운 이유는 코드가 가독성이 좋기 때문이다.
파이썬으로 프로그래밍할 때 주의할 점은 이름공간이다.
'''

'''
역슬래시를 이용하여 이어주거나 ''''''을 사용할 수도 있고 기다란 문자열에는 ''''''을 사용할 수 있다.
'''

'''
0.1+0.2 에 대한 부동소수점 오류로 0.30000000000000004 이게 나온다.
'''

'''
리스트는 저장형으로 변경이 가능하다.
튜플은 하나 하나의 인덱스가 변경이 불가하다.
'''
print(3*7+5, end="")
print("idontknow")
'''
end 라는 인자는 프린트가 new line을 안하도록 만들어준다.
'''
print(3*7+5, end="\n\t")
'''
역슬래쉬 n이 의미하는 것은 new line, 역슬래쉬 t 는 tab을 뜻한다.
'''

'''
index와 slicing은 어딜 가도 많이 쓰인다.
'''

'''
문자열을 .split 함수로 쓰면 list로 바뀐다.
'''
STR = "MDS ACADEMY"
STR.split()
['MDS', 'ACADEMY']
STR.split()[1]
'ACADEMY'


'''
단어와 단어 사이를 " " 공백으로 구분하겠다.
'''

" ".join(LST)
'MDS EMBEDDED ACADEMY.'

'''

스트링은 불변성이기 때문에 리스트로 주무르고 다시 원상태로 바꾸는 거다. 
STR = "MDS ACADEMY"
>>> STR.split()
['MDS', 'ACADEMY']
>>> STR.split()[1]
'ACADEMY'
>>> STR.split().insert(1,"EMBEDDED")
>>> STR
'MDS ACADEMY'
>>> LST = STR.split().insert(1,"EMBEDDED")
>>> LST
>>> LST = STR.split()
>>> LST.insert(1,"EMBEDDED")
>>> LST
['MDS', 'EMBEDDED', 'ACADEMY']
>>> LST[2]+="."
>>> LST
['MDS', 'EMBEDDED', 'ACADEMY.']
>>> " ".join(LST)
'MDS EMBEDDED ACADEMY.'
>>> "-".join(LST)
'MDS-EMBEDDED-ACADEMY.'
>>> STR = " ".join(LST)
>>> STR
'MDS EMBEDDED ACADEMY.'
>>> 

'''

'''
swapcase() - 대문자와 소문자를 바꾸는 것

'''

'''
>>> courses = ['CIT591', 'CIT 592', 'CIT593']
>>> courses[2]
'CIT593'
>>> courses[0][-1]
'1'
>>> print(courses[2], courses[1], courses[0])
CIT593 CIT 592 CIT591
>>> courses = ['CIT591', 'CIT592', 'CIT593']
>>> print(courses[2], courses[1], courses[0])
CIT593 CIT592 CIT591
>>> print(courses[2: :-1])
['CIT593', 'CIT592', 'CIT591']

인덱스 2번으로부터 끝을 생략하고 증감값을 -1을 줌으로써 거꾸로 나오게 할 수 있다.

'''