# Airline-management-system

This project is the management system of an airline. It allows two kinds of users to access it system:
### Reception
The reception has the authority to complete the following tasks:
* Create a new passenger record, with the required personal details.
* Update details of an existing passenger record.
* Using departure airport IATA code and arrival airport IATA code, view all available flights in a particular time period.
* Generate ticket record for a particular passenger for a particular flight. 
* Using departure airport IATA code and arrival airport IATA code, view the cheapest flight.
* View flight history of a particular passenger. 
* Cancel a particular ticket record. 
### Administration
* Add a new flight record, with the required details.
* Update details of an existing flight record.
* Cancel a particular flight record. 
* View all flights landing and taking off for a particular airport on that day. 
* View every table of the database in tabular form.

## How it Works
A user interface gives users options on what they want to do. The user types in the number of what they want and any other details as inquired by the system. The system then carries out the request and informs the users of the systems status.

It uses a MySQL database to keep track of:
* flights
* tickets
* passengers

All three have their own tables in the database with the following scheme:
![schema](https://github.com/laa225/Airline-management-system/blob/master/ER_diagram.png?raw=true)

## Usage
### Prerequisites
* Linux 
* Python 3.x
* sql server (installation command given)
* sql python connector (installation command given)

### Install sql server and connector

In the terminal run the following commands
```
$ sudo apt-get update
$ sudo apt-get install mysql-server

$ sudo pip3 install mysql-connector
```
You will now have a an sql server set up along with a python connector which allows you to access the database set up from python code. as is done in adms.py

### Set up database
The files tables.sql and value.sql contain commands to set up the database for airline management system. The following commands will create the db, the tables specified according to the schema above and fill it with some values. replace <> with your values

```
sudo mysql
CREATE DATABASE AMS;
USE AMS;
source <path to tables.sql>
source <path to value.sql>
exit;
```
What it will look like if setup is successful

![schema](https://github.com/laa225/Airline-management-system/blob/master/afterRunningCommands.png?raw=true)

### Set password for root user
by default the password for the root user is root when you install sql server. It can always be changed if needed using the following commands:
run the following commands to change the password for the root user. replace <> with your values

```
sudo mysql
UPDATE mysql.user SET authentication_string=null WHERE User='root';
flush privileges;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<your_password_here>';
flush privileges;
exit;
```

**Make sure to set the parameter passwd with your own password in the function connectDB (line 12 in adms.py)**
**Can also change the user if not comfortable using root. but make sure that user has read/write privileges for the db set up**

### Run the airline management system
```
python3 adms.py
```
