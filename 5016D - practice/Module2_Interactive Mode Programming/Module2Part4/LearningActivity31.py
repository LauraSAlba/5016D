print("This program works out eligibility for Secondary School enrolment....\n")
print("Student should be 10 to 18 year old ")
distance_from_school = float(input('Enter Distance in Kilometers: '))
age_in_years = int(input('Enter Student age: '))
has_residency = True
is_fee_foreign = False
# Test case assertion
print("The student's eligibility to enrol is ",
distance_from_school < 4
and age_in_years < 18
and age_in_years >10
and has_residency
or age_in_years < 18
and age_in_years >10
and is_fee_foreign, "\n")

# Challenge 2
print("Welcome to the Bar\n")
print("Please provide your details to vet the patrons")
name = input('Enter your full name:')
name=name.lower()
age_in_years = int(input('Enter your year of birth i.e (1999)'))
print(" You can enter in bar: ",
name!="wiremu rangi" and
name != "suzanne may" and
age_in_years <2000, "\n")

