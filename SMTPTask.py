from socket import *

mailserver = '213.199.180.138'
mailport = 25 
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((mailserver, mailport))
responseIfServerIsReadyOrNot = clientSocket.recv(1024) 
responseIfServerIsReadyOrNot = responseIfServerIsReadyOrNot.decode()
print("Server response after connection request:" + responseIfServerIsReadyOrNot)

try:
    responseIfServerIsReadyOrNot[:3] != '220'   
except Exception as msg:
    print('220 reply not received from server.')

heloCommand = 'HELO usos\r\n'
clientSocket.send(heloCommand.encode())
responseIfrequestedMailActionCompleted = clientSocket.recv(1024)
responseIfrequestedMailActionCompleted = responseIfrequestedMailActionCompleted.decode()
print("Server response after HELO command:" + responseIfrequestedMailActionCompleted)

try:
    responseIfrequestedMailActionCompleted[:3] != '250'
except Exception as msg:
    print('250 reply not received from server.')

clientSocket.send("MAIL FROM:<kaja@student.uj.edu.pl>\r\n".encode()) 
responseAfterSpecifyingSender= clientSocket.recv(1024) 
responseAfterSpecifyingSender = responseAfterSpecifyingSender.decode()
print("Server response after specifying MAIL FROM : "+responseAfterSpecifyingSender) 

try:
    responseAfterSpecifyingSender[:3] !='250'  
except Exception as msg:
    print('250 reply not received from server.')

clientSocket.send("RCPT TO:<kaja.slomska@student.uj.edu.pl>\r\n".encode()) 
responseAfterSpecifyingReciper = clientSocket.recv(1024) 
responseAfterSpecifyingReciper = responseAfterSpecifyingReciper.decode()
print("Server response after specifying RCPT TO: "+responseAfterSpecifyingReciper)

try:
    responseAfterSpecifyingReciper[:3] !='250'
except Exception as msg:
    print('250 reply not received from server.')

data = "DATA\r\n" 
clientSocket.send(data.encode())
responseAfterStartingMailInput = clientSocket.recv(1024)
responseAfterStartingMailInput = responseAfterStartingMailInput.decode()
try:
    responseAfterStartingMailInput[:3] !='354'
except Exception as msg:
    print('354 reply not received from server.')

print("Server response after DATA command: "+responseAfterStartingMailInput)

clientSocket.send('\r\n One sentence message'.encode()) 
clientSocket.send("\r\n.\r\n".encode())
responseAfterSendingData = clientSocket.recv(1024)
responseAfterSendingData = responseAfterSendingData.decode()
try:
    responseAfterSendingData[:3] !='250' 
except Exception as msg:
    print('250 reply not received from server.')

clientSocket.send("QUIT\r\n".encode()) 
responseAfterClosingConnection = clientSocket.recv(1024)
responseAfterClosingConnection = responseAfterClosingConnection.decode()
print("server response after QUIT command: " + responseAfterClosingConnection)

try:
    responseAfterClosingConnection[:3] !='221'
except Exception as msg:
    print('221 reply not received from server.')
clientSocket.close()
