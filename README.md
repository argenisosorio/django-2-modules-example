# Django 2 modules example
<br />

## Requirements
```
Django==2.0.2
Python 3.4.2
```
<br />

## Note
We will use # for commands as superuser

We will use $ for commands as a regular user

<br />

## Deploy with python virtualenv's
```
# apt-get install python3.4 python3-pip python3.4-dev python3-setuptools

# apt-get install python3-virtualenv virtualenvwrapper

$ virtualenv -p python3 my_env

$ source my_env/bin/activate

$ cd django-2-modules-example

$ pip install -r requirements.txt
```
<br />

## Run project
```
$ cd django-2-modules-example

$ python manage.py migrate

$ python manage.py runserver
```