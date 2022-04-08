# Code For Good - Team 64
## Anton 64.0

## About the Project

### Prerequisites

The email application uses Redis as its backing store. To install Redis

For Mac,
```console
foo@bar:~$ brew install redis
```

For Linux : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis

For Windows : https://redis.io/download

For Docker : https://hub.docker.com/_/redis/

Starting Redis

```console
foo@bar:~$ redis-server
```

### Installing

```console
foo@bar:~$ pip3 install -r requirements.txt
```

##### Database Migration

```console
foo@bar:~$ python3 manage.py makemigrations
foo@bar:~$ python3 manage.py migrate
```

##### Running the application

```console
foo@bar:~$ python3 manage.py runserver
```

### About Our Solution

### Screenshots