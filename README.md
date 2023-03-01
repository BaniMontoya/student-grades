
# student-grades

"Student-grades" is a Django-based web app for managing student grades.

How to test: 
1.-clone this repository:  [https://github.com/BaniMontoya/student-grades.git](https://github.com/BaniMontoya/student-grades.git)

2.-create venv on root of project 
python -m venv venv
 .\venv\Scripts\activate 
 pip install -r requirements.txt

2.-create database 
cd grades 
python manage.py migrate 
python manage.py makemigrations api
 python manage.py migrate api

3.-tests 
python .\manage.py test

4.-create super user 
python .\manage.py createsuperuser 
choices 
username: super 
email:  [super@super.com](mailto:super@super.com)  
password: 1234 
confirm: 1234 
y

5.-run django project 
python .\manage.py runserver

6.-access admin panel  [http://127.0.0.1:8000/admin/login/?next=/admin/](http://127.0.0.1:8000/admin/login/?next=/admin/)  

7.-login with your super user 

8.-create test:  [http://127.0.0.1:8000/admin/api/test/add/](http://127.0.0.1:8000/admin/api/test/add/)  

9.-create question:  [http://127.0.0.1:8000/admin/api/question/add/](http://127.0.0.1:8000/admin/api/question/add/)  and select a test 

10.-create user:  [http://127.0.0.1:8000/admin/auth/user/add/](http://127.0.0.1:8000/admin/auth/user/add/)  add is_staff option and select group student and save 

11.-create student:  [http://127.0.0.1:8000/admin/api/student/add/](http://127.0.0.1:8000/admin/api/student/add/)  and select user of student 
12.-give access to student group:  [http://127.0.0.1:8000/admin/auth/group/1/change/](http://127.0.0.1:8000/admin/auth/group/1/change/)  select "student asnwer view permission" 

13.-create student answer:  [http://127.0.0.1:8000/admin/api/studentanswer/add/](http://127.0.0.1:8000/admin/api/studentanswer/add/)  

14.-logout 

15.-login with your student user 

16.-check your answer:  [http://127.0.0.1:8000/admin/api/studentanswer/](http://127.0.0.1:8000/admin/api/studentanswer/)

Done!.
