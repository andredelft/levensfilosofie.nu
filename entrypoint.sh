python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compress --force
gunicorn levensfilosofie.wsgi:application --bind 0.0.0.0:$1
