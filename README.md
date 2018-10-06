# Django Blog Sample Application

## how to run

```bash
mkdir static
mkdir media

docker-compose up --build -d
docker-compose run web ./manage.py collectstatic
docker-compose run web ./manage.py makemigrations auth users blog
docker-compose run web ./manage.py migrate
docker-compose run web ./manage.py createsuperuser
```
