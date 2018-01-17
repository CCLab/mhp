# mhp

## Installation (local development - Docker)

1. Request appropriate permissions to Docker images on [our Docker registry](https://registry.laboratorium.ee/) from [kazet](mailto:krzysztof.zajac@laboratorium.ee)

2. Log in to our Docker repository:

        docker login registry.laboratorium.ee

3. Build Docker images

        docker-compose build

4. Run Docker images

        docker-compose up

You may also use the `run_development.sh` script.

## Installation (local development - classic)

### Prerequisites

- [Python 3.5+](https://www.python.org/)
- [Node.js](https://docs.npmjs.com/getting-started/installing-node)
- [SASS](http://sass-lang.com/install)

### Installation instructions

1. Create and enter a Python 3 [virtualenv](https://virtualenv.pypa.io/en/stable/):

        virtualenv -p python3 venv
        source venv/bin/activate
    (alternatively you can use a [conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html) or [Pipenv](https://docs.pipenv.org/))

2. Install the Python requirements:

        pip install -r requirements/local.txt

    This project uses [Django 1.11](https://docs.djangoproject.com/en/1.11/)

3. Install the npm requirements:

        npm install

4. Create and fill out the local settings file:

       cp src/settings/env.local.example src/settings/.env
    (alternatively you can set those settings as environment variables)

5. Configure your local database by filling out `DJANGO_DATABASE_URL` setting in `.env` file.

    If there is no good reason to do otherwise, it should be a [Postgres](https://www.postgresql.org/) database since that's what we are using by default on production servers.

6. Run database migrations:

        python manage.py migrate

7. Install [npm](https://www.npmjs.com/) packages:

        npm install

8. Run test command to make sure everything is in order:

        python manage.py test

9. Start the development server:

       python manage.py runserver

## Development guidelines
Before committing to this repository, please read [the official Laboratorium EE development guidelines](https://github.com/EE/bombaatomowa).
