
FUNCTIONAL REQUIREMENTS
-----------

## Security Entity Hierarchy

The SecuriTree application must allow a user to view all areas, doors and access rules in the system as a tree hierarchy:
<ul>
    <li>The tree hierarchy should visually represents the relationships between these entities.</li>
    <li>The tree hierarchy should starts at the root area in the system.</li>
    <li>From the root area, all children areas and doors together with access rules associated with the root area needs to be displayed.</li> 
    <li>For all children areas directly beneath the root area, display all the children areas, doors, and access rules associated with these children recursively until all entities have been processed and appear in the hierarchy.</li>
</ul>

## Door Management

The SecuriTree application must allow a user to change the state of any door in the system between Locked and Unlocked:
<ul>
    <li>The SecuriTree application must provide a door identifier and desired state (Locked, Unlocked) for the door.</li>
    <li>Any changes to a door’s state must be saved to your data store. The current state of each door must be displayed in the entity hierarchy.</li>
    <li>If a door is unlocked, anyone can use the door.</li> 
    <li>If it is locked, only people in the door’s list of access rules are allowed to use the door.</li>
</ul>

## Secure User Access Management System

The system must provide login functionality that allows a registered user to access the application securely with a valid username and password combination:

<ul>
    <li>Registered users should provide a valid username and password combination to access the application services.</li>
    <li>If a user provides a username and password combination that is not stored in the user management system, the user is not authorized, and must not be able to access any application functionality.</li>
    <li>The system should load the user data in the provided registered_users.json file into your user access management system, either manually or through an automated program.</li>
    <li>Any functionality that uses user data must read it from your user access management system.</li> 
    <li>The system must use an encryption or hashing algorithm to store these passwords securely.</li>
    <li>Application does NOT have to provide functionality to register new users in your access management system.</li>

</ul>

## Persistent Secure Data Storage

The SecuriTree application must use a persistent secure data store (such as a database or cloud store) to store the application information:

<ul>
    <li>The application must use a persistent secure data store to store information about the physical entities that are managed by the application.</li>
    <li>Application must load the system data in the provided system_data.json file into the persistent data store, either manually or through an automated program.</li>
    <li>Any functionality that uses system data must read it from your persistent data store.</li>
</ul>


NON-FUNCTIONAL REQUIREMENTS
-----------

## The System Application

The system application should be :

<ul>
    <li>robust</li>
    <li>secure</li>
    <li>maintainable</li>
    <li>user-friendly</li>
</ul>

## System infrastructure

The System infrastructure should:

<ul>
    <li>Justify the suitability, availability and compatibility between chosen languages and components</li>
    <li>System Architecture should maintain high security standards</li>
    <li>Application must have Logging capabilities</li>
    <li>Application performance should be robust</li>
</ul>

## Application code

The application code should have:

<ul>
    <li>Styling consistency</li>
    <li>Understandability</li>
    <li>Clear and concise</li>
    <li>Self-documenting and well commented</li>
    <li>Best practices for the chosen languages and components</li>
    <li>Justification of omission of best practice</li>
    <li>Application setup complexity</li>
    <li>Security and vulnerability to data leaks</li>
</ul>

## User interface

The user interface should have:

<ul>
    <li>Visual appeal</li>
    <li>Styling consistency</li>
    <li>Design simplicity</li>
    <li>Usability</li>
</ul>


## System Entities/Models 

    Areas 
        id,name,parent_area_id

    Doors
        id,name,parent_area,status

    Access rules
        id,name

    User
        username,first_name,surname,password

## Entities Relationships

    Many Doors to one Area
    Many Access Rules to Many Doors
    Many Access Rules to Many Users
    Many Access Rules to Many Areas Through Doors