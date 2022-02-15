from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
	mailserver = ('127.0.0.1', 1025)

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect(mailserver)
    # Fill in end

    recv = clientSocket.recv(1025).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1025).decode()
    #print(recv1) 
    if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
	mail_command = ('MAIL FROM: &..6@nyu.edu>\r\n') #from who the message will appear
	clientSocket.send(mail_command.encode())
	recv1 = clientSocket.recv(1025).decode()
		#print(recv2)
	if recv2[:3] !='250': #if the data is not received
		#print('250' reply not recieved from server.!')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
	rcpt_command = ('RCPT TO:..3@hotmail.com\r\n) #Recipient
	clientSocket.send(rcpt_command.encode())
	recv3 =  clientSocket.recv(1025).decode()
	if recv[:3] != '250': #if the data is not received
		#print('250 reply is not received from server)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
	data = "DATA \r\n"
	clientSocket.send(data.encode())
	recv4 = clientSocket.recv(1025).decode()
	#print(recv4)
	if recv4[:3] != '354': #if data us not received
		#print('354 reply is not received from server')
    # Fill in end

    # Send message data.
	#subject = "Subject: Testing SMTP client \r\n"
	subject =  "Subject: testing my client \r\n"
	clientSocket.send(subject.encode())
	#date = data + '\r\n\r\n
	#clientSocket.send(msg.encode())
    # Fill in start
	clientSocket.send(msg.encode())
	clientSocket.send(endmsg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
	recv_msg = clientSocket.recv(1025)
	#print("Response after sending message body:" + recv_msg.decode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
	quitcommand = ('QUIT\r\n')
	clientSocket.send(quitcommand.encode())
	recv5 = clientSocket.recv(1025).decode()
	#print(recv5)
    # Fill in end

clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')