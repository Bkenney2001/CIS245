#gathers necessary input from user
file_name = input("What is your file name? ")
user_name = input("What is your name? ")
street_name = input("What is your street name? ")
phone_number = input("What is your phone number? ")

filename = file_name

#opens the file that the user input and writes their name, address, and phone number into the file
#closes the file
with open(filename, 'w') as fileHandle:
  fileHandle.write(f"{user_name}, {street_name}, {phone_number}")
fileHandle.close()

#opens the file and reads the text the program wrote into it
#prints the data to the user
with open(filename, 'r') as fileHandle:
  data = fileHandle.read()
print("\n",data)