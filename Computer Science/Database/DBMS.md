# DBMS
Database management system = 데이터베이스 관리 시스템
다수의 사용자가 데이터베이스 내의 데이터를 접근할 수 있도록 설계된 소프트웨어

### DBMS의 기능
- 정의 기능 (DDL: Data Definition Language)
  데이터 베이스의 용도와 이용 방법에 맞춰 구조를 정의하고 생성하는 것
  CREATE, ALTER, DROP, RENAME

- 조작 기능 (DML: Data Manipulation Language)
  데이터베이스를 만들었을 때, 그 안에 정보를 수정, 추가, 삭제 등의 조작을 하는 것
  SELECT, INSERT, UPDATE, DELETE

- 제어 기능 (DCL: Data Control Language)
  데이터베이스에 접근하고 객체들을 사용할 수 있는 권한을 주고 회수하는 명령어
  GRANT, REVOKE


### DBMS의 종류
데이터베이스를 사용하기 위해서 DBMS 소프트웨어를 설치해야하며, 대표적으로 MySQL, 오라클(Oracle), SQL 서버, MariaDB 등이 있다.
각각의 특징을 살펴보자.

DBMS 	   |    제작사	    |          작동운영체제	             |     기타
MySQL	   |   Oracle     |    Unix, Linux, Windows, Mac	|  오픈 소스(무료), 상용
MariaDB	   |   MariaDB	  |    Unix, Linux, Windows	        |  오픈 소스(무료), MySQL 초기 개발자들이 독립해서 만듦
PostgreSQL |  PostgreSQL  |    Unix, Linux, Windows, Mac	|  오픈 소스(무료)
Oracle	   |    Oracle	  |    Unix, Linux, Windows	        |  상용 시장 점유율 1위
SQL Server |  Microsoft	  |    Windows	                    |  주로 중/대형급 시장에서 사용
DB2	       |     IBM	  |    Unix, Linux, Windows         |  메인프레임 시장 점유율 1위
Access     |  Microsoft   |    Windows	                    |  PC용
SQLite	   |    SQLite	  |    Android, iOS	                |  모바일 전용, 오픈 소스(무료


### DBMS 분류
DBMS의 유형은 계층형(Hierarchical), 망형(Network), 관계형(Relational), 객체지향형(Object-Oriented), 객체관계형(Object-Relational) 등으로 분류된다. 현재 사용되는 DBMS 중에는 관계형 DBMS가 가장 많은 부분을 차지하며, MySQL도 관계형 DBMS에 해당한다.

- 계층형 DBMS: 계층형 DBMS(Hierarchical DBMS)는 처음으로 등장한 DBMS 개념으로 계층이 트리(tree) 형태를 갖는다. 계층형 DBMS는 처음 구성을 완료한 후에 이를 변경하기가 상당히 까다롭다는 문제가 있다. 또한 다른 구성원을 찾아가는 것이 비효율적이어서 현재는 사용하지 않는 형태이다. 
- 망형 DBMS: 망형 DBMS(Network DBMS)는 계층형 DBMS의 문제점을 개선하기 위해 등장한 방식으로 하위에 있는 구성원끼리도 연결된 유연한 구조이다. 이 형태를 잘 활용하려면 프로그래머가 모든 구조를 이해해야 한다는 한계가 있어 지금은 거의 사용하지 않는 형태이다.
- 관계형 DBMS: 관계형 DBMS(Relational DBMS)는 줄여서 RDBMS라고 부르며 MySQL뿐만 아니라, 대부분의 DBMS가 RDBMS 형태로 사용된다. RDBMS의 데이터베이스는 테이블(table)이라는 최소 단위로 구성되며, 이 테이블은 하나 이상의 열(column)과 행(row)으로 이루어져 있다.

### SQL: DBMS의 언어
SQL(Structured Query Language)은 관계형 데이터베이스에서 사용되는 언어다. 국제표준화기구에서 SQL에 대한 표준을 정해서 발표하기 때문에 DBMS를 만드는 회사에서는 되도록 표준 SQL을 준수하되, 각 제품의 특성을 반영한 SQL을 사용한다.
