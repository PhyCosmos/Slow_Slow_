# Slow_Slow_
파이보 게시판 제작 프로젝트 연습

## git bash 명령어 모음
- `git status` : add to commit할(스테이지 영역에 있는) 파일, untracked 파일 등 현재 git 저장소의 상태를 보여줌
- `git add <파일명>` 또는 `git add *` : 파일을 스테이지 영역에 올려 commit할 준비를 한다.
- `git commit -m "메시지"` : 스테이지에 올려진 파일들을 커밋(저장소에 보관)한다. 이때 메시지를 입력하여 어떤 이유로 커밋하는지 정보를 남길 수 있다.
- `set LC_ALL=C.UTF-8` : 혹시라도 있을 한글 깨짐 방지
- `git commit -a -m "메시지"` : add와 commit을 한꺼번에 실행한다.
- `git diff` : 변경 내용을 출력한다.
- `git log` : 커밋 이력을 출력한다.
- `git restore <파일명>` :  `git status`로 보여지는 파일 중에서 <파일명>을 원래상태로 복원 시킨다.
- `git remote add origin https://github.com/pahkey/pybo.git` : https://github.com/pahkey/pybo.git 이라는 원격저장소를 연결한다.
- `git push -u origin master` : master브랜치로 푸시한다.(원격저장소로 upstream/옮겨저장시킨다.)
- `git pull` : 원격저장소로부터 변경사항을 가져온다.
