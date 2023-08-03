# MLOps for MLE
## 01. Database
Docker를 이용해서 DB server를 생성하고 psycopg2 패키지를 사용해 테이블을 생성하고 데이터 삽입을 해볼 것이다.
또한 Docker 파일과 Compose 파일을 만들어 Docker 컨테이너 안에서 계속 데이터를 생성하는 서비스를 구축해볼 것이다.

### Docker의 기능
- Build and run an image as a container.
- Share images using Docker Hub.
- Deploy Docker applications using multiple containers with a database.
- Run applications using Docker Compose.

### what is a container?
A container is a sandboxed process running on a host machine that is isolated from all other processes running on that host machine.
- Is a runnable instance of an image. We can create, start, stop, move, or delete a container using the DockerAPI or CLI.
- Can be run on local machines, virtual machines, or deployed to the cloud.
- Is portable (and can be run on any OS).
- Is isolated from other containers and runs its own software, binaries, configurations, etc.

### what is a container image?
A running container uses an isolated filesystem. This isolated filesystem is provided by a container image, and the container image must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc. The image also contains other configurations for the container, such as environment variables, a default command to run, and other metadata.

# 실습 - 1
## DB Server Creation

[설치링크](https://www.docker.com/)   
위 링크에서 Mac - Intel Chip 버전을 설치하였음.   

docker run 명령어를 통해 옵션을 설정하여 DB 서버를 생성할 수 있다.   
-d : 컨테이너가 detached 모드로 실행하게 되며, -d 옵션 없이 실행했다면 해당 터미널에서 Ctrl + C 를 눌러서 빠져나오는 순간 해당 컨테이너는 종료된다.   
--name : 컨테이너의 이름을 지정   
-p : 컨테이너에서 외부로 노출할 포트 포워딩 (port forwarding) 을 설정한다. 형식은 host:container 으로 사용되며, 여기서는 5432:5432 로 설정하겠다.   
-e : 필요한 환경 변수를 설정한다.   
POSTGRES_USER : 유저의 이름을 설정한다.   
POSTGRES_PASSWORD : 유저의 비밀번호를 설정한다.   
POSTGRES_DB : DB 의 이름을 설정한다.   
postgres:14.0 : 사용할 이미지를 지정한다.   

```python
docker run -d \
> --name postgres-server \
> -p 5432:5432 \
> -e POSTGRES_USER=heejin \
> -e POSTGRES_PASSWORD=password \
> -e POSTGRES_DB=mydatabase \
> postgres:14.0
```

이렇게 서버가 생성되고 나면 docker ps 명령어를 통해 확인할 수 있다.   
```
CONTAINER ID   IMAGE           COMMAND                   CREATED          STATUS          PORTS                    NAMES
363e70063ae3   postgres:14.0   "docker-entrypoint.s…"   20 seconds ago   Up 16 seconds   0.0.0.0:5432->5432/tcp   postgres-server
```

### DB 서버 확인
PostgreSQL DB 서버를 확인할 때 사용하는 CLI 툴인 psql을 설치한다.   

[설치 링크](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)   


PostgreSQL Version - 15.3 / Mac OS X 로 설치하였다. 그 다음 아래 커맨드로 psql을 통해 postgreSQL DB 서버로 접속한다.   
```python
PGPASSWORD=password psql -h localhost -p 5432 -U heejin -d mydatabase
```
아래와 같은 출력을 확인할 수 있다.   
```
psql (14.8 (Homebrew), server 14.0 (Debian 14.0-1.pgdg110+1))
Type "help" for help.

mydatabase=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 heejin    | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

mydatabase=# 
```
