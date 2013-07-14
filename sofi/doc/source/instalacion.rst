.. -*- coding: utf-8 -*-

.. _instalacion_sofi:

Instalar Sofi 1.0
=================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Actualizado el: |today|

Para instalar Sofi requiere realizar los siguientes pasos:

Dependencias previas
--------------------

Mínimamente requiere instalado las dependencias básicas para instalar aplicaciones Python, 
para hacer esto posible ejecute el siguiente comando:

.. code-block:: console

    # aptitude install build-essential python-dev python-pip python-setuptools
    # pip install virtualenv
    # exit

Descargar Sofi 1.0
------------------
Para descargar Sofi 1.0 ejecute los siguientes comandos:

.. code-block:: console

    $ hg clone https://macagua@bitbucket.org/conectivo/sofi sofi-1.0.x
    $ cd sofi-1.0.x/
    $ hg checkout 1.0.x

Para instalar Sofi requiere crear un entorno `virtual Python`_ dentro del cual 
realizara la instalación de dependencias Python con los siguientes comandos: 

.. code-block:: console

    $ virtualenv --distribute --python=/usr/bin/python2.6 .
    $ source ./bin/activate

Primero, instale Django 1.0 con el siguiente comando: 


.. code-block:: console

    $ pip install https://www.djangoproject.com/m/releases/1.0/Django-1.0.tar.gz

Segundo, instale el resto de las dependencias usando la herramienta `pip`_ 
con los siguientes comandos: 

.. code-block:: console

    $ cd sofi/
    $ pip install -r ./requeriments/compilado.txt
    $ pip install -r ./requeriments/sofi.txt

Tercero, crea la base de datos de Sofi 1.0 con el siguiente comando:

.. code-block:: console

    $ python manage.py syncdb

.. note::

  Cuando pregunte le dices que **'yes'** y responda adecuadamente a las preguntas.

Cuarto, inicie el servidor de ejecución Django con el siguiente comando: 

.. code-block:: console

    $ python manage.py runserver

.. note::

  Luego accedes a Sofi 1.0 en la siguiente dirección http://127.0.0.1:8000/
  
  Opcionalmente puede acceder a la interfaz administrativa en la siguiente dirección http://127.0.0.1:8000/admin/

Quinto, Si no va a instalar `paquetes Egg Python`_ adicionales a su aplicación Sofi, 
desactive en `entorno virtual Python`_ creado con el siguiente comando: 

.. code-block:: console

    $ deactivate

Sofi con SQLite
===============

Para entornos de pruebas y desarrollos se recomienda usar la base de datos `SQLite`_, 
para hacer esto posible ejecute el siguiente comando:

.. code-block:: console

    # aptitude install sqlite3 libsqlite3-dev

Referencias
-----------

-   `Creación de entornos virtuales Python`_
-   `Instalación de paquetes Python con Distribute y pip`_

.. _virtual Python: https://lcaballero.wordpress.com/2012/10/22/creacion-de-entornos-virtuales-python/
.. _pip: https://lcaballero.wordpress.com/2013/03/20/instalacion-de-paquetes-python-con-distribute-y-pip/
.. _entorno virtual Python: https://lcaballero.wordpress.com/2012/10/22/creacion-de-entornos-virtuales-python/
.. _paquetes Egg Python: https://plone-spanish-docs.readthedocs.org/en/latest/glosario.html#term-paquetes-egg
.. _SQLite: http://www.sqlite.org/
.. _Creación de entornos virtuales Python: https://lcaballero.wordpress.com/2012/10/22/creacion-de-entornos-virtuales-python/
.. _Instalación de paquetes Python con Distribute y pip: https://lcaballero.wordpress.com/2013/03/20/instalacion-de-paquetes-python-con-distribute-y-pip/
