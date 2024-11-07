#!/bin/sh

# Aguardando o banco de dados ficar disponível usando wait-for-it.sh
./wait-for-it.sh db:5432 --timeout=10 --strict -- echo "Banco de dados está disponível. Aplicando migrações e iniciando o servidor..."

# Aplicando as migrações e iniciando o servidor
#python manage.py collectstatic --noinput

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
