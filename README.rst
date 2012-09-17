README
======

Install & Run
-------------

Clone it::

    git clone git://github.com/PyConFr/Pyconfr.git
    cd Pyconfr/

Buildout it::

    python2.7 bootstrap.py
    ./bin/buildout
    
Init dev DB::

    ./bin/django syncdb
    ./bin/django loaddata src/pyconfr/fixtures/*.json
    
Static and messages (cf.: ./conf/locale)::
    
    ./bin/django collectstatic
    ./bin/django compilemessages
    
Start it in dev mode::

    ./bin/django runserver

Gunicorn start for prod::

    ./bin/django run_gunicorn -b 127.0.0.1:8001
