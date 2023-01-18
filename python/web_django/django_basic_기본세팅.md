# Django
## 가상환경
파이썬으로 개발을 하다보면 필연적으로 라이브러리를 사용하게 되는데, 필요없는 부분까지 존재하게 된다.

이럴 경우, 따로 독립된 공간을 만들어서 필요한 패키지만 존재하게 할 수 없나? 라는 생각이 들때가 있다.

바로 이럴때 사용하는게 가상환경이다.

아래의 그림을 보자.
![img](./%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD_1.png)

위 그림에서 위에 그려진 초록색 박스가 Global Python, 그리고 아래에 MTV라고 그려진 파란색 상자가 프로젝트이다.

Django 패키지를 임포트한다고 가정하자. 

일반적으로 파이썬을 사용할 경우 터미널에 python 명령을 사용하면 Global Python을 참조하게된다. 여기서 python 패키지 import 시, 당연히 패키지 또한 Global Python의 패키지를 참조하게 된다.

이때, **나는 Global Python에서 일일히 패키지를 가져오기보다는 MTV 프로젝트에서 독립된 파이썬 공간을 만들어서 패키지를 직접 넣어놓고 쓰고싶어!**라는 생각이 들게 되는데, 바로 이럴때 가상환경을 사용하는 것이다.

MTV프로젝트의 venv/라는 독립된 파이썬 가상환경을 만들어서 나한테 꼭 필요한 패키지만을 사용할 수 있게 된다.

이 가상환경은 패키지의 버전을 여러개 사용하고 싶을 경우에 특히 강점을 발휘하게 된다.

### venv 명령어
#### 가상환경 생성
독립된 파이썬 가상환경을 생성하는 명령이다. python -m venv까지는 고정 명령어고 그 뒤에 나오는 venv는 가상환경의 이름이다.
보통 가상환경의 이름은 venv로 통일하는 것이 좋다.

**사용법**
```
$ python -m venv venv
```

#### 가상환경 참조방향 변경
python의 참조 방향을 변경하는 명령이다.

source는 Global에서 venv로 참조하며, 이때 사용되는 파일은 venv/Scripts/activate 파일이다.

deactivate는 venv에서 Global로 다시 변경한다.
```
$ source venv/Scripts/activate

$ deactivate
```

### .gitignore 추가
하단의 01-09 수업내용 참조.


## 2023-01-09 수업내용
```t
$ mkdir MTV
$ cd MTV
$ python -m venv venv  # 독립 환경 생성
$ touch .gitignore  # => https://gitignore.io 에서 "python" "django" "venv" 입력하고 내용 복붙
$ touch README.md

# Windows venv 활성화
$ source venv/Scripts/activate
# Mac venv 활성화
$ source venv/bin/activate

(venv)  # 확인
$ pip install django==3.2.16
(venv)
$ django-admin startproject mtv .
(venv)
$ code . (vscode 로 열기)

# 만약 추가 설치한 패키지들이 있다면
$ pip freeze > requirements.txt
```
