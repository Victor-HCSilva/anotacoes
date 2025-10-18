#!/bin/bash

echo "_____Iniciando container_____ \n\n ........Para cancelar click ctrl + c ..............."
sleep 5

python manage.py makemigrations

python manage.py migrate

python -u manage.py runserver 0.0.0.0:8000
