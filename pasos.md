django-admin startproject proyecto1
python3 manage.py startapp appalgo

Modifico settings para instalar la app y usar postgresql en database
Creo el 1er modelo

Instalar Psycopg2-binary
    pip install psycopg2-binary

No puedo activar postgresql, noo tengo la contraseña -_- (pg_isready // ps aux | grep postgress)
    sudo systemctl start postgresql

Hago las migraciones
    python3 manage.py makemigrations appalgo
    python3 manage.py migrate
    python3 manage.py showmigrations appalgo
        Tiene  que dar algo como []0001_inicial
    ...