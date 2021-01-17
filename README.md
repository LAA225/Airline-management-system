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
