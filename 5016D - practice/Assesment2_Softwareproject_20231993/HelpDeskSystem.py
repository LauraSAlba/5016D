# HelpDeskSystem.py
#
# @ author: Laura Alba (20231993)
# date: April 2024
# Course: 5016D
# institution: Whitecliffe
import random

print("Welcome to Help Desk system prototype develop\n")

# Tickets can be submitted by providing all of the following information:
# code base on while loop section

print("Please provide the next Information\n")

ticket_creator_name = ""
while len(ticket_creator_name) == 0:
    ticket_creator_name = input("Enter Your Name: ")
    print("Helo " + ticket_creator_name)

# staff Id

staff_id = ""
while len(staff_id) == 0:
    staff_id = input("Enter Your staff ID: ")


e_mail = ""
while len(e_mail) == 0:
    e_mail = input("enter your e_mail: ")

    print("Helo " + staff_id + "how can we help today?")

# description

description = ""
while len(description) == 0:
    description = input("Describe the problem in less than 50 worlds: ")
    print("Thank to contact Help desk")
    print("Ticket Status: Open")
    print("your ticket number is: ")

import random

print(random.randint(1, 200))




