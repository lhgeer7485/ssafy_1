# Markdown 기본

- 확장자는 .md

- 해더는 # text

- -, *, + text

- 숫자는 똑같이 1. 2. 3. ...

- 강조는 ******(text)**

- 코드를 깔끔하게 올릴때는 ``````코드``````

- 취소선은 물결 2개

- 이텔릭은 *

- 이미지는 ![로고] (이미지경로)

- 링크는 [이름] (url)



# GUI(Graphic User Interface)

- 그래픽을 이용하여 사용자와 컴퓨터가 상호작용
  
  

# CLI(Command Line Interface)

- 명령어를 이용하여 사용자와 컴퓨터가 상호작용

- .  현재 디렉토리

- .. 상위 디렉토리

- touch 파일 생성

- mkdir 디렉토리 생성

- ls 현재 디렉토리 파일 목록

- cd 현재 디렉토리 이동

- start 폴더/파일 열기

- rm 파일 삭제

- rm -r 디렉토리 삭제





---



# Git 명령어를 알아보자

### 기본명령어

- git init : 저장소 생성

- git add : 수정 또는 작업된 파일 stage area에 추가

- git config --globaluser.email "메일주소"

- git config --global user.name "유저네임"

- git commit -m "메시지" : 커밋

- git log [--graph] : 커밋 로그 확인

- git status : git 상태 확인

- git branch : 브랜치 확인

- git branch {브랜치이름} : 브랜치 생성

- git switch {브랜치이름} : 브랜치 이동

- git branch [-d | -D] {브랜치이름} : 브랜치 삭제

- git merge {브랜치이름} : 브랜치 병합

### 원격 저장소(remote repository) 관련 명령어

- git clone : 원격 저장소 로컬에 복사

- git push {원격저장소 이름} {브랜치이름} : 원격 저장소에 업로드

- git pull {원격저장소 이름} {브랜치이름} : 원격 저장소 다운로드

- git remote add {원격저장소이름} {원격저장소주소} : 로컬저장소에 원격저장소 추가하기 (단, 원격저장소가 비어있어야함, commit X, 파일 X)

### git 사용 시나리오

#### 집-강의장 에서 소스코드 공유하기

1. 원격저장소 생성(gitlab, github)

2. 강의장(또는 집)에서 원격저장소 복제(clone)

3. 강의장(또는 집)에서 작업 후, commit

4. 원격저장소에 push

5. 집(또는 강의장)에서 pull (만약 저장소가 없다면 clone)

#### 충돌시 대처방안

1. 대체로 로컬에서 commit 후, pull, 수동 merge 하면 대부분 해결됨

2. 그냥 pull만 받고 싶은데 안된다. 삭제후 clone이 가장 간편함
