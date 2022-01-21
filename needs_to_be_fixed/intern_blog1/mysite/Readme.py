A)Creating Virtual environment (https://realpython.com/lessons/creating-virtual-environment/)
1.which pip3
   /home/linux/.local/bin/pip3

2.Install virtual environment
   ~/Documents/django_project/intern_blog$python3 -m venv ./venv

3.~/Documents/django_project/intern_blog$ ls
   venv

--------------------------------------------------------------------------------------------------------------
B)Create PROJECT STRUCTURE
1.Create project(outer folder)
django-admin startproject mysite
2.
/Documents/django_project/intern_blog1/mysite$ python3 manage.py makemigrations 
3.
/Documents/django_project/intern_blog/mysite$ python3 manage.py migrate
4.create superuser
/Documents/django_project/intern_blog1/mysite$ python3 manage.py createsuperuser
5.run server
5.now check for table in admin panel.
-------------------------------------------------------------
c)Running development server
  /Documents/django_project/intern_blog/mysite$ python3 manage.py runserver
d)creating app(blog)
    /Documents/django_project/intern_blog/mysite$ python3 manage.py startapp blog
-----------------------------------------------------------------------------
e)in blog/models.py add "POST" name model
and migrate,migration,superuser
f)declare Post model  in admin.py declare Post model 
------------------------------------------------
create urls.py in blog(app)

------------------------------
run the code
1.go to the project using vscode
2./Documents/django_project/intern_blog1/mysite$ python3 manage.py runserver
