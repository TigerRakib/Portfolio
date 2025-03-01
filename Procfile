web: gunicorn my_folio.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn my_folio.wsgi