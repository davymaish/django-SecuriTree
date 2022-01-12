INSTALL MYSQL

    ``
    sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
    sudo mysql_install_db
    sudo mysql_secure_installation

    ``

    INSTALL MARIADB

    ``
    sudo apt-get install python-pip python-dev mariadb-server libmariadbclient-dev libssl-dev
    sudo mysql_secure_installation

    ``

    CREATE USER

    ``
    mysql -u root -p
    CREATE DATABASE myproject CHARACTER SET UTF8;
    CREATE USER myprojectuser@localhost IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON myproject.* TO myprojectuser@localhost;
    FLUSH PRIVILEGES;
    exit

    ``

    INSTALL POSTGRESQL FOR DJANGO

    ``
    sudo apt-get install postgresql postgresql-contrib
    sudo apt-get install libpq-dev python3-dev
    pip install psycopg2

    ``

    CREATE USER FOR DJANGO POSTGRESQL

    ``
    sudo -u postgres psql
    CREATE DATABASE mydb;
    CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypass';
    ALTER ROLE myuser SET client_encoding TO 'utf8';
    ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myuser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
    \q

    ``

Configure your app database settings.
    Open up epiuse/settings.py and change the following keys in the DATABASES 'default' item to match your database connection settings.


    ``
    'ENGINE': 'django.db.backends.mysql',
    'NAME': securitree
    'USER': epiuse
    'PASSWORD': 123456
    'HOST': localhost

    ``


    ``
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': securitree
    'USER': epiuse
    'PASSWORD': 123456
    'HOST': localhost

    ``