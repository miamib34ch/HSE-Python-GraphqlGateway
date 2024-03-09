# GraphQL API Gateway

GraphQL API Gateway for microservices interaction.

## Requirements:

Install the appropriate software:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (optional).

## Installation

Clone the repository to your computer:
```bash
git clone https://github.com/mnv/python-course-graphql-gateway
```

1. To configure the application copy `.env.sample` into `.env` file:
    ```shell
    cp .env.sample .env
    ```
   
    This file contains environment variables that will share their values across the application.
    The sample file (`.env.sample`) contains a set of variables with default values. 
    So it can be configured depending on the environment.

2. Build the container using Docker Compose:
    ```shell
    docker compose build
    ```
    This command should be run from the root directory where `Dockerfile` is located.
    You also need to build the docker container again in case if you have updated `requirements.txt`.

3. To run the project inside the Docker container:
    ```shell
    docker compose up
    ```
   When containers are up server starts at [http://0.0.0.0:8000/graphql](http://0.0.0.0:8000/graphql). You can open it in your browser.

## Usage

### Queries

Query example to request a list of favorite places: 
```graphql
query {
  places {
    latitude
    longitude
    description
    city
    locality
  }
}
```

Query example to request a list of favorite places with countries information: 
```graphql
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
```

Query example to get specific favorite place: 
```graphql
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
```

Query example to create new favorite place: 
```graphql
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
```

Query example to delete specific favorite place: 
```graphql
mutation {
  deletePlace(placeId: 1) {
    result
  }
}
```

Query example to create a favorite place: 
```graphql

```

This query will request additional information about related countries in optimal way using data loaders to prevent N + 1 requests problem.

### Automation commands

The project contains a special `Makefile` that provides shortcuts for a set of commands:
1. Build the Docker container:
    ```shell
    make build
    ```

2. Generate Sphinx documentation run:
    ```shell
    make docs-html
    ```

3. Autoformat source code:
    ```shell
    make format
    ```

4. Static analysis (linters):
    ```shell
    make lint
    ```

5. Autotests:
    ```shell
    make test
    ```

    The test coverage report will be located at `src/htmlcov/index.html`. 
    So you can estimate the quality of automated test coverage.

6. Run autoformat, linters and tests in one command:
    ```shell
    make all
    ```

Run these commands from the source directory where `Makefile` is located.

## Documentation

The project integrated with the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation engine. 
It allows the creation of documentation from source code. 
So the source code should contain docstrings in [reStructuredText](https://docutils.sourceforge.io/rst.html) format.

To create HTML documentation run this command from the source directory where `Makefile` is located:
```shell
make docs-html
```

After generation documentation can be opened from a file `docs/build/html/index.html`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
