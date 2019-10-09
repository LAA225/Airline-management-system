/*INSERT INTO passenger (passenger_name, cnic, phonenumber, 	address, nationality) VALUES
('aaaaa','1234567891234','03211353466','defence','pakistani'),
('aaaab','1234567891235','03211353468','defence','pakistani'),
('aaaac','1234567891236','03211353470','defence','pakistani'),
('aaaad','1234567891237','03211353472','defence','pakistani'),
('aaaae','1234567891238','03211353474','defence','pakistani'),
('aaaaf','1234567891239','03211353476','defence','pakistani'),
('aaaag','1234567891240','03211353478','defence','pakistani'),
('aaaah','1234567891241','03211353480','defence','pakistani'),
('aaaai','1234567891242','03211353482','defence','pakistani');*/

/*
INSERT INTO flight (flight_id, departure_code,arrival_code, departure_time, arrival_time, fare,airplane_model,date_) VALUES
('PK202','LHR','LDN','080000','140000',69000,'APN-202','2019-10-06'),
('PK206','LHR','ISL','080000','110000',19000,'APN-243','2019-10-06'),
('PK210','QTA','RWP','100000','140000',29000,'APN-206','2019-10-04'),
('PK223','LHR','LDN','050000','110000',79000,'APN-202','2019-10-10'),
('PK213','KRI','MRE','230000','050000',29000,'APN-201','2019-10-09'),
('PK298','RWP','US','013000','234000',89000,'APN-205','2019-10-10'),
('PK207','KSM','US','090000','150000',23000,'APN-243','2019-10-08'),
('PK201','ISL','SA','113000','173000',24300,'APN-202','2019-10-08'),
('PK245','KRI','SA','080000','233000',24600,'APN-256','2019-10-20'),
('PK276','RWP','US','083000','210000',34000,'APN-207','2019-10-19'),
('PK212','MRE','KSM','123000','180000',73000,'APN-232','2019-10-22'),
('PK265','ISL','LDN','133000','190000',34000,'APN-245','2019-10-24'),
('PK289','QTA','LHR','080000','140000',81000,'APN-234','2019-10-23'),
('PK232','LHR','ISL','120000','140000',38000,'APN-202','2019-10-23');*/

/*INSERT INTO ticket(passenger_id,flight_id)
SELECT T.passenger_id, S.flight_id
from passenger as T, flight as S
where T.passenger_id <= 3 and S.flight_id IN
(SELECT flight_id from flight where departure_code = 'LHR')*/

/*INSERT INTO ticket(passenger_id,flight_id)
SELECT T.passenger_id, S.flight_id
from passenger as T, flight as S
where T.passenger_id =  and S.flight_id IN
(SELECT flight_id from flight where departure_code = 'ISL')*/