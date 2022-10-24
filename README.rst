=====
BOOTSTRAP 5 - MODULO
=====

Modulo es una aplicacion de Django Para implementar el crud y tablas en bootstrap 5.2

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'modulo',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('modulo/', include('modulo.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/modulo/ to participate in the poll.