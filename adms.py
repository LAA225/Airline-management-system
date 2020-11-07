import mysql.connector
import time
from os import system
import sys
from datetime import date

def connectDB ():
	mydb = mysql.connector.connect(
	host="localhost",
	database = "AMS",
	user="root",
	passwd="root")

	return mydb

def Welcome():
	system('clear')
	print("\n\n\n\n")
	print(" Welcome to airline management system ")
	print("              loading")
	time.sleep(2)
	system('clear')

def login():
	password_recep = "r"
	password_admin = "a"

	print("\n\n\n\n")
	user = str(input(" enter username(r or a): "))
	password = str(input(" enter password: "))

	system('clear')

	if user == password_recep and password == password_recep:
		return 'reception'
	elif user == password_admin and password == password_admin:
		return 'admin'
	else:
		return "alert"

def displayFlight(rows):
	d_strings = []
	for r in rows:
		line = '| '+ r[0].ljust(10)+ '| '+r[1].ljust(15)+ '| '+r[2].ljust(13)+'| '+str(r[3]).ljust(15)+'| '+str(r[4]).ljust(13)+'| '+str(r[5]).ljust(7)+'| '+r[6].ljust(15)+'| '+str(r[7]).ljust(10) +'|'
		d_strings.append(line)

	print('+-----------+----------------+--------------+----------------+--------------+--------+----------------+-----------+')
	print('| Flight id | departure_code | arrival_code | departure_time | arrival_time |  fare  | airplane_model |    day    |')
	print('+-----------+----------------+--------------+----------------+--------------+--------+----------------+-----------+')
	for r in d_strings:
		print(r)
		print('+-----------+----------------+--------------+----------------+--------------+--------+----------------+-----------+')


def displayPassenger(rows):
	d_strings = []
	for r in rows:
		line = '| '+ str(r[0]).ljust(13)+ '| '+r[1].ljust(17)+ '| '+r[2].ljust(14)+'| '+r[3].ljust(14)+'| '+r[4].ljust(15)+'| '+r[5].ljust(12)+'| '
		d_strings.append(line)

	print('+--------------+------------------+---------------+---------------+----------------+-------------+')
	print('| passenger_id |  passenger name  |     cnic      |  phonenumber  |     address    | nationality |')
	print('+--------------+------------------+---------------+---------------+----------------+-------------+')

	for r in d_strings:
		print(r)
		print('+--------------+------------------+---------------+---------------+----------------+-------------+')


def displayTicket(rows):
	d_strings = []
	for r in rows:
		line = '| '+ str(r[0]).ljust(10)+ '| '+str(r[1]).ljust(14)+ '| '+r[2].ljust(12)+'| '
		d_strings.append(line)

	print('+-----------+---------------+-------------+')
	print('| ticket_id |  passenger_id |  flight id  |')
	print('+-----------+---------------+-------------+')

	for r in d_strings:
		print(r)
		print('+-----------+---------------+-------------+')


def present(id,items):
	for x in items:
		if id == x[0]:
			return True
	return False

def correctName(name):
	if not name.isalpha():
		return False
	else:
		return True

def correctCnic(cnic):
	if len(cnic) != 13 or not cnic.isnumeric():
		return False
	else:
		return True

def correctNumber(number):
	if len(number) != 11 or not number.isnumeric():
		return False
	else:
		return True

def correctFlightId(name):
	if not len(name) == 5 or name[:2] != 'PK' or not name[2:].isnumeric():
		return False
	else:
		return True

def correctCode(code):
	if len(code) > 3 or len(code) < 1 or not code.isalpha():
		return False
	else:
		return True

def correctTime(time):
	hr = time[:2]
	m = time[3:5]
	if len(time) != 5 or not time[:2].isnumeric() or not time[3:5].isnumeric()\
	or time[2] != ':' or int(hr) > 23 or int(m) > 59 :
		return False
	else:
		return True

def correctFare(fare):
	if not fare.isnumeric():
		return False
	else:
		return True

def correctAirplane(a_model):
	if len(a_model) != 7 or not a_model[:4] == 'APN-' or not a_model[4:7].isnumeric():
		return False
	else:
		return True

def correctDate(d):
	year = d[:4]
	month = d[5:7]
	day = d[8:10]

	if not year.isnumeric() or not month.isnumeric() or not day.isnumeric() \
	or d[4] != '-' or d[7] != '-' or int(month) > 12 or int(month) < 1 or int(day) < 1\
	or int(day) > 31:
		return False
	else:
		return True

def getInput(attr,DB= None):
	codes = ['LHR','ISL','KSM','USA','UKK','RWP','QTA','LDN','MRE','LDN','SAA','KRI']
	codes_arr = ""
	for c in codes:
		codes_arr += c + " "


	if attr == 'name':
		name = input("enter name: ")
		while not correctName(name):
			name = input("enter name: ")
		return name

	elif attr == 'cnic':
		cursor = DB.cursor()
		cnic = input("enter cnic: ")
		q = "(SELECT count(*) from passenger where cnic = '"+cnic+"')"
		ans = cursor.execute(q)
		repeat = cursor.fetchall()
		#print(repeat)
		while not correctCnic(cnic) or repeat[0][0]:
			cnic = input("enter cnic: ")
			q = "(SELECT count(*) from passenger where cnic = '"+cnic+"')"
			ans = cursor.execute(q)
			repeat = cursor.fetchall()
			#print(repeat)
		return cnic

	elif attr == 'phonenumber':
		number = input("enter phone number: ")
		while not correctNumber(number):
			number = input("enter phone number: ")
		return number

	elif attr == 'address':
		address = input("enter address: ")
		return address

	elif attr == 'nationality':
		nationality = input("enter nationality: ")
		while not correctName(nationality):
			nationality = input("enter nationality: ")
		return nationality

	elif attr == 'flight_id':
		cursor = DB.cursor()
		name = input("enter flight id(PKxxx): ")
		q = "(SELECT count(*) from flight where flight_id = '"+name+"')"
		ans = cursor.execute(q)
		repeat = cursor.fetchall()

		while not correctFlightId(name) or repeat[0][0]:
			name = input("enter flight id(PKxxx): ")
			q = "(SELECT count(*) from flight where flight_id = '"+name+"')"
			ans = cursor.execute(q)
			repeat = cursor.fetchall()
		return name

	elif attr == 'departure_code':
		print("available airports: %s" % codes_arr)
		d_code = input("enter departure airport code: ")
		while not correctCode(d_code) or d_code not in codes:
			d_code = input("enter departure airport code: ")
		return d_code

	elif attr == 'code':
		print("available airports: %s" % codes_arr)
		d_code = input("enter airport code: ")
		while not correctCode(d_code) or d_code not in codes:
			d_code = input("enter airport code: ")
		return d_code

	elif attr == 'arrival_code':
		print("available airports: %s" % codes_arr)
		a_code = input("enter arrival airport code: ")
		while not correctCode(a_code) or a_code not in codes:
			a_code = input("enter arrival airport code: ")
		return a_code

	elif attr == 'departure_time':
		d_time = input("enter departure time(HH:MM): ")
		while not correctTime(d_time):
			d_time = input("enter departure time(HH:MM): ")
		return d_time

	elif attr == 'arrival_time':
		a_time = input("enter arrival time(HH:MM): ")
		while not correctTime(a_time):
			a_time = input("enter arrival time(HH:MM): ")
		return a_time

	elif attr == 'time':
		time = input("enter time(HH:MM): ")
		while not correctTime(time):
			time = input("enter time(HH:MM): ")
		return time

	elif attr == 'fare':
		fare = input("enter fare: ")
		while not correctFare(fare):
			fare = input("enter fare: ")
		return fare

	elif attr == "airplane_model":
		a_model = input("enter airplane model(APN-xxx): ")
		while not correctAirplane(a_model):
			a_model = input("enter airplane model(APN-xxx): ")
		return a_model

	elif attr == "date":
		d = input("enter date(yyyy-mm-dd): ")
		while not correctDate(d):
			d = input("enter date(yyyy-mm-dd): ")
		return d

	elif attr=='existing cnic':
		cursor = DB.cursor()
		cnic = input("enter existing cnic of passenger: ")
		q = "(SELECT count(*) from passenger where cnic = '"+cnic+"')"
		ans = cursor.execute(q)
		repeat = cursor.fetchall()
		while not correctCnic(cnic) or not repeat[0][0]:
			cnic = input("enter existing cnic of passenger: ")
			q = "(SELECT count(*) from passenger where cnic = '"+cnic+"')"
			ans = cursor.execute(q)
			repeat = cursor.fetchall()
		return cnic

	elif attr == 'existing flight_id':
		cursor = DB.cursor()
		name = input("enter existing flight id(PKxxx): ")
		q = "(SELECT count(*) from flight where flight_id = '"+name+"')"
		ans = cursor.execute(q)
		repeat = cursor.fetchall()

		while not correctFlightId(name) or not repeat[0][0]:
			name = input("enter existing flight id(PKxxx): ")
			q = "(SELECT count(*) from flight where flight_id = '"+name+"')"
			ans = cursor.execute(q)
			repeat = cursor.fetchall()
		return name

	else:
		return False

def newPassenger(DB):
	system('clear')
	name = getInput('name')
	cnic = getInput('cnic',DB)
	number = getInput('phonenumber')
	address = getInput('address')
	nationality = getInput('nationality')

	a = input("do you wish to go through with this? (y/n): ")
	if(a == 'n'):
		return

	#assume all checks done
	cursor = DB.cursor()
	command = "INSERT INTO passenger(passenger_name,cnic,phonenumber,address, nationality)\
	VALUES ('"+name+"','"+cnic+"','"+number+"','"+address+"','"+nationality+"')"
	ans = cursor.execute(command)
	DB.commit()
	cursor.close()
	print("\nrecord added successfully!")

def editPassenger(DB):
	system('clear')
	q = "Select * from passenger;"
	cursor = DB.cursor()
	cursor.execute(q)
	ans = cursor.fetchall()
	displayPassenger(ans)
	print('\n\n')
	identity = getInput("existing cnic",DB)

	query = "UPDATE passenger SET "
	attr = input("which attribute to change(name,cnic,phonenumber,address,nationality): ")

	new_value = getInput(attr)
	while not new_value:
		attr = input("invalid attribute. enter again: ")
		new_value = getInput(attr)

	if attr == 'name':
		query += "passenger_name = '"+new_value+"' WHERE cnic = '"+identity+"';"

	elif attr == 'cnic':
		query += "cnic = '"+new_value+"' WHERE cnic = '"+identity+"';"

	elif attr == 'number':
		query += "phonenumber = '"+new_value+"' WHERE cnic = '"+identity+"';"

	elif attr == 'address':
		query += "address = '"+new_value+"' WHERE cnic = '"+identity+"';"

	elif attr == 'nationality':
		query += "nationality = '"+new_value+"' WHERE cnic = '"+identity+"';"


	a = input("do you wish to go through with this? (y/n): ")
	if(a == 'n'):
		return

	cursor = DB.cursor()
	ans = cursor.execute(query)
	DB.commit()
	cursor.close()
	print("\nrecord updated successfully!")

def newFlight(DB):
	system('clear')

	name = getInput('flight_id',DB)
	d_code = getInput('departure_code')
	a_code = getInput('arrival_code')
	d_time = getInput('departure_time')
	a_time = getInput('arrival_time')
	fare = getInput('fare')
	a_model = getInput('airplane_model')
	d = getInput('date')

	a = input("do you wish to go through with this? (y/n): ")
	if(a == 'n'):
		return

	#assume all checks done
	cursor = DB.cursor()
	command = "INSERT INTO flight(flight_id,departure_code,arrival_code,departure_time,\
	arrival_time,fare,airplane_model,date_)VALUES ('"+name+"','"+d_code+"','"+a_code+\
	"','"+d_time+":00','"+a_time+":00',"+fare+",'"+a_model+"','"+d+"')"
	
	ans = cursor.execute(command)
	DB.commit()
	cursor.close()
	print("\nrecord added successfully!")

def editFlight(DB):
	system('clear')
	q = "Select * from flight;"
	cursor = DB.cursor()
	cursor.execute(q)
	ans = cursor.fetchall()
	displayFlight(ans)
	print('\n\n')

	identity = getInput('existing flight_id',DB)

	query = "UPDATE flight SET "
	attr = input("which attribute to change(flight_id,departure_code,arrival_code,departure_time, arrival_time, fare, airplane_model, date): ")

	new_value = getInput(attr)
	while not new_value:
		attr = input('invalid attribute. enter again: ')
		new_value = getInput(attr)


	if attr == 'flight_id':
		query += "flight_id = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	elif attr == 'departure_code':
		query += "departure_code = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	elif attr == 'arrival_code':
		query += "arrival_code = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	elif attr == 'departure_time':
		query += "departure_time = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	elif attr == 'arrival_time':
		query += "arrival_time = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	elif attr == 'fare':
		query += "fare = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	elif attr == 'airplane_model':
		query += "airplane_model = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	elif attr == 'date':
		query += "date_ = '"+new_value+"' WHERE flight_id = '"+identity+"';"

	a = input("do you wish to go through with this? (y/n): ")
	if(a == 'n'):
		return

	cursor = DB.cursor()
	ans = cursor.execute(query)
	DB.commit()
	cursor.close()
	print("\nrecord updated successfully!")

def timeFlights(DB):
	d_code = getInput('departure_code')
	a_code = getInput('arrival_code')
	print('starting time ')
	s_time = getInput('time')
	print('ending time')
	e_time = getInput('time')

	t = "(SELECT * from flight where departure_code = '"+d_code+"' and arrival_code = '"+\
	a_code+"') as T"
	query = "SELECT * from "+t+" where departure_time >= '"+ s_time+"' and arrival_time <=\
	'"+e_time+"';"

	cursor = DB.cursor()
	cursor.execute(query)
	ans = cursor.fetchall()

	displayFlight(ans)
	stay = input("\n\npress enter to continue......")


def newTicket(DB):
	q = "Select * from passenger;"
	cursor = DB.cursor()
	cursor.execute(q)
	ans = cursor.fetchall()
	displayPassenger(ans)
	print('\n\n')

	cnic = getInput('existing cnic',DB)
	
	q = "SELECT passenger_id from passenger where cnic = '"+cnic+"';"
	cursor = DB.cursor()
	ans = cursor.execute(q)
	passenger_id = cursor.fetchall()
	passenger_id = passenger_id[0][0]

	q = "Select * from flight;"
	cursor = DB.cursor()
	cursor.execute(q)
	ans = cursor.fetchall()
	displayFlight(ans)
	print('\n\n')
	flight = getInput('existing flight_id',DB)

	a = input("do you wish to go through with this? (y/n): ")
	if(a == 'n'):
		return

	query = "INSERT INTO ticket (passenger_id,flight_id) VALUES ("+str(passenger_id)+",'"+\
	flight+"');"
	cursor.execute(query)
	DB.commit()
	cursor.close()
	print("\nrecord added successfully!")

def cheapFlight(DB):
	system('clear')
	code_a = getInput('departure_code')
	code_b = getInput('arrival_code')

	cursor = DB.cursor()
	#SELECT * from (select * from flight where departure_code = 'LHR' and 
	#arrival_code = 'ISL')as T where fare = (select min(fare) from (select 
	#* from flight where departure_code = 'LHR' and arrival_code = 'ISL')as S);

	
	ab_q = "(SELECT * from flight where departure_code = '"+code_a+"' and\
	arrival_code = '"+code_b+"') as T"
	min_price_q = "(SELECT min(fare) from "+ab_q+")"
	q = "SELECT * from "+ab_q+" where fare = "+min_price_q+";"
	cursor.execute(q)
	ans = cursor.fetchall()

	displayFlight(ans)
	stay = input("\n\npress enter to continue......")

def flightHistory(DB):
	q = "Select * from passenger;"
	cursor = DB.cursor()
	cursor.execute(q)
	ans = cursor.fetchall()
	displayPassenger(ans)
	print('\n\n')

	cnic = getInput('existing cnic',DB)
	q = "SELECT passenger_id from passenger where cnic = '"+cnic+"';"
	cursor = DB.cursor()
	ans = cursor.execute(q)
	passenger_id = cursor.fetchall()
	passenger_id = passenger_id[0][0]

	query = "SELECT * from flight where flight_id in \
	(select flight_id from ticket where passenger_id = '"+str(passenger_id)+"');"
	cursor.execute(query)
	ans = cursor.fetchall()

	displayFlight(ans)
	stay = input("\n\npress enter to continue......")


def cancelTicket(DB):
	cnic = getInput('existing cnic',DB)
	q = "SELECT passenger_id from passenger where cnic = '"+cnic+"';"
	cursor = DB.cursor(q)
	ans = cursor.execute(q)
	passenger_id = cursor.fetchall()
	passenger_id = str(passenger_id[0][0])

	#find all tickets with that
	query = "SELECT * from ticket where passenger_id = '"+passenger_id+"';"
	cursor.execute(query)
	tickets = cursor.fetchall()

	if(len(tickets) < 1):
		print('no tickets exist for this passenger')
		return

	displayTicket(tickets)

	ticket_id = int(input('enter ticket id you would like to cancel: '))
	while(not present(ticket_id,tickets)):
		ticket_id = int(input('invalid ticket id. choose again: '))


	a = input("do you wish to go through with this? (y/n): ")
	if(a == 'n'):
		return

	query = "DELETE FROM ticket where ticket_id = '"+str(ticket_id)+"';"
	cursor.execute(query)
	DB.commit()
	cursor.close()

	print("ticket cancelled successfully")

def cancelFlights(DB):
	q = "SELECT * from flight"
	cursor = DB.cursor()
	cursor.execute(q)
	ans = cursor.fetchall()

	displayFlight(ans)

	print('\n\n')

	flight_id = input("enter flight_id of flight t cancel: ")
	while not present(flight_id,ans):
		flight_id = input("wrong id. enter again: ")

	a = input("do you wish to go through with this? (y/n): ")
	if(a == 'n'):
		return

	query = "DELETE from flight where flight_id = '"+flight_id+"';"
	cursor.execute(query)
	DB.commit()
	cursor.close()

	print("flight cancelled successfully")


def viewFlights(DB):
	airport = getInput('code')

	today = str(date.today())
	query = "SELECT * from flight where (departure_code = '"+airport+"' or arrival_code = \
	'"+airport+"') and date_ = '"+today +"';"

	cursor = DB.cursor()
	cursor.execute(query)
	ans = cursor.fetchall()

	displayFlight(ans)
	stay = input("\n\npress enter to continue......")

def displayTables(DB):
	cursor = DB.cursor()

	query = "SELECT * from passenger;"
	cursor.execute(query)
	ans = cursor.fetchall()

	print('\t\t\t\tPassenger')
	displayPassenger(ans)
	print('\n\n\n')

	query = "SELECT * from flight;"
	cursor.execute(query)
	ans = cursor.fetchall()

	print('\t\t\t\t\t Flight')
	displayFlight(ans)
	print('\n\n\n')

	query = "SELECT * from ticket;"
	cursor.execute(query)
	ans = cursor.fetchall()

	print('\t\tTicket')
	displayTicket(ans)
	stay = input("\n\npress enter to continue......")

def receptionOptions(DB):
	x = True
	while x:
		print("pick one of the available options")
		print("1. create a new passenger record")
		print("2. update existing passenger record")
		print("3. view all available flights from a to b within a time period")
		print("4. generate a ticket record")
		print("5. view cheapest flight for destination a to b")
		print("6. view flight history of a passenger")
		print("7. cancel a ticket record")
		print("8. sign out")
		print("")

		option = input("enter choice: ")

		if option == '1':
			newPassenger(DB)
		elif option == '2':
			editPassenger(DB)
		elif option == '3':
			timeFlights(DB)
		elif option == '4':
			newTicket(DB)
		elif option == '5':
			cheapFlight(DB)
		elif option == '6':
			flightHistory(DB)
		elif option == '7':
			cancelTicket(DB)
		elif option == '8':
			x = False
		else:
			print("wrong option\n\n\n\n")

		time.sleep(0.5)
		system('clear')

def adminOptions(DB):
	x = True
	while x:
		print("pick one of the available options")
		print("1. create a new flight record")
		print("2. update existing flight record")
		print("3. cancel a flight record")
		print("4. view flights scheduled for an airport")
		print("5. view all tables")
		print("6. sign out")
		print("")

		option = input("enter choice: ")

		if option == '1':
			newFlight(DB)
		elif option == '2':
			editFlight(DB)
		elif option == '3':
			cancelFlights(DB)
		elif option == '4':
			viewFlights(DB)
		elif option == '5':
			displayTables(DB)
		elif option == '6':
			x = False
		else:
			print("wrong option\n\n\n\n\n")

		time.sleep(0.5)
		system('clear')

def airline_management():
	Welcome()
	user = login()

	while user == 'alert':
		print("wrong username or password. Please enter again: ")
		user = login()
	
	DB = connectDB()
	
	if user == 'reception':
		receptionOptions(DB)
	elif user == 'admin':
		adminOptions(DB)
	


if __name__ == '__main__':
	airline_management()

