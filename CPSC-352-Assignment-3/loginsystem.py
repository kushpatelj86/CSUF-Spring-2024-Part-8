
passwordfile = "db.txt"

import os
import bcrypt
#part 1, prompt user to choose between login or create account

def main():
	#check that the passwordfile exists
	#if not, create it
	if ( not os.path.exists(passwordfile)):
		open( passwordfile, 'w')
	part1()

	return 0
	
def create_account():
	print("creating an account")
	username = input("username: ")
	hashed_pass = ""
	if ( is_username_exist( username) ):
		print("username already exists. Please choose a different one.")
		create_account()
	else:
		password = input( "password: ")
		salt = bcrypt.gensalt()
		hashed_pass = hash_password( password, salt)
		append_dbfile = open( passwordfile, 'a')
		store_string = username + "  " + str( hashed_pass ) + " " + str(salt)
		append_dbfile.write( store_string)
		append_dbfile.write("\n") # set to new line
		append_dbfile.close()
	return username, hashed_pass
	
def loginto_account():
	# part 3

	print("username and password: ")
	username = input("username: ")
	if ( is_username_exist( username) ):
		# get the user entry
		user_entry = get_user_entry( username) # an array
		stored_hash = user_entry[2].rstrip()
		
		print("Hashed pass", stored_hash)
		password = input("password: ")
		if(bcrypt.checkpw(password.encode(), stored_hash.encode())):
			return True
		else:
			return False
		

	else:
		print("no username by that. Please try again.")
		loginto_account()
	
	return 0
	
def is_username_exist( username = ""):
	is_exist = False
	read_file = open(passwordfile, 'r')
	is_exist = ( username in read_file.read())
	read_file.close()
	return is_exist

def get_user_entry( username = ""):
	
	open_file = open( passwordfile, 'r')
	file_contents = open_file.readlines()
	# file_contents = open_file.read()
	search_str = username + " " #include the separating space of the username
	line_number = 0
	for entry in file_contents: #cycle through the lines of the db file
		if search_str in entry: # looking for the username to match
			break 
		line_number += 1
	print("line index: " , line_number)
	chosen_str = file_contents[line_number] # get the line contents of the username match
	line_array = chosen_str.split(" ")
	print("line array: " , line_array)
	return line_array

	
def hash_password ( plain_password = "", salt_int = 1):
	
	bytes = str.encode( plain_password)
	salt = bcrypt.gensalt()
	
	
	print("salt: ", salt)
	hashed_string = bcrypt.hashpw( bytes, salt)
	return hashed_string

def match_username_password ( username = "", hashed_pass = ""):
	
	open_file = open( passwordfile, 'r')
	user_pass_str = username + " " + hashed_pass
	is_matched = ( user_pass_str in open_file.read() )
	
		# if the username and hahs are in the file, return trueu
	open_file.close()
	return is_matched

def part1():
	print("""Would you like to:
	(1): create an account
	(2): login into an existing account""")
	user_input = input()
	
	username = ""
	hashed_pass = ""
	if user_input == "1":
		create_account()
	elif user_input == "2":
		#part3
		login_state = loginto_account()
		if login_state: # login successful
			print("login successful")
		else: #login failed
			print("login failed")
# part1()

main()