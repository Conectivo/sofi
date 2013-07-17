.. -*- coding: utf-8 -*-

.. _apache2_mod_python:

Apache2 con Sofi
================

:Autor(es): Leonardo J. Caballero G.
:Correo(s): leonardocaballero@gmail.com
:Lanzamiento: |version|
:Actualizado el: |today|

Para instalar Sofi requiere realizar los siguientes pasos:

Dependencias previas
--------------------

Mínimamente requiere instalado las dependencias básicas para 
instalar aplicaciones Python, para hacer esto posible ejecute 
el siguiente comando:

.. code-block:: console

    # aptitude install apache2 libapache2-mod-python
    # a2enmod python
    # service apache2 reload

VirtualHost y mod_python
------------------------

Para hacer disponible Sofi a través de un servidor Web, ejecute 
el siguiente comando:

.. code-block:: console

    # cp ./apache2_sofi.site /etc/apache2/sites-available/sofi.site

Entonces edite el archivo de configuración VirtualHost de 
Apache, con el siguiente comando:

.. code-block:: console

    # vim /etc/apache2/sites-available/sofi.site
    
Usted adaptar su archivo de configuración VirtualHost como se 
muestra a continuación:

.. code-block:: cfg

    <VirtualHost *:80>

        ServerAdmin TU-NOMBRE@CORREO
        ServerName TU-HOST-O-localhost

        <Location "/">
            SetHandler python-program
            PythonHandler myvirtualdjango
            SetEnv DJANGO_SETTINGS_MODULE sofi.settings
            SetEnv PYTHON_EGG_CACHE /var/tmp/egg
            PythonDebug Off
            PythonPath "['/<RUTA>/bin','/<RUTA>/lib/python2.7/site-packages','/<RUTA>/sofi', '/<RUTA>/sofi/sofi', '/<RUTA>/apps'] + sys.path"
        </Location>

        Alias /admin_media/ /<RUTA>/lib/python2.7/site-packages/django/contrib/admin/media/
        <Location /admin_media/>
            SetHandler none
            Options -Indexes
        </Location>

        Alias /site_media/ /<RUTA>/sofi/site_media/
        <location /site_media/>
            SetHandler none
            Options -Indexes
        </Location>

        ErrorLog ${APACHE_LOG_DIR}/sofi.error.log

        # Possible values include: debug, info, notice, warn, error, crit,
        # alert, emerg.
        LogLevel warn

        CustomLog ${APACHE_LOG_DIR}/sofi.access.log combined

    </VirtualHost>

.. tip::

  Debe cambiar **<RUTA>** por la ruta adecuada en el contexto de la explicación.

Después debe habilitar la configuración VirtualHost creada como 
un sitio disponible para Apache:

.. code-block:: console

    # ln -s /etc/apache2/sites-available/sofi.site /etc/apache2/sites-enabled/sofi.site
    # a2ensite sofi.site

Seguidamente agregue el archivo ``myvirtualdjango.py`` dentro 
del directorio ``bin`` de su ``virtualenv`` python (adecue la 
ruta a la ruta real de su instalación):

.. code-block:: python

    #myvirtualdjango.py
    
    activate_this = '/<RUTA>/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))
    
    from django.core.handlers.modpython import handler

.. tip::

  Debe cambiar **<RUTA>** por la ruta adecuada en el contexto de la explicación.

En el archivo ``settings.py`` de tu aplicación debes cambiar la variable 
``DEBUG`` de **True** a **False**


Otorgas permisos al servicio de Apache para que acceda al directorio 
de instalación de Sofi, con el siguiente comando:

.. code-block:: console

    # chown -R :www-data /<RUTA>/sofi
    # chmod g+rw /<RUTA>/sofi/sofi/sofi.db

.. tip::

  Debe cambiar **<RUTA>** por la ruta adecuada en el contexto de la explicación.

.. warning::

  Si usted esta solo usando el servidor Web para ejecutar Sofi le recomiendo que 
  deshabilite el sitio por defecto de Apache ya que esta configuración VirtualHost 
  es para un solo sitio Web dentro del servidor Web Apache.
  
  Para esto ejecute el siguiente comando: ``a2dissite default``.
  
  De no ser así necesita adaptar su configuración VirtualHost de Sofi para que 
  conviva con los demás sitios Web.

Reinicie y recargue el servicio de Apache, con los siguientes comandos:

.. code-block:: console

    # service apache2 restart
    # service apache2 reload

.. note::

  Luego accedes a Sofi en la siguiente dirección http://localhost/
  
  Opcionalmente puede acceder a la interfaz administrativa en la siguiente dirección http://localhost/admin/

.. tip::

  Cada ves que cambies algo en tu aplicación Sofi debe recargar las configuraciones 
  del servidor Apache, con el comando: **service apache2 reload**

Referencias
-----------

-   `Django, mod_python and virtualenv`_.

.. _virtual Python: https://lcaballero.wordpress.com/2012/10/22/creacion-de-entornos-virtuales-python/
.. _entorno virtual Python: https://lcaballero.wordpress.com/2012/10/22/creacion-de-entornos-virtuales-python/
.. _Django, mod_python and virtualenv: http://mydjangoblog.com/2009/03/30/django-mod_python-and-virtualenv/
