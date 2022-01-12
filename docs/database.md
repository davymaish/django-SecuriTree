
INSTALL A DATABASE
-----------

You will need a database to store the application information as per the EPIUSE Functional Requirement Specification that the application must support persistent secure data storage.


## WINDOWS OPERATING SYSTEM

### INSTALL MYSQL
You can read the following article on how to install MYSQL Community Server in your local machine:

[Online Tutorials Point.](https://www.onlinetutorialspoint.com/mysql/install-mysql-on-windows-10-step-by-step.html)


### INSTALL POSTGRESQL
You can read the following article on how to install POSTGRESQL Database in your local machine:

[Postgresql Tutorial.](https://www.postgresqltutorial.com/install-postgresql/)


## LINUX OPERATING SYSTEM

### INSTALL MYSQL

Open a new terminal and type in the following commands:

   ```sh
    sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
    sudo mysql_install_db
    sudo mysql_secure_installation
   ```

INSTALL MARIADB

If you prefer MariaDB over MySQL you can run the following commands

   ```sh
    sudo apt-get install python-pip python-dev mariadb-server libmariadbclient-dev libssl-dev
    sudo mysql_secure_installation
   ```

CREATE USER FOR DJANGO MYSQL

Create the project database ex. epiuse and admin user ex. epiuseadmin and grant all database permissions and privalleges and to the user. Simply run the following commands:

   ```sh
    mysql -u root -p
    CREATE DATABASE epiuse CHARACTER SET UTF8;
    CREATE USER epiuseadmin@localhost IDENTIFIED BY 'secret';
    GRANT ALL PRIVILEGES ON myproject.* TO epiuseadmin@localhost;
    FLUSH PRIVILEGES;
    exit
   ```

### INSTALL POSTGRESQL

The application can also use POSTGRESQL Database for its persistent secure data storage. If you prefer POSTGRESQL over MYSQL, run the following commands to install POSTGRESQL Database:

   ```sh
    sudo apt-get install postgresql postgresql-contrib
    sudo apt-get install libpq-dev python3-dev
    pip install psycopg2
   ```

CREATE USER FOR DJANGO POSTGRESQL

Create the project database ex. epiuse and admin user ex. epiuseadmin and grant all database permissions and privalleges and to the user. Simply run the following commands:

   ```sh
    sudo -u postgres psql
    CREATE DATABASE epiuse;
    CREATE USER epiuseadmin WITH ENCRYPTED PASSWORD 'mypass';
    ALTER ROLE epiuseadmin SET client_encoding TO 'utf8';
    ALTER ROLE epiuseadmin SET default_transaction_isolation TO 'read committed';
    ALTER ROLE epiuseadmin SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE epiuse TO epiuseadmin;
    \q
   ```

CONFIGURE YOUR APP DATABASE SETTINGS
-----------

Open up epiuse/settings.py and change the following keys in the DATABASES 'default' item to match your database connection settings.

For MYSQL Database Connection as per the installation above:

   ```sh
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'epiuse'
    'USER': 'epiuseadmin'
    'PASSWORD': 'secret'
    'HOST': localhost

   ```

For POSTGRESQL Database Connection as per the installation above:

   ```sh
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'epiuse'
    'USER': 'epiuseadmin'
    'PASSWORD': 'secret'
    'HOST': localhost
   ```