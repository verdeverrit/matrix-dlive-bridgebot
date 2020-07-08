# THIS CODE IS NOWHERE NEAR COMPLETION
# AS YOU CAN SEE...
# THIS IS CURRENTLY JUST A SKELETON
# 
# API CALLS CURRENTLY ARE BEING TESTED
# MESSAGE PROCESSING IS CURRENTLY BEING TESTED
# 
# THIS FILE WILL NOT BE UPDATED UNTIL
# ALL TESTS ARE COMPLETED AND THE CODING BEGINS

import requests
import graphene
import json

# Default account credentials
acct_dlive_user=""
acct_dlive_pass=""
acct_dlive_token=""
acct_matrix_user=""
acct_matrix_pass=""
acct_matrix_token=""

# Registers dlive account with bot
def register_dlive():

	return status
	
# Registers matrix account with bot
def register_matrix():

	return status

# Gets data from dlive
def recv_dlive():
	
	return data_recv_dlive

# Sends data to dlive
def send_dlive(msgs_send_dlive):

	return status

# Gets data from matrix
def recv_matrix():

	return data_recv_matrix

# Sends data to matrix
def send_matrix(msgs_send_matrix):

	return status

# Sorts dlive data outputting only messages
# exclude sticker messages
def sort_dlive(data_recv_dlive):

	return msgs_recv_dlive

# Sorts matrix data outputting only messages
# Maybe not needed due to proper api calls
def sort_matrix(data_recv_matrix):

	return msgs_recv_matrix

# Formats dlive json to matrix json
def format_dlive_matrix(msgs_recv_dlive):

	return msgs_send_matrix

# Formats matrix json to dlive json
def format_matrix_dlive(msgs_recv_matrix):

	return msgs_send_dlive

# Main program
def main():
	#runs once then loops forever
	#register accounts with bot
	register_dlive()
	register_matrix()
	#loop forever
		#check exit signal: exit or continue
		#use unix epoch without millseconds to comapare last call
		#request data from dlive and matrix once per second
		recv_dlive()
		recv_matrix()
		#sort data for messages
		sort_dlive(data_recv_dlive)
		sort_matrix(data_recv_matrix)
		#format data for other platform
		format_dlive_matrix(msgs_recv_dlive)
		format_matrix_dlive(msgs_recv_matrix)
		#send data to dlive and matrix
		send_dlive(msgs_send_dlive)
		send_matrix(msgs_send_matrix)

# Runs main program
if __name == "__main__":
	main()
