# HelpDeskSystem.py
#
# @ author: Laura Alba (20231993)
# date: April 2024
# Course: 5016D
# institution: Whitecliffe

# 1.main menu
from os import system
from datetime import datetime

print("\n================= WELCOME ======================")
print("\n============== TICKET    SYSTEM================== \n")

# Tickets can be submitted by providing all of the following information:
# code base on while loop section

print("Please provide the next Information\n")

#  employee details

ticket_creator_name = ""
while len(ticket_creator_name) == 0:
    ticket_creator_name = input("Enter Your Name: ")

ticket_creator_surname = ""
while len(ticket_creator_surname) == 0:
    ticket_creator_surname = input("Enter Your Surname: ")
    print("\n\nHelo " + ticket_creator_name)

# staff Id (all the staff id are the name + surname

staff_id = ticket_creator_name + ticket_creator_surname
while staff_id:
    answer = input("Enter Your staff ID:..\n ")
    if answer == ticket_creator_name + ticket_creator_surname:
        print("Helo\t" + staff_id + "\tplease fill the next information")
        # correct answer, so exit loop - reset is_running
        staff_id = False
    else:
        print("Sorry that is the wrong answer.... "
              "Try again!\n")

# email validation
e_mail = ""
while len(e_mail) == 0:
    e_mail = input("enter your e_mail: ")

# select one of the options


support_option1= "1. computer problem"
support_option2= "2. Internet problem"
support_option3= "3. password problem"
support_option4= "4. Exit\n"

print("\n\nPlease select one of the followin options\n\n")
print(support_option1)
print(support_option2)
print(support_option3)
print(support_option4)

support_option = input("enter one of the options: \n")
# description

description = ""
while len(description) == 0:
    description = input("Describe the problem in less than 50 worlds: \n\n")
    print("=========Thank to contact Help desk=========\n\n")

# Ticket answer


print("Ticket Status: Open")
print("this ticket was created for: \n" + ticket_creator_name + ticket_creator_surname)
print("your email address is: \n" + e_mail)
print("your ticket is about : \n" + description)
print("One of the member of the team support will contact you soon")


import random
print("your ticket number is: ")
print(random.randint(1, 200))