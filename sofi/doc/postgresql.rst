.. -*- coding: utf-8 -*-

.. _sofi_con_postgresql:

Sofi con PostgresSQL
====================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Actualizado el: |today|

Para entornos de pruebas y producción es posible usar el servidor de base de 
datos PostgresSQL, para hacer esto posible ejecute el siguiente comando:

.. code-block:: python

    # aptitude install postgresql
    # exit

Luego active su entorno virtual Python si no lo tiene activado para instalar 
el adaptador de base de datos para PostgreSQL en Python `psycopg2`_, para esto 
ejecute el siguiente comando:

.. code-block:: python

    $ pip install -r ./requeriments/sofi-postgresql.txt

Seguidamente edita su archivo ``settings.py``, y ajusta las configuraciones de 
conexión a la base de datos como se describe a continuación:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'sofi'),                      # Or path to database file if using sqlite3.
            'USER': 'TU-USUARIO',                      # Not used with sqlite3.
            'PASSWORD': 'TU-CONTRASENA',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

Referencias
-----------

-   `Instalación de PostgreSQL en Debian GNU/Linux Wheezy`_

.. _psycopg2: https://pypi.python.org/pypi/psycopg2
.. _Instalación de PostgreSQL en Debian GNU/Linux Wheezy: https://lcaballero.wordpress.com/2013/03/01/instalacion-de-postgresql-en-debian-gnulinux-wheezy/

