# DjangoProject
First DjangoProject
나만의 앱 만들기

<br>

# [ 장고 프로젝트앱 생성 후 template, db구현 순서 ]
#### 1. terminal에서 python manage.py startapp 앱이름
#### 2. 메인의 settings.py에 INSTALLED_APPS에 '앱이름' 추가
#### 3. 메인의 urls.py에 urlpatterns에 path('원하는 경로/', include('앱이름.urls')), 추가
#### 4. 생성 앱에 templates-앱이름으로 폴더 생성 html 저장
#### 5. 생성 앱에 models.py에 내가 db에서 사용할 컬럼들 생성
#### 6. 생성 앱에 forms.py를 생성 후에 class로 내가 만들 db의 모델과 사용할 컬럼들 fields에 추가
#### 7. migration 작업 : terminal에 python manage.py makemigrations 후에 python manage.py migrate하면 db에 반영됨.
#### 8. 생성 앱에 views.py에 class로 CRUD view 생성
#### 9. 생성 앱에 urls.py 생성 후에 app_name 반드시 지정(다른 곳에서 불러올 때 사용)
#### 10. 생성 앱에 urls.py에 urlpatterns에는 내가 views에서 생성한 class를 기반한 view 연동(라우팅)

<br>

# [ 만들면서 생겼던 에러들 ]
### 1) namespace 관련 에러 발생
#### sol) 연동된 urls에 app_name 설정을 확인하고 설정이 안되어있으면 추가한다.

<br>

### 2) makemigrations 관련 에러 발생
#### ![에러2](https://user-images.githubusercontent.com/78336335/146772335-713231b6-0a36-49e7-8f7d-9454c8019f45.png)
#### sol) django의 mainapp에서의 urls 설정 확인 후 수정.

<br>
