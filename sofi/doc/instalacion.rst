.. -*- coding: utf-8 -*-

.. _instalacion_sofi:

Instalar Sofi 2.0
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

    # aptitude install build-essential python-dev python-pip python-setuptools libfreetype6-dev libpng-dev
    # pip install virtualenv
    # exit

Descargar Sofi 2.0
------------------
Para descargar Sofi 2.0 ejecute los siguientes comandos:

.. code-block:: console

    $ hg clone https://macagua@bitbucket.org/conectivo/sofi sofi-2.0.0
    $ cd sofi-2.0.0/
    $ hg checkout default

Para instalar Sofi requiere crear un entorno `virtual Python`_ dentro del cual 
realizara la instalación de dependencias Python con los siguientes comandos: 

.. code-block:: console

    $ virtualenv --distribute --python=/usr/bin/python2.7 .
    $ source ./bin/activate

Primero, instale el resto de las dependencias usando la herramienta `pip`_ 
con los siguientes comandos: 

.. code-block:: console

    $ cd sofi/
    $ pip install -r ./requirements/compilado.txt
    $ pip install -r ./requirements/sofi.txt

Segundo, crea la base de datos de Sofi 2.0 con el siguiente comando:

.. code-block:: console

    $ python manage.py syncdb

.. note::

  .. Cuando pregunte le dices que **'yes'** y responda adecuadamente a las preguntas.
  
  En un momento de la creación de la base de datos Django le realizara la siguiente pregunta:
  
  You just installed Django's auth system, which means you don't have any superusers defined.
  
  Would you like to create one now? (yes/no): 

  Usted le responde **yes**, seguidamente debe responder adecuadamente 
  a las siguientes preguntas que Django le realizara.

Tercero, inicie el servidor de ejecución Django con el siguiente comando: 

.. code-block:: console

    $ python manage.py runserver

.. note::

  Luego accedes a Sofi 2.0 en la siguiente dirección http://localhost:8000/
  
  Opcionalmente puede acceder a la interfaz administrativa en la siguiente dirección http://localhost:8000/admin/

Cuarto, Si no va a instalar `paquetes Egg Python`_ adicionales a su aplicación Sofi, 
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
