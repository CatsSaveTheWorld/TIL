# Python

파이썬은 대충 아는 관계로, 내용 보충 정도로 끝냄.

```
print('hello')print('world')    # Error
print('hello');print('world')   # helloworld 출력

``` 

## 변수 x, y값 변경
x = 1, y = 2 일 때 x, y 값을 서로 바꾸면?

1. 새로운 변수 생성
   ```
   
    x = x + y  
    y = x - y  
    x = x - y

    print(x, y)
   ```
2. 파이썬만의 방식
    ```
    x, y = y, x
    ```
3. 덧셈 뺄셈 응용
    ```
    x = x + y
    y = x - y
    x = x - y
    ```

a = 3.5 - 3.12  
b = 0.38

print(a == b)  
print(abs(a - b))  
print(abs(a - b) <= 1e-10)


## 복소수
```
a = 3 - 4j  
type(a)                    # complex

a.real, a.imag             # (3.0, -4.0)

com_str = complex('복소수')

type(com_str)               # ValueError: complex() arg is a malformed string
```

## Boolean
```
# 0빼고 다 True
bool(0)                                 # False
bool(1)                                 # True
bool(2)                                 # True
bool(-1)                                # True

bool(None)                              # False

bool([]), bool([1, 2])                  # (False, True)

bool([]), bool([1, 2])                  # (False, True)

# 리스트 자료형에서 값이 있으면 True
# 리스트 자료형에서 값이 없으면 False
bool([''])                              # True


# 정리
boolean 자료형에서 다 외우기 귀찮으면 대충 아래와 같이 정리할 수 있다.
값이 없으면 False, 있으면 True
```

## 문자형 (String)
```
print("나는 '자연인'이다")      # 나는 '자연인'이다
print("나는" " 자연인이다")     # 나는 자연인이다

```

import datetime

today = datetime.datetime.now()

print(today)

```
f'오늘은 {today.year}년 {today.month}월 {today.day}일 {today:%A}요일이다.'

# 혹은
# f'오늘은 {today:%Y}년 {today:%m}월 {today:%d}일 {today:%A}요일이다.'


import math
pi = math.pi

# f-string 안에서 계산 후 출력을 자제할 것.
# 아래의 코드는 그냥 이렇게도 할 수 있구나 정도로만 생각할 것.
f'원주율은 {round(pi, 2)}입니다. 반지름 2원의 넓이는 {round(pi * 2 * 2, 2)} 입니다.'
```

## 연산자

```
print('a' in 'aeiou')
print('b' in 'asdf')

list1 = ['Life', 'is', 'short', 'You', 'need', 'Python']
list2 = [1, 2, 3, 4, 5]

print('Life' in list1)
print('Python' in list1)
print(6 in list2)
print(3 in list2)

print(list1.index('short'))
# print(list1.index('python'))

# range안에 특정한 원소가 있는지 확인해봅시다.
1 in range(10)
11 in range(11)    # range(11) : 0 ~ 10
1.1 in range(10)   # range는 정수만
```

## Identity

```
# 파이썬에서 -5 부터 256 까지의 id는 동일합니다. (하도 많이 쓰는 값이라 미리 메모리를 할당하는게 좋아서 동일.)
a = 25
b = 25

print(id(a), id(b))

# 257 이루의 id 는 다릅니다.
a = 257
b = 257

print(id(a), id(b))
```

## 리스트 (List)

```
# del locations

locations = ['강남', '서초', '송파', '광진', '마포', [1],]
locations[0]
locations[0] = '양천'
locations


locations.append('동탄')
locations.append(1)
locations.append(True)
locations.append([1, 2, 3])


locations        # ['양천', '서초', '송파', '광진', '마포', [1], '동탄', 1, True, [1, 2, 3]]


locations[5] = [1, 2,]
locations        # ['양천', '서초', '송파', '광진', '마포', [1, 2], '동탄', 1, True, [1, 2, 3]]


nums1.remove(101)       # 101추가
nums1.sort()            # num1 정렬
```


### 튜플 (tuple)
```
x, y = (1, 2)
x, y            # type(x) -> int

# 혹은

x, y = 1, 2


l = [1]
t = (1)        # 쉼표를 찍으면 tuple로 처리, 안찍으면 int로 처리.

print(type(t))
print(l, t)

l = [1]
t = (1,)        # 쉼표를 찍으면 tuple로 처리, 안찍으면 int로 처리.

print(type(t))
print(l, t)
```


### range()
```
import random

numbers = [1, 2, 3, 4, 5]

# 1개만 뽑기
print(random.choice(numbers), '\n')

# 여러개 뽑기
print(random.sample(numbers, 3), '\n')

# 로또 번호 추첨
numbers = range(1, 46)
lucky = random.sample(numbers, 6)

lucky.sort()    # list에 종속된 함수라서 list.sort(), sort(object)와의 차이점은 자료형에의 '종속'이다.
lucky

# range에 담긴 값을 list로 바꿔서 확인해봅시다.
r1 = list(range(0, 9))    # 혹은 list2 = [n for n in range(0, 9)]
r1
```

## 딕셔너리
```
'''
# 내가 짠거
names = ['dowon', 'taeyoung', 'minzi']
major = ['industry', 'computer science', 'society']
sex = ['male', 'male', 'female']


info = {'names' : names, 'major' : major, 'sex' : sex}
info
# print(info.items())
# print(info.keys())
# print(info.values())
'''

# 혹은

# info = 
# {
#     'names' : ['dowon', 'taeyoung', 'minzi'], 
#     'major' : ['industry', 'computer science', 'society'], 
#     'sex' : ['male', 'male', 'female'],
# }

infos = [
    {'names' : 'dowon', 'major' : 'industry', 'sex' : 'male'},
    {'names' : 'taeyoung', 'major' : 'computer science', 'sex' : 'male'},
    {'names' : 'minzi', 'major' : 'society', 'sex' : 'female'},
]

infos
```
