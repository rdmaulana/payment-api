# Dockerizing Simple Payment API

## Build with Flask, MongoDB, Celery, Redis

## How to run this project locally

1. Rename .env.sample to .env
2. Fill out required variable (SECRET_KEY)
3. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test API at [http://localhost:5000](http://localhost:5000)
    Check Dashboard Celery at [http://localhost:5555](http://localhost:5555)