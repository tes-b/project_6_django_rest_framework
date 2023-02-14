# whdf_cp2

[페이지 링크](http://3.38.47.74/)
[API 설명](http://3.38.47.74/swagger)

##프로젝트 
-------------
DRF를 사용하여 REST API를 만들고 배포

##API 주요 기능
-------------
* 회원가입, 회원목록, API접근을 위한 jwt발급 등 회원정보 처리
* 질문글과 답변글 CRUD 기능(Create, Read, Update, Delete)
* 회원들의 활동에 대한 통계 Dashboard
* 회원들의 활동에 대한 Log 기능구현

##그 외
-------------
* username과 password를 입력해 jwt 발급
* API에 대한 권한 설정
* 질문글 수정은 본인만 가능, 삭제는 본인과 staff만 가능
* App을 내부적으로 테스트하는 기능
* 커스터마이징 웹 제작

##사용방법
-------------
* 레포지토리 클론
  $ git clone https://github.com/tes-b/whdf_cp2.git
* DB생성
  mysql> create database <db name> ;
* .env 파일 DB정보 설정
  '''.env파일을 이용하여 환경변수 설정한다'''
  DB_NAME='DB이름'
  DB_USER='유저아이디'        
  DB_PASSWORD='비밀번호'
* 패키지 설치
  '''conda 이용하여 가상환경 생성 후 패키지 설치'''
  conda create --name [이름] python=3.9.16
  conda env create --file conda_requirements.yaml
