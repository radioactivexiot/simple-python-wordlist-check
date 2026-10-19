
import time

password_input = input("Enter your password: ")
start = time.time()
with open(r"@filepath\passwords.txt") as file:
    for line in file:
        line = line.strip()
        print(f"{line} and {password_input}")
        if password_input == line.strip(" \n"):
            end = time.time()
            difference = end - start
            print(f"Cracked! in {difference} seconds")
            break;
    print("Password wasn't found..Congratulations!")

