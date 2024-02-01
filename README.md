# prueba_quick_python

## Especificaciones de lenguaje

```sh
Python 3.8.18
```

## Especificaciones de Base de datos

```sh
Postgresql
```

## Instalación

1. Clone el repositorio

```sh
git clone https://github.com/helmuntv/prueba_python.git
```
2. Crea un entorno virtual
```sh
python3 -m venv env
```

3. Activa el entorno virtual

linux
```sh
source env/bin/activate
```
windows
```sh
env/Scripts/activate
```

4. Ubicarse en la carpeta del proyecto

```sh
cd store
```

5. Copiar y configurar '.env':

```sh
cp .env.example .env
```

6. Instalar las dependencias

```sh
pip install -r requirements.txt
```

8. Crea tu base de datos "store"

9. Configura variables de la base de datos en tu .env:

```sh
DB_NAME=store
DB_USER=postgres
DB_PASSWORD=prueba
DB_HOST=localhost
DB_PORT=5432
```
10. Ejecuta las migraciones:

```sh
python3 manage.py migrate
```

11. Correr el proyecto:

```sh
python3 manage.py runserver
```

## Documentación

http://localhost:8000/swagger/