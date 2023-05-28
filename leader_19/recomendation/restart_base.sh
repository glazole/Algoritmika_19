#!/bin/bash

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete

mysql -uroot -e "drop database Leader_19"
mysql -uroot -e "create database Leader_19"
mysql -uroot -e "create user 'leader_19'@'localhost' identified by 'leader_19';"
mysql -uroot -e "grant all privileges on Leader_19.* to 'box'@'localhost' with grant option;"

#python3 manage.py migrate --fake-initial
python3 manage.py makemigrations app
python3 manage.py migrate

#cd testing/
#find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete

#python2 manage.py create_base_Q.py
