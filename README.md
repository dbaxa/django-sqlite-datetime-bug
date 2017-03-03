# django-sqlite-datetime-bug
This repository contains code to demonstrate a bug with filtering on __date of a DateTimeField when TIME_ZONE=None that exists in Django 1.10 when sqlite is used. This issue does not affect Django 1.11 as it does not allow TIME_ZONE to be set to None.

After installing the required dependencies (`pip install requirements.txt`) run `python manage.py test` .
