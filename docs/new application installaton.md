


Install a New Application
-----------
1. Open a new Terminal window.



1. Install a virtual environment

    ``
    sudo pip install epiusenv
    ``

2. Clone or download the repo and navigate to the project folder:

   ```sh
   git clone https://github.com/iamdanre/SecuriTree.git
   ```

3. create project directory and navigate into the  directory

    ``
    mkdir ~/epiuse
    cd ~/epiuse
   ``

3. To install the SecuriTree package:

   ``
    python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz
    ``

2. Activate virtual environment and sart the project

    ``
    virtualenv epiusenv
    source epiusenv/bin/activate
    django-admin.py startproject epiuse
    ``

4. Configure your SecuriTree Application
Open up epiuse/settings.py and add the following keys at the end of the file.

    ``
    # SecuriTree Configs
    FIXTURE_DIRS = [BASE_DIR / 'fixtures']
    AUTH_USER_MODEL = 'SecuriTree.User'
    LOGIN_REDIRECT_URL = '/home'
    LOGIN_URL = '/login/'
    LOGOUT_REDIRECT_URL = '/login/'
    ``
2. Include the SecuriTree URLconf in the epiuse/urls.py like this::

    ``
    path('securitree/', include('SecuriTree.urls')),
    ``

3. Install a database

   This application has been tested in mysql and postgesql databases. Choose your favourite database. Individual installation guide for each database can be found on docs/database folder. If you have your favourite database installed and configured continue to step 4.


4. Make migration Database

    ``
    python3 manage.py makemigrations SecuriTree
    python manage.py migrate
    ``
 
4. Populate Database

   \*Note: The database will initially be empty for review purposes. The database can be populated using the JSON files in the SecuriTree/fixtures directory by running the following commands in the terminal:

    ``
    python3 manage.py populateUserData SecuriTree/fixtures/registered_users.json
    python3 manage.py populateSystemData SecuriTree/fixtures/system_data.json
    ``

    This will populate the database with the user data required to log in after salting and hashing the passwords. It also populates the relevant system data collections required for constructing the Security Entity Hierarchy.

4. Web App: 

While still inside the project directory run the following command. This will serve the application:

   ```sh
   python3 manage.py runserver
   ```
   .
   Navigate to [http://127.0.0.1:8000/securitree/](http://127.0.0.1:8000/securitree/) in your browser to use the application.
