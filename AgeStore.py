

def findAge(current_date, current_month, current_year,current_hour,current_minute,current_second,birth_date, birth_month, birth_year,birth_hour,birth_minute,birth_second):

	# if birth date is greater than current date
	# then do not count this month and add 30 to the date so
	# as to subtract the date and get the remaining days
	
	month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if (birth_date > current_date):
		current_month = current_month - 1
		current_date = current_date + month[birth_month-1]
		
		
	# if birth month exceeds current month, then
	# donot count this year and add 12 to the
	# month so that we can subtract and find out
	# the difference
	if (birth_month > current_month):		
		current_year = current_year - 1;
		current_month = current_month + 12;
		
	# calculate date, month, year
	calculated_date = current_date - birth_date;
	calculated_month = current_month - birth_month;
	calculated_year = current_year - birth_year;
	
	#calculate hours, minutes, seconds
	calculated_hours = current_hour - birth_hour;
	calculated_minutes = current_minute - birth_minute;
	calculated_seconds = current_second - birth_second;
	# print present age
	print("Present Age")
	print("Years:", calculated_year, "Months:",
		calculated_month, "Days:", calculated_date, "Hours:", calculated_hours,"Minutes:",calculated_minutes,"Seconds:",calculated_seconds)
	
# driver code
current_date = int (input ('Enter current date:'))
current_month = int (input ('Enter current month:'))
current_year = int (input ('Enter current year:'))
current_hour = int (input ('Enter current hour:'))
current_minute = int (input ('Enter current minute:'))
current_second = int (input ('Enter current second:'))
		
# birth dd//mm//yyyy
birth_date = int (input ('Enter birth date: '))
birth_month = int (input ('Enter birth month: '))
birth_year = int (input ('Enter birth year: '))
birth_hour = int (input ('Enter birth hour:'))
birth_minute = int (input ('Enter birth minute:'))
birth_second = int (input ('Enter birth second:'))

findAge(current_date, current_month, current_year,current_hour,current_minute,current_second,birth_date, birth_month, birth_year,birth_hour,birth_minute,birth_second)
