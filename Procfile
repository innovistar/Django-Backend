web: gunicorn backend.wsgi --log-file -

release: python manage.py makemigrations --no-input-
release: python manage.py migrate --no-input-
