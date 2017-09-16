===============
django po
===============

.. image:: https://img.shields.io/pypi/v/django_po.svg
    :target: https://pypi.python.org/pypi/django_po

.. image:: https://img.shields.io/pypi/pyversions/django_po.svg
    :target: https://pypi.python.org/pypi/django_po

Overview
========

- This is useful for export PO files data inot files using simple commands

- Currently it's support xlsx, xls, csv file format in export

Documentation
=============

- Installation -
   * Run ::

      pip install django_po

   * Add 'django_po' to your INSTALLED_APPS ::

      'django_po',

- Export -
   * Run django management commands like below ::

       python manage.py export_po <language> --format=<file format> (Optional) # default format: 'xlsx'

       1) python manage.py export_po en   #It will create 'django_en.xlsx'

       2) python manage.py export_po en --format=xlsx,xls,csv  #It will create 'django_en.xlsx', 'django_en.xls', 'django_en.csv'

       3) python manage.py export_po en,ar,hi #It will create 'django_en.xlsx', 'django_ar.xlsx', 'django_hi.xlsx'

       4) python manage.py export_po en,hi --format=xlsx,csv # 'django_en.xlsx', 'django_en.csv', 'django_hi.xlsx', 'django_hi.csv'

License
=======

django_po is an Open Source project licensed under the terms of the `MIT license <https://github.com/sainipray/django_po/blob/master/LICENSE>`_
