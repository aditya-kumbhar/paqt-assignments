import re
import logging

#Open file for logging
logging.basicConfig(filename='passwordValidation.log',level=logging.DEBUG)

#Function to validate password : return type-boolean (True: valid, False: invalid)
def validate(password):
	logging.info('Validating password %s',password)
	
	if(len(password) in range(6,13)):				#validate password length
		if(re.search('[A-Z]',password)):			#check presence of an upper case char
			if(re.search('[a-z]',password)):		#check presence of a lower case char
				if(re.search('[$#@]',password)):	#check presence of special characters
					logging.info('Password is valid') 
					return True						#return true for valid password	
				else:
					logging.info('Invalid password: Special characters not present')
			else:
				logging.info('Invalid password: Lower case characters not present')
		else:
			logging.info('Invalid password: Upper case characters not present')
	else:
		logging.info('Invalid password: Password length must be between 6-12 characters')
	return False									#return false for invalid password	

#Main
if __name__ == '__main__':
	s = input("Enter password to validate: ")
	if(validate(s)):
		print('Valid password')
	else:
		print('Invalid password')			


