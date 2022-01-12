Installation In an Existing Django Application
-----------

1. Add "SecuriTree" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'SecuriTree',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('securitree/', include('SecuriTree.urls')),

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