# Django
## URL
클라이언트가 서버에 요청을 보내는 주소.

클라이언트가 서버에 어떤 요청을 보내고 싶을때, 방법은 URL 쓰는 것 말고는 없다.

## Django
### MTV 패턴
- Model     : DB에 저장되는 데이터를 의미.
- Template  : 유저에게 보여지는 화면을 의미. (HTML 파일)
- View      : 요청에 따라 적절한 로직을 수행. (def 함수(request))

보통 다른 언어에서는 MVC패턴이라고 하나, 파이썬은 힙스터기질이 심한 사람들이 많아서
MTV패턴을 사용.

이를 아래처럼 표로 정리할 수 있음.

|MTV패턴|MVC패턴|설명|
|-|-|-|
|Model|Model|DB에 저장되는 데이터|
|Template|View|유저에게 보여지는 화면(HTML)|
|View|Controller|요청에 따른 로직을 수행.|

### Django 실습 전 명령어

```
$ django-admin startproject test    # project 시작
$ python manage.py                  # manage.py로 실행 가능한 명령 확인
$ python manage.py startapp         # app 시작 (settings.py 등록 필요)
```

### 데이터 입력 그림
![image](./web_data_input.png)
서버를 건물에 비유하자면 위와 같다.

Project라 써져 있는 큰 건물이 Django에서 `django-admin startproject 플젝이름`으로 생성하는 그 project 맞다.

건물안에 각각의 urls.py로 가지는 각각의 부서들은 `python manage.py startapp 앱이름`으로 생성하는 그 app이다.

설명
1. 위 건물에서 저 수문장1이라고 적혀있는 urls.py가 최초로 url을 받는다. 
2. url에 포함된 앱 종류에 따라 각각의 앱 urls.py로 보낸다.
3. 각 앱의 urls.py에서는 view.py에 정의된 각종 함수들(로직)에 따라 HTML파일을 내보낸다.
4. view.py에는 urls.py에서 호출된 메소드에 따라 template에 정의된 HTML파일을 내보내는 로직을 기술한다.


#### 각 파일 별 코드 예시
```python
# 수문장1 (Project의 urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')), # review로 url이 오면 review.urls.py로 전송
    path('data/', include('data.urls')),    # data로 url이 오면 data.urls.py로 전송
]
```
```python
# 각 앱의 urls.py
# URL 구성 맨 앞에 'review/'는 이미 master url에서 검사가 끝남.
urlpatterns = [
    # 패턴 '(review/)index/'가 요청으로 들어온다면, 
    path('index/', index, name='index'),
    path('hello/', hello, name='hello'),
]
```
```python
# views.py
from django.shortcuts import render

# Create your views here.
# URL이 review/index로 오면 review/hello_world.html을 반환
def index(request):
    return render(request, 'review/hello_world.html')


# URL이 review/hello로 오면 review/hello.html을 반환
def hello(request):
    return render(request, 'review/hello.html')

```

### Django 실습 과정
#### 실습 전 사전 준비
먼저 프로젝트를 생성한다.

```
$ django-admin startproject test
```
당연히 test는 프로젝트 이름이니까 아무렇게나 정해도 된다.

위처럼 프로젝트를 처음 생성하면 `test` 폴더랑 `manage.py` 파일 두개만 덩그러니 생성된다.

이제부터 모든 Django 프롬프트 명령어는 `manage.py`로 소통한다.

그 다음엔 `master_templates` 폴더를 만든다. 이 폴더는 HTML파일을 돌려쓰기 위한?(재사용을 위한) 폴더이다.

`master_templates` 폴더를 생성하고 나면, `settings.py`의 `Templates`의 `DIR` 항목에 해당 폴더의 경로에 적어 넣어야 한다.

```
$ cd ~/test
$ mkdir master_templates
```
```python
# BASE_DIR은 생성한 프로젝트의 기본 위치이다.
# 예를 들어, review 프로젝트를 생성했다면 BASE_DIR은 review 디렉토리의 위치를 말한다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # django는 기본적으로 app안에 templates/폴더에서 HTML을 찾음.
        'DIRS': [BASE_DIR / 'master_templates'],     # django가 추가로 HTML을 찾아볼 폴더 등록.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

그리고 각 부서(앱)들을 만든다. 앱을 만들고나서는 프로젝트 시작과 동시에 생성된 `settings.py`의 `INSTALLED_APPS`에 해당 앱을 추가해야 한다.

그리고 HTML파일들을 모아놓을 `templates` 폴더도 추가하면 금상첨화.
```
$ python manage.py startapp review
$ cd review
$ mkdir templates
```
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'review',                       # 이렇게 추가.
]
```
app들은 새로 생성될때마다 `INSTALLED_APPS`에 추가해야 한다.

여기까지 했다면 사전준비는 끝난다.

### 실습 시작
Django의 각 주요 파일들(urls.py, views.py, templates 등)은 서로 유기적으로 연결되어 있으며, 이 연결들은 장고가 뒤에서 열심히 해주고 있다. 각 파일들의 역할을 알아보자.

### urls.py
실습의 처음은 먼저 수문장1에 해당되는 프로젝트 디렉토리의 urls.py로 각 url에 따라 분배하는 것이다.

예를 들어, https://~뭐시기~/review/index 로 온 것은 review.urls.py로 보내서 나머지 index를 처리하게 하고,

https://~뭐시기~/data/hello 로 온 것은 data.urls.py로 보낸 다음, 나머지 hello를 처리하게끔 구성해야 한다.

이를 코드로 나타내면 아래와 같다.

```python
# TEMPLATE_VIEW Project의 urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('data/', include('data.urls')),
]

# review 앱의 urls.py
from django.urls import path
from data.views import *

# 변수명 반드시 app_name
app_name = 'review'

# URL 구성 맨 앞에 'review/'는 이미 master url에서 검사가 끝남.
urlpatterns = [
    # 패턴 '(review/)index/'가 요청으로 들어온다면, 
    path('index/', index, name='index'),
    path('hello/', hello, name='hello'),
    path('user_input', user_input, name='user_input`')
]

# data 앱의 urls.py
from django.urls import path
from data.views import *

app_name = 'data'

urlpatterns = [
    path('index/', index, name='index'),

    # data/hello/<name>/ => Variable Routing
    path('hello/<str:name>/', hello, name='hello'),
    # hello/neo => 안녕 neo,
    # hello/andy => 안녕 andy,

    path('user_input/', user_input, name='user_input'),
    path('user_output/', user_output, name='user_output'),
]
```
뭔가 잔뜩 있어서 보기 힘들지만, 아래의 표를 보면 이해에 도움이 된다.

|메소드|파라미터|설명|
|-|-|-|
|path|str <br> method_object <br> name(*optional)|str: 처리를 보낼 앱의 종류를 뜻한다. <br> method_object: 파라미터 str에 따라 처리를 달리할 메소드를 뜻한다. <br> name: URL에 짓는 이름이다. 이걸 하면 템플릿을 포함한 Django 어디에서나 명확하게 참조가 가능하다.
|include|str|str에 해당되는 앱의 urls.py에 URL을 보낸다. 보통 path()와 같이 쓰인다.|

정리하면, 요청이 들어온 url을 프로젝트 디렉토리의 **urls.py을 통해 각 앱의 urls.py로 보내고**,
각 앱의 urls.py에 정의된 path 메소드에 따라 path 메소드의 인자값에 대응되는 **메소드를 호출하여 HTML파일을 반환**한다고 보면 된다.

### views.py
처리의 핵심이다. urls.py가 각 url을 로직에 맞게 이동시키는 **도로** 정도의 역할을 한다면, views.py는 url 요청이 들어왔을때, 구체적으로 어떤 로직에 따라 수행할지를 결정한다.

```python
# data.urls.py
from data.views import *

path('index/', index, name='index'),
path('hello/<str:name>/', hello, name='hello'),


# data.views.py
def index(request):
    return render(request, 'data/index.html')

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'data/hello.html', context)
```

위 코드를 보자.

data.urls.py 부분을 보면 URL 요청이 index/로 들어오면 index 메소드를 실행한다고 되어 있다. 여기서 index 메소드가 views.py에 기술되어 있다.

또다른 예를 보자, URL 요청이 `hello/사용자 입력값`의 형태로 들어오면 hello 메소드를 실행한다고 되어 있다. hello 메소드 또한 views.py 파일에 기술되어 있는 것을 확인할 수 있다.

views.py의 메소드 부분을 정리하면 아래와 같다.

|메소드|설명|
|-|-|
|render|HTML파일을 렌더링한다. 즉, HTML파일을 클라이언트에게 반환한다.|
|HttpResponse|문자 그대로 HTTP프로토콜로 응답을 보낸다. <br> HttpResponse(data, content_type)의 형태로 사용한다. (잘 사용안함)|

### Templates
HTML파일을 모아놓은 문서이다.

`python manage.py startapp 앱이름` 명령으로 처음 앱을 생성하면 곧바로 `mkdir templates`로 템플릿 폴더를 생성한다고 위에서 언급했는데, 그게 이거다.

views.py에서 render() 메소드로 HTML파일을 응답할때, **장고는 가장 먼저 해당 앱의 templates 폴더를 참조한다.**

#### master_templates
HTML파일에서 반복되는 부분을 재사용하기 위해 미리 기술해놓은 HTML파일을 모아놓은 폴더이다.

프로젝트 생성 시 가장 먼저 생성하는 템플릿 폴더 중 하나이다.

아래 코드를 통해 바로 알 수 있다.
```HTML
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% block content %}

    {% endblock content %}
</body>
</html>


<!-- hello.html -->
{% include 'base.html' %}

{% block content %}

    <h1>안녕, {{ name }}</h1>

{% endblock content %}
```

body 부분의 {% block content %} ~ {% endblock content %} 사이에 각 HTML파일 별 내용이 들어가는 것을 알 수 있다.

이런식으로 반복을 줄여서 코드의 재사용성을 높일 수 있다.



## 23-01-05 강의 핵심 요약
1. 어제와 동일한 URL => View => Template
2. 앞으로 urls.py 에서 app_name = 'APP_NAME' 과 path('', views.func, name='PATTERN_NAME') 설정하기
3. 템플릿에서 {% url 'APP_NAME:PATTERN_NAME' %} 으로 링크 생성 가능
4. App 마다 html 파일 이름이 겹칠경우 django에서 제대로 인식하지 못함
5. app/ > templates/ > app/ > html 파일들 방식으로 구분
6. 사용자 입력을 받아보자

그 외 정리
- POST 방식으로 데이터 전송 시 csrf 토큰을 반드시 사용해야함. (안하면 브라우저에서 차단, 자세한 건 하단 코드 참조.)
- 사용자에게 입력받은 값은 아래처럼 전송 (request는 메소드 생성시 필수적으로 생성하는 매개변수)
  
```HTML
<form action="{% url 'data:user_output' %}" method='POST'>
    {% csrf_token %}
    <input type="text" name='username'>
    <input type="password" name='password'>
```
```python
context = {
        'f': f,
        'username' : request.POST['username'],
        'password' : request.POST['password'],
    }
```
