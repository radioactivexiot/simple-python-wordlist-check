
import time

password_input = input("Enter your password: ")
start = time.time()
password_found = False;
with open(r"enter_filepath_here") as file:
    for line in file:
        line = line.strip()
        if password_input == line.strip(" \n"):
            password_found = True;
            end = time.time()
            difference = end - start
            print(f"Cracked! in {difference} seconds")
            print(f"Password is {line}")
            break;
    if password_found == False:
        print("Password wasn't found..Congratulations!")

