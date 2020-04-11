# CubaVSCovid

> Una app para organizar la impresión y distribución de piezas 3D para respiradores artificiales en Cuba, como parte de la lucha contra la COVID-19.

## Arquitectura

Esta aplicación web consta de un `backend` y un `frontend`, comunicados por una `API` en `GraphQL`.

**Stack frontend:**

* VueJS
* NuxtJS
* Buefy
* Axios
* Apollo
* Vuelidate
* Vuex

Más detalles en [package.json](frontend/package.json).

**Stack backend:**

* Python 3.6
* Django 3.0.4
* Graphene 2.1.8
* Djangorestframework 3.2.1

Más detalles en [pyproject.toml](backend/pyproject.toml).

## Ejecutar el `frontend` en modo desarrollo:

Si usas `yarn`:

```bash
cd frontend
yarn install
yarn dev
```

Si usas `npm`:


```bash
cd frontend
npm install
npm run dev
```

El `frontend` quedará expuesto en `localhost:3000`.

## Ejecutar el `backend` en modo desarrollo:

Usamos `poetry` como manejador de dependencias de `Python`.

```bash
pip3 install --user poetry
cd backend
poetry install
poetry run ./dev.py createsuperuser
poetry run ./dev.py runserver
```

El `backend` quedará expuesto en `localhost:8000`.

Sugerencia: Aplica estos alias en tu `.bashrc` o `.zshrc` para que sea más cómodo:

```
alias poetry="python3 -m poetry"
alias django="poetry run ./dev.py"
alias djm="django makemigrations; django migrate;"
alias djr="django runserver"
```

Así, puedes usar estos comandos:

Comando | Descripción
--------|------------
poetry install | Instalar dependencias
djr | Levantar backend
djm | Migrar base de datos

## Contribuir

¿Deseas contribuir? Contáctame en [Telegram](https://t.me/lugodev).

## Guía de despliegue

1. Clona el repositorio.

2. Colócalo en `/root/apps/cubavscovid/codebase` en tu VPS.

3. Crea un archivo `.env` en dicha locación y añade las siguientes líneas:

    ```.env
    CUBAVSCOVID__DJANGO_SECRET_KEY=unallavesecretaaleatoria
    CUBAVSCOVID__DJANGO_HOSTNAME=covid.copincha.org
    CUBAVSCOVID__DJANGO_PRODUCTION_STATIC_ROOT=/storage/frontend/static
    CUBAVSCOVID__DJANGO_PRODUCTION_MEDIA_ROOT=/storage/frontend/static/media
    ```

4. Crea un archivo `.env` dentro de `frontend` y añade las siguientes líneas:

    ```..env
    BASE_URL=http://covid.copincha.org
    BACKEND_BASE_URL=http://covid.copincha.org/api/
    API_BASE_URL=http://covid.copincha.org/api/
    ```

5. Levanta los servicios usando `docker-compose`:

    ```..env
    sudo docker-compose up --build
    ```

6. Habilita los puertos 80 y 443 en el firewall para permitir el tráfico hacia la aplicación.

**Voilà!**

🦠😷🦠