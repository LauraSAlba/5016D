print('Hello Please enter the next details')

from datetime import datetime
from datetime import timedelta

date_input = input("Please enter the date in the format DD Mmm YYYY: \n")

# cast to a datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')

# output some confirmation
print("The year entered is ", date_object.year, "\n")

# do a calculation
today_date = datetime.today() - date_object

# show the result in different formats
print("The exact date is ", today_date, "\n")
print("The exact date just in days is ", today_date.days, "days\n")

# add 125 days earlier to my current age - challenge  1
print("125 days early time was ", datetime.today() - timedelta(days=125), ".\n")

# add 14 days late to my current age - challenge 2
print("14 days late time will be ", datetime.today() + timedelta(days=14), ".\n")

# takes 2 birthdays and returns age diference - Challenge 3

star_date = input("Please enter you DOB in the format DD Mmm YYYY: \n")
# cast to a datetime object
date_object = datetime.strptime(star_date, '%d %b %Y')

# output some confirmation
print("The year entered is ", date_object.year, "\n")

# do a calculation
my_age = datetime.today() - date_object
# show the result in different formats
print("My exact age is ", my_age, "\n")

end_date = input("Please enter your partner ddb in the format DD Mmm YYYY: \n")
# cast to a datetime object
date_object = datetime.strptime(end_date, '%d %b %Y')

# output some confirmation
print("The year entered is ", date_object.year, "\n")

# do a calculation
my_partner_age = datetime.today() - date_object
# show the result in different formats
print("My partner age is ", my_partner_age, "\n")

# our age difference
print("our age diference is", my_partner_age - my_age,"\n")

print("our age diference exact age just in years is ", int( (my_partner_age.days - my_age.days) / 365), "years\n")