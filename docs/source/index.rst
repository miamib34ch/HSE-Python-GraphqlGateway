GraphQL API Gateway
===================

GraphQL API шлюз для взаимодействия с микросервисами.

Зависимости
===========

Install the appropriate software:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (optional).


Установка
=========

Install and deploy the following projects:

https://github.com/miamib34ch/HSE-Python-CountriesInformer

https://github.com/miamib34ch/HSE-Python-FavoritePlaces

Clone the repository to your computer:

.. code-block::shell
    git clone https://github.com/miamib34ch/HSE-Python-GraphqlGateway

1. To configure the application copy `.env.sample` into `.env` file:

    .. code-block::shell
        cp .env.sample .env

    This file contains environment variables that will share their values across the application.
    The sample file (`.env.sample`) contains a set of variables with default values.
    So it can be configured depending on the environment.

2. Build the container using Docker Compose:

    .. code-block::shell
        docker compose build

    This command should be run from the root directory where `Dockerfile` is located.
    You also need to build the docker container again in case if you have updated `requirements.txt`.

3. To run the project inside the Docker container:

    .. code-block::shell
        docker compose up

   When containers are up server starts at [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql). You can open it in your browser.

Использование
=============

Query example to request a list of favorite places:

    .. code-block::graphql
        query {
          places {
            latitude
            longitude
            description
            city
            locality
          }
        }

Query example to request a list of favorite places with countries information:

    .. code-block::graphql
        query {
          places {
            latitude
            longitude
            description
            city
            locality
            country {
              name
              capital
              alpha2code
              alpha3code
              capital
              region
              subregion
              population
              latitude
              longitude
              demonym
              area
              numericCode
              flag
              currencies
              languages
            }
          }
        }

Query example to get specific favorite place:

    .. code-block::graphql
        {
          place(placeId:1) {
            id
            latitude
            longitude
            description
            city
            locality
          }
        }

Query example to create new favorite place:

    .. code-block::graphql
        mutation {
          createPlace (
            latitude: 25.20485,
            longitude: 55.27078,
            description: "Nice food."
          ) {
            place {
              id
              latitude
              longitude
              description
              city
              locality
            }
            result
          }
        }

Query example to update a favorite place:

    .. code-block::graphql
        mutation {
          updatePlace (
            placeId: 1,
            latitude: 25.20485,
            longitude: 55.27078,
            description: "updated"
          ) {
            result
          }
        }

Query example to delete specific favorite place:

    .. code-block::graphql
        mutation {
          deletePlace(placeId: 1) {
            result
          }
        }

Автоматизация
=============

The project contains a special `Makefile` that provides shortcuts for a set of commands:

1. Build the Docker container:

    .. code-block::shell
            make build

2. Generate Sphinx documentation run:

    .. code-block::shell
            make docs-html

3. Autoformat source code:

    .. code-block::shell
            make format

4. Static analysis (linters):

    .. code-block::shell
           make lint

5. Autotests:

    .. code-block::shell
            make test

6. Run autoformat, linters and tests in one command:

    .. code-block::shell
            make all

Run these commands from the source directory where `Makefile` is located.

The project integrated with the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation engine.
It allows the creation of documentation from source code.
So the source code should contain docstrings in [reStructuredText](https://docutils.sourceforge.io/rst.html) format.

To create HTML documentation run this command from the source directory where `Makefile` is located:

    .. code-block::shell
        make docs-html

After generation documentation can be opened from a file `docs/build/html/index.html`.

Документация
============

Клиенты
=======

.. automodule:: clients.base.base
    :members:

.. automodule:: clients.countries
    :members:

.. automodule:: clients.places
    :members:

Модели
======

.. automodule:: models.mixins
    :members:

.. automodule:: models.countries
    :members:

.. automodule:: models.places
    :members:

Схемы
=====

.. automodule:: schema.mutation
    :members:

.. automodule:: schema.query
    :members:

Сервисы
=======

.. automodule:: services.countries
    :members:

.. automodule:: services.places
    :members:

