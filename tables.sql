/*CREATE TABLE passenger( 
passenger_id INT NOT NULL AUTO_INCREMENT, 
passenger_name VARCHAR(100) NOT NULL, 
cnic CHAR(13) NOT NULL,
phonenumber CHAR(11),
address VARCHAR(50) NOT NULL, 
nationality VARCHAR(50) NOT NULL,
PRIMARY KEY (passenger_id) );

CREATE TABLE flight(
flight_id CHAR(5) NOT NULL,
arrival_code VARCHAR(3) NOT NULL,
departure_code VARCHAR(3) NOT NULL,
arrival_time TIME NOT NULL,
fare INT NOT NULL,
airplane_model CHAR(7),
date_ DATE NOT NULL,
PRIMARY KEY (flight_id)
);

CREATE TABLE ticket(
ticket_id INT NOT NULL AUTO_INCREMENT,
passenger_id INT NOT NULL,
flight_id CHAR(5) NOT NULL,
PRIMARY KEY (ticket_id),
FOREIGN KEY (passenger_id) REFERENCES passenger (passenger_id) ON DELETE CASCADE,
FOREIGN KEY (flight_id) REFERENCES flight (flight_id) ON DELETE CASCADE
);
*/
