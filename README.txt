** Install:

- Python 
- VSCode
- PGAdmin
- Postman

** Install modules Django projects:

Open CMD on main src:
- pip install django
	- pip install djangorestframework
	- pip install django-cors-headers

** Create Django project:

Open CMD src of new project :
- django-admin startproject NameProject

** Runing the project:

- python manage.py runserver

** Create Apps inside in Project:

- python manage.py startapp NameApp

** Add in settings.py:

Apps:
- 'rest_framework','corsheaders', 'CovidAPI.apps.CovidapiConfig'

CORS_ORIGIN_ALLOW_ALL = True  //Not recommended in prod

Middleware:
- 'corsheaders.middleware.CorsMiddleware'