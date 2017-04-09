from socket import *


mailserver = '213.199.180.138'
mailport = 25 # smptp port
clientSocket = socket(AF_INET, SOCK_STREAM) #establishing a TCP connection
clientSocket.connect((mailserver, mailport))
recv = clientSocket.recv(1024) # client socket receives a certain amount of data
recv = recv.decode()
print("Server response after connection request:" + recv)

try:
    recv[:3] != '220'   #if the message is not received
except Exception as msg:
    print('220 reply not received from server.')

heloCommand = 'HELO usos\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Server response after HELO command:" + recv1)

try:
    recv1[:3] != '250'
except Exception as msg:
    print('250 reply not received from server.')

clientSocket.send("MAIL FROM:<kaja@student.uj.edu.pl>\r\n".encode()) #From whom the message will be comming from
recv2 = clientSocket.recv(1024) #amount of data received
recv2 = recv2.decode()
print("Server response after specifying MAIL FROM : "+recv2) # printing out received message

try:
    recv2[:3] !='250'  #if message not received
except Exception as msg:
    print('250 reply not received from server.')

clientSocket.send("RCPT TO:<kaja.slomska@student.uj.edu.pl>\r\n".encode()) # To whom the message will be delivered
recv3 = clientSocket.recv(1024) #amount of data received
recv3 = recv3.decode()
print("Server response after specifying RCPT TO: "+recv3)

try:
    recv3[:3] !='250'
except Exception as msg:
    print('250 reply not received from server.')

data = "DATA\r\n" # sending the data
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
try:
    recv4[:3] !='354'
except Exception as msg:
    print('354 reply not received from server.')

print("Server response after DATA command: "+recv4)

clientSocket.send('\r\n One sentence message'.encode()) # A message to sent
clientSocket.send("\r\n.\r\n".encode())
recv5 = clientSocket.recv(1024)
recv5 = recv5.decode()
try:
    recv5[:3] !='250'  #if message not received
except Exception as msg:
    print('250 reply not received from server.')

clientSocket.send("QUIT\r\n".encode()) # telling server that a connection will be terminated
recv6 = clientSocket.recv(1024)
recv6 = recv6.decode()
print("server response after QUIT command: " + recv6)

try:
    recv6[:3] !='221'
except Exception as msg:
    print('221 reply not received from server.')
clientSocket.close() # closing socket