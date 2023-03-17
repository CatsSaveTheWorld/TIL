# markdown 기초 문법

## 기초

### 개행
- 두 줄을 띄운다.
- 마지막에 공백 두개(  )를 넣는다.
- `<br>`을 넣을때마다 개행된다. (권장하지 않음)

// 추가요망

## 리스트

### 순서가 있는 리스트 (ordered list)
1. 손 씻기
  1. 물을 틀기                       # 탭(Tab) 누르면 들여쓰기, Shift + Tab 하면 역들여쓰기
  2. 비누칠하기
  3. 닦아내기
2. 식당에 가기
3. 밥을 먹기
4. 계산하기
5. 양치하기

### 순서가 없는 리스트 (unordered list)
- 짜장면
  - 간짜장                          # 탭(Tab) 누르면 들여쓰기,
- 돈까스                            # Shift + Tab 하면 역들여쓰기
- 김밥
- 라면
  1. 물을 넣기
  2. 끓이기
  3. 건더기 스프
  4. 앙념 스프
  5. 면
  6. 식사

### 인라인 강조
중요한 것은 **굵게 표시하고 (Ctrl + B)**, 주의할 것은 *기울이고 (Ctrl + I)*, 코드 혹은 명령어는 `따로 강조 (백틱 `` 문자)`를 하고 싶다.

#### 정리
- 굵게 할때 : Ctrl + B / * 두 개로 감싸기 (**문자**)
- 기울일 때 : Ctrl + I / * 한 개로 감싸기 (*문자*)
- 따로 강조 : 백틱 문자 (``)로 감싸기      (`문자`)
- 취소선 : 물결로(~) 감싸기              (~~문자~~)

## 블럭 강조


### 표
파이프 (|)로 구분하여 테이블 헤더를 생성

| 명령어      | 설명                                           | 예시                                                             |
| ----------- | ---------------------------------------------- | ---------------------------------------------------------------- |
| `mkdir`     | 디렉토리 생성                                  | $ mkdir test1                                                    |
| `touch`     | 파일 생성                                      | $ touch test1.txt                                                |
| `rm`        | 파일이나 디렉토리 삭제                         | $ rm test1.txt <br> $ rm -rf test1                               | # <br> 으로 개행      |
| `pwd`       | 현재 디렉토리 위치 출력                        | $ pwd                                                            |
| `ls`        | 현재 디렉토리의 파일 출력                      | $ ls -ltr <br> $ ls -a <br> $ ll                                 |
| `ps`        | 현재 실행중인 프로세스 출력                    | $ ps                                                             |
| `cd`        | 디렉토리 이동                                  | $ cd /root/home <br> $ cd / <br> $ cd ~ <br> $ cd -              |
| `find`      | 파일이나 디렉토리 위치를 탐색                  | $ find -name test1.txt                                           |
| `chmod`     | 파일이나 디렉토리의 읽기/쓰기/실행 권한을 변경 | $ chmod 755 test1.txt                                            |
| `chown`     | 파일이나 디렉토리의 소유권을 변경              | $ chown aaa:bbb test1.txt                                        |
| `cat`       | 파일의 내용을 출력                             | $ cat test1.txt <br> $ cat -n test1.txt                          |
| `yum`       | 패키지 설치/제거 도구                          | $ sudo yum install mysql-server -y                               |
| `systemctl` | 서비스 제어                                    | $ systemctl [start, stop, enable, disable, status, reload] httpd | # 대괄호 단어 중 택 1 |
| `clear`     | 터미널 비우기                                  | $ clear                                                          |
| `ipconfig`  | 네트워크 정보 표시                             | $ ipconfig <br> $ ipconfig -all                                  |


### 코드
백틱(`) 세 개로 감싼다. 이때, 백틱 3개 옆에 언어명을 입력하면 각 언어의 특색에 맞는 색칠을 해준다.

```
$ mkdir mydir

$ cd mydir

$ touch a.txt

$ rm a.txt

```

```python
# python

import os


def rename_file(file_name):
    return file_name.replace('webp', 'jpg')         # 여기에 수정할 파일이름 작성


file_path = 'C:\\Users\\4ser\\Pictures\\Feedback'
file_names = os.listdir(file_path)

new_file_names = list(map(rename_file, file_names))

for old_name, new_name in zip(file_names, new_file_names):
    src = os.path.join(file_path, old_name)
    dst = os.path.join(file_path, new_name)
    os.rename(src, dst)
```

```javascript
// js
function my_func(x, y) {
  return x + y;
}
```

## 기타


### 인용
> 일단 똥을 싸라. 그리고 박수칠때까지 닦아라. -No man's sky

<br>

### 수식
- 인라인 수식 $x + y$
- 블럭 수식
​
$$
\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}
$$
​
### 이미지 / 하이퍼링크
```
link
[표시 텍스트](링크) 
​
image
![대체 텍스트](링크)
```
​
[구글](https://google.com)
​
![img](https://cdn.travie.com/news/photo/first/201710/img_19975_1.jpg)


