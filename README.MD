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