#!/usr/bin/env bash

echo "Migrando banco de dados..."
python3 src/manage.py makemigrations --noinput
python3 src/manage.py migrate --noinput

echo "Criando usuário padrão..."
python3 src/manage.py createsuperuser --noinput

echo "Tudo pronto!"