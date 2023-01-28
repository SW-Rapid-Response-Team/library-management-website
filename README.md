# 1. 가상환경 세팅과 실행 방법
1.1 가상환경 다운 받기  
```
sh make_venv.sh
```
1.2 가상환경 실행하기
```
source website_virtual_env/bin/activate
```
실행 후에는 directory 앞에 (website_virtual_env)이 나오는 것이 정상.  

1.3 가상환경 끄기
```
deactivate
```

# 2. GCP를 통해 웹사이트를 실행 하는 법
2.0 게이트웨이 세팅에서 80 or 8080 or 8000 포트를 연다.  
2.1 가상환경을 실행한다.  
2.2 allowed host를 설정한다.  
library-management-website/main/config/settings.py 경로에서,  
![gcp_example](/readme_img/gcp_example.png)  
위 그림에서 나온 외부 ip와 포트를 적는다.  

<br>
예시) 내부 ip를 10.178.0.9, 외부 ip를 34.64.146.1라고 하자.  

```ALLOWED_HOSTS = ['34.64.146.1','8080']```
와 같이 setting 한다.  

2.3 django를 실행한다.  
```
python manage.py runserver 10.178.0.9:8080
```
2.4 브라우저에서 django에 접속한다.  
http://34.64.146.1:8080 접속.  
