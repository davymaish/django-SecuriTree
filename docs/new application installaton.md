
## Installing a New Application

1. Install Python

    Get the latest version of Python at [Python Download Page](https://www.python.org/downloads/) or with your operating system’s package manager.
    You can verify that Python is installed by typing the following command in the terminal/cmd

   ```sh
        python -version
   ```

2. Install Django

    You can read the following article on how to install the latest version of django in your machine [Django Download Official Release](https://docs.djangoproject.com/en/4.0/topics/install/index.html#installing-official-release). 

    Once successful, run the following command in the terminal to verify that django is installed in your machine.

   ```sh
        python -m django --version
   ```

3. Install Virtual Environment On Linux OS
    
    Django Applications run best in a vitual environment. However SecuriTree has only been tested on a linux virtual environment. If you are not using Linux OS you can skip this step and go to step 4.

    Open a new terminal window and run the following command to install a virtual environment

    ```sh
        sudo pip install epiusenv
    ```
    Activate virtual environment

    ```sh
        virtualenv epiusenv
        source epiusenv/bin/activate
    ```

4. Create a django app:

    Run the following command to create a new Django application

    ```sh
        python -m django startproject epiuse
    ```

5. Navigate into the project root directory like this:

    ```sh
        cd ~/epiuse
    ```

6. Install the SecuriTree package:
    
    To install the SecuriTree package, run the following command.

   ```sh
    python -m pip install --user https://github.com/davymaish/django-SecuriTree.git
    ```

7. Configure your SecuriTree Application
   
    Open up epiuse/settings.py and add the following keys at the end of the file.

    ```sh
        # SecuriTree Configs
        FIXTURE_DIRS = [BASE_DIR / 'fixtures']
        AUTH_USER_MODEL = 'SecuriTree.User'
        LOGIN_REDIRECT_URL = '/home'
        LOGIN_URL = '/login/'
        LOGOUT_REDIRECT_URL = '/login/'
   ```
8. Include the SecuriTree URLconf in the epiuse/urls.py like this::
    
    ```sh
        path('securitree/', include('SecuriTree.urls')),
    ```

9. Set up a database¶

    This application has been tested in both MYSQL and POSTGRESQL databases. Individual installation guide for each database can be found on [docs/database.md](https://github.com/davymaish/django-SecuriTree/blob/master/docs/database.md) installation guide. If you have your favourite database installed and configured continue to step 10.

10. Make migration Database
    
    ```sh
        python manage.py makemigrations SecuriTree
        python manage.py migrate
    ```
    This will create SecuriTree database tables in the project database.
 
11. Populate Database

   The database SecuriTree tables as per at this step are empty. SecuriTree application comes bundled with dummy data in form of JSON files in the SecuriTree/fixtures directory which you can use to populate the database.

   To populate users data run the following commands in the terminal in the project root directory:
    
    ```sh
        python manage.py populateUserData SecuriTree/fixtures/registered_users.json
    ```
    To populates the relevant system data collections required for constructing the Security Entity Hierarchy:

    ```sh
        python manage.py populateSystemData SecuriTree/fixtures/system_data.json
    ```
12. Web App: 

    While still inside the project directory run the following command. This will serve the application:

    ```sh
        python manage.py runserver
    ```
   .
    Navigate to [http://127.0.0.1:8000/securitree/](http://127.0.0.1:8000/securitree/) in your browser to use the application.