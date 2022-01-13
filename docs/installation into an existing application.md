
## Installation In an Existing Django Application

Follow the steps outlined below to integrate SecuriTree into your existing django application:

1. Open up terminal(on linux) or command prompt on windows and navigate to you project directory ex. epiuse.

   ```sh
   cd epiuse
   ```
2. Run the following command to install SecuriTree Package from github.

   ```sh
    python -m pip install --user https://github.com/davymaish/django-SecuriTree.git
   ```
3. Open up epiuse/settings.py and add "SecuriTree" package to your INSTALLED_APPS setting like this::

   ```sh
    INSTALLED_APPS = [
        ...
        'SecuriTree.apps.SecuritreeConfig',
    ]
   ```
   This will activate SecuriTree models to be seen by your application.

   Add this to the end of the settings.py to use the SecuriTree user model

   ```sh
   AUTH_USER_MODEL = 'SecuriTree.User'
   ```

4. Include the SecuriTree URLconf in your project url ex. epiuse/urls.py like this:

   ```sh
    path('securitree/', include('SecuriTree.urls')),
   ```

5. Make migration Database
    
   ```sh
    python manage.py makemigrations SecuriTree
    python manage.py migrate
   ```
   This will create SecuriTree database tables in your project database.
 
6. Populate Database

   The database SecuriTree tables as at this step are empty. SecuriTree application comes bundled with dummy data in form of JSON files in the SecuriTree/fixtures directory which you can use to populate the database.

   To populate users data run the following commands in the terminal in the project root directory:
    
   ```sh
    python manage.py populateUserData SecuriTree/fixtures/registered_users.json
   ```
    To populates the relevant system data collections required for constructing the Security Entity Hierarchy:

   ```sh
    python manage.py populateSystemData SecuriTree/fixtures/system_data.json
   ```
7. Web App: 

    While still inside the project directory run the following command. This will serve the application:

   ```sh
   python manage.py runserver
   ```
   .
   Navigate to [http://127.0.0.1:8000/securitree/](http://127.0.0.1:8000/securitree/) in your browser to use the application.