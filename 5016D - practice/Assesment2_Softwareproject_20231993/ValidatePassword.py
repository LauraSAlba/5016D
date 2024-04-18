# ValidatePassword.py
#
# @ author: Laura Alba (20231993)
# date: April 2024
# Course: 5016D
# institution: Whitecliffe

# This code is from the if functions video
# collect strings / test length


input = raw_input("please enter a test string: ")

if len(input) < 6:
    print("your string is too short.")
    print("Please enter a string with at least 6 characters.")

# loop con  intentos para validar respuesta

number_of_tries = 3

while True:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!\n")
        # correct answer, so exit loop using break
        break
    else:
        print("Sorry that is the wrong answer.... "
              "Try again!\n")
        number_of_tries -= 1

    # check number of tries and break if none left
    if number_of_tries == 0:
        print("You have run out of goes. Sorry.")
        break

x = input("Press any key to exit.")