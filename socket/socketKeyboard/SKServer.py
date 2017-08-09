# first of all import the socket library
import socket
import keyboard               

# next create a socket object
s = socket.socket()         
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12346 but it can be anything
port = 12346                

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)     
print("socket is listening")            

# a forever loop until we interrupt it or 
# an error occurs
while True:
	# Establish connection with client.
	c, addr = s.accept()     
	print('Got keyevent from', addr)

	# send a thank you message to the client.
	#sndmsg = "Hello Keyboard"
	#sndmsg2 = "anothermsg"
	#c.send(sndmsg.encode())
	#c.send(sndmsg2.encode())
	# Close the connection with the client
	#laststring = ''
	instring = c.recv(4096).decode()
	if instring:
		print(type(instring))
		print(instring)
		#instring = int(instring)
		#laststring = instring
		keyboard.press(instring)