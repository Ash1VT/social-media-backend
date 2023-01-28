
## Requirements

* Python 3.10 (you can use virtual environment)
* Pip (v22.3)
* Docker (v20.10.21) and docker compose (v1.29.2)
* .env file in root project directory, which must contain secret key for tokens generating and name of database, port, user and password, like this:
  ```
  SECRET_KEY=your_secret_key
  DATABASE_NAME=your_database_name
  DATABASE_PORT=your_port
  DATABASE_USER=your_user
  DATABASE_PASSWORD=your_password
  ```
## Run Locally (ubuntu 22.04 LTS)

Clone the project
 
```bash
  git clone --branch develop https://github.com/ash1vt/social-media-backend
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create and launch docker container (you can set your own configuration in `docker-compose.yaml` file)

```bash
  sudo docker-compose up -d
```

Apply migrations for database

```bash
  flask db upgrade
```

Run server

```bash
  flask run
```

