web: gunicorn backend.wsgi

release: python manage.py collectstatic
release: python manage.py test
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
