.. -*- coding: utf-8 -*-

.. _sofi_con_mysql:

Sofi con MySQL
==============

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Actualizado el: |today|

Opcionalmente, para entornos de pruebas y producción es posible usar el servidor 
de base de datos MySQL, para hacer esto posible ejecute el siguiente comando:

.. code-block:: console

    # aptitude install mysql-server mysql-client libmysqlclient15-dev
    # exit

Luego active su entorno virtual Python si no lo tiene activado para instalar 
la interfaz Python a MySQL `MySQL-python`_, para esto ejecute el siguiente comando:

.. code-block:: console

    $ pip install -r ./requeriments/sofi-mysql.txt

Seguidamente edita su archivo ``settings.py``, y ajusta las configuraciones de 
conexión a la base de datos como se describe a continuación:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'sofi'),                      # Or path to database file if using sqlite3.
            'USER': 'TU-USUARIO',                      # Not used with sqlite3.
            'PASSWORD': 'TU-CONTRASENA',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

Referencias
-----------

-   `Instalación de un servidor MySQL en Debian Lenny`_
-   `Instalación y configuración de Python, Django y MySQL (WIndows)`_

.. _MySQL-python: https://pypi.python.org/pypi/MySQL-python/1.2.4
.. _Instalación y configuración de Python, Django y MySQL (WIndows): http://upfcode.wikispaces.com/Instalaci%C3%B3n+y+configuraci%C3%B3n+de+Python,+Django+y+MySQL+(WIndows)
.. _Instalación de un servidor MySQL en Debian Lenny: https://lcaballero.wordpress.com/2010/08/16/instalacion-de-un-servidor-mysql-en-debian-lenny/
