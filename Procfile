release: python manage.py migrate && python manage.py loaddata home/fixtures/initial_data.json
web: gunicorn myportfolio.wsgi --log-file -
