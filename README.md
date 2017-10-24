# Web Friends Portal

Development of the project:\
"Web Platform for Experiments with the Friends-of-Friends Hybrid Parallel Algorithm for Astronomical Objects Classification"\
\
Original application developed by Otávio Madalosso: https://github.com/Madalosso/TG/tree/master/Django%20Proj/webfriends 

## Summary

* [Running Local](#running-local)
* [Using Heroku](#using-heroku)
* [References](#references)

-----

## Running Local
Using an virtual environment.

1. Create new virtual environment: 
``` bash 
$ sudo python2 -m pip install virtualenv
($  virtualenv --version)
$ virtualenv myenv
```
2. Activate it and create an requirements log: 
``` bash 
$ source myvenv/bin/activate
$ pip freeze > requirements.txt
($ pip list)
```
<!---  3.0 - Create project inside the virtualenv (in case of new project): $ django-admin startproject projname . --->

3. Install all the packages which the project will use:
``` bash 
$ pip install Django==1.8	
$ pip install Celery==3.1.18
$ pip install django-registration-redux==1.4
$ pip install --upgrade django-crispy-forms==1.6.1
$ pip install django-jsonview==1.0.0
$ wget http://download.redis.io/releases/redis-3.0.0.tar.gz
$ tar xzvf redis-3.0.0.tar.gz
$ cd redis-3.0.0
$ make
$ pip install django-celery
$ pip install redis
$ pip install pipenv
$ pipenv install requests==2.8.1
```
4. For an existing git project just clone it inside the virtual environment 

5. Start the Django app:

``` bash
to start redis server: $ /redis-3.0.0/src/redis-server
to start django server: $ ./manage.py runserver
to start celery worker: $ celery -A webfriends worker -l info
```
- **Attention!** Changes are needed in settings, experiments and tasks files.

## Using Heroku

## References


