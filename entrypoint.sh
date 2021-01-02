python manage.py migrate
python manage.py populate_symposia
python manage.py populate_members
python manage.py populate
python manage.py collectstatic --no-input
gunicorn levensfilosofie.wsgi:application --bind 0.0.0.0:$1
