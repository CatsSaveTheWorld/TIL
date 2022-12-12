# git
## 기초
---
Git의 Repository 구조는 크게 세가지로 구성되어있다.
```
작업폴더(Working directory) > 인덱스(Staging Area) > 저장소(Head -Repository) 
```
우리가 작업하는 폴더를 `작업트리(Working directory)` 라고 부르며 commit을 실행하기 전에 작업트리와 저장소 사이에 존재하는 가상의 준비 영역(Staging Area)을 `인덱스(Index)`라고 한다.

저장소에 commit하기 위해서 먼저 추가(Untracked files) 및 변경(Modified files) 하고자 하는 파일을 먼저 `인덱스에 기록(Stage)`하고 이후 스테이징된 목록만 최종적으로 commit 명령어에 의해 저장소에 공개하게 됩니다.

#### 쉬운 설명
영화 촬영에 비교하여 설명한다.

영화를 촬영하려면 3가지 공간이 필요하다.

1. 분장실 (작업공간, working directory)
2. 스테이지 (stage)
3. 커밋들 (commits)

이때, 1 → 2에서 가는 명령이 add이고, 2 → 3으로 가는 명령이 commit이다.


## git 사용 전 설정
---
### 이름 설정
1. 이름을 설정한다.
   ```
   $ git config --global user.name "name"
   ```
2. 이메일 주소를 설정한다. (G메일 권장)
   ```
   $ git config --global user.email "email@gmail.com"
   ```


## init
---
### 정의
현재 디렉토리를 로컬 저장소로 만든다. 이걸 Initialize시켜야 본격적으로 git을 사용할 수 있다.

### 사용법
```
$ git init
```


## 로컬저장소 해제
---
### 정의
.git 디렉토리를 삭제하면 해당 디렉토리의 로컬저장소가 해제된다.

### 사용법
```
$ rm -rf .git
```


## status
---
## 정의
현재 git의 상태를 나타낸다.

### 사용법
```
$ git status
```


## add
---
### 정의
특정 파일을 stage에 올린다.

### 사용법
```
$ git add a.txt
```


## commit
---
### 정의
스테이징된 파일을 최종 확정한다.

### 사용법
```
$ git commit a.txt -m '변경내용'
```


## reset
---
### 정의
스테이징된 파일을 되돌린다. 

### 옵션
- reset 옵션
  - -soft : index 보존(add한 상태, staged 상태), 워킹 디렉터리의 파일 보존. 즉 모두 보존.
  - -mixed : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 보존 (기본 옵션)
  - -hard : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 삭제. 즉 모두 취소.

### 사용법
```
# git reset a.txt
```


## restore
---
### 정의
특정 커밋으로 되돌리거나 unstaging한다.

### 사용법
```
$ git restore a.txt
```

## 에러
---
### fatal: bad object HEAD

해결법
1. .git 디렉토리를 삭제하고 init을 다시 설정한다.
2. VScode를 재시작하여 소스 제어에 아무것도 출력되지 않는 현상을 해결한다.


### ※ init 사용 시 하단의 CRLF 에러 발생 시
```
warning: in the working copy of 'a.txt', LF will be replaced by CRLF the next time Git touches it
```

**CR(Carriage-Return)**  
현재 커서를 줄 올림 없이 가장 앞으로 옮기는 동작  

**LF(Line-Feed)**  
커서는 그 자리에 그대로 둔 상황에서 종이만 한 줄 올려 줄을 바꾸는 동작

**CRLF (Carriage-Return+Line-Feed)**  
한마디로 줄 바꿈

OS마다 줄 바꿈에 대한 문자열이 다르기 때문에 git에서 어느 쪽을 선택해야 할지 경고 메시지를 띄워 준 것이다.
</br></br>

**해결법**

위 에러는 git init시 줄바꿈과 관련된 에러이다. 아래 명령을 쓰면 해결된다.

```
$ git config --global core.autocrlf true
```




### 참고
https://app.slack.com/client/T04DPM0NUKU/C04FEDADPU0 # 04_실시간코드
```
$ git init  # 이걸 해야 (master)가 나옴!
$ git commit # => 안내문 나옴
$ git config --global user.email "개발에쓸@이메일"
$ git config --global user.name "내이름"
```