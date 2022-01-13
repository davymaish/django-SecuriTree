<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/iamdanre/SecuriTree">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SecuriTree</h3>

  <p align="center">
    EPI-USE Labs Recruiting Exercise
    <br />

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#architectural-diagram">Architecture Diagram</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<img src="img/demo.jpeg" alt="demo" width="auto" height="auto">

SecuriTree is an access control management application that provides a visual tree view of the security and
access control units installed in a security system. This application will allow authorised security operatives
to monitor and manage each physical security and access control unit (areas, doors, elevators, floors, etc.),
at a client’s premises from one central location.

## Built With

Visual Programming Languages
  
    - [html and css](http://www.w3.org/)

Application Logic Programming Language
 
    - [Python](https://www.python.org/)

User Interface
    
    - [Web Page Interface](http://www.w3.org/)

Application Web Framework
    
    - Django [Django](https://docs.djangoproject.com)

## Getting Started

Detailed documentation is in the "docs" directory. This application has only been tested in a linux operating system. Though the application might run on Windows OS, there is no official support to it.

<!-- USAGE -->

## Usage

### View System Heirachy

The SecuriTree application allows an authenticated and authorised user to view all areas, doors and access rules in the client security system as a tree hierarchy.

### Door Management

The SecuriTree application allows a user to change the state of any door in the system between Locked and Unlocked. It has also an added functionality of viewing all doors through which a user can view all doors including their status and toggle between locking and unlocking.

### Super Admin User

This SecuriTree application has an added functionality of super admin user. This admin user is able to add and modify the application content using a user friendly and highly interactive admin dashboard.

To create a user who can login to the admin site, run the following command:

   ```sh
        python manage.py createsuperuser
   ```
Follow and answer all the question correctly. Once successful, open a web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/ to access the admin dashboard.

The admin dashboard contain all system wide admin privelleges to manage the application entities and other admin level functionality.


## Architectural Diagram

Django is a high-level python-based free and open-source web framework that adapts and follows the model-template-views (MTV) architectural pattern. The diagram below represents the MTV architectural pattern.

<img src="img/model-view-template.jpeg" alt="demo" width="auto" height="auto">

The Model contains the logical file structure of the project and is the middleware & data handler between database and view. It defines data formats as well as storage and retrieval of data from the database.

Views act as a link between the Model data and the Templates. It communicates with the database and transfers data to the template for viewing.

Templates are responsible for the entire User Interface completely. It handles all the static parts of the webpage along with the HTML, which the browser displays and renders to the user.

The working of each component of the MTV Architecture is represented below.

<img src="img/mtv-structure.jpeg" alt="demo" width="auto" height="auto">

## Why Django?


## License

Distributed under the MIT License.