#import the socket module
import socket

def client_program():
    host=socket.gethostname()
    port =5000

    #create the instead socket
    client_socket = socket.socket()

    #instead pf binding, in client we are connecting  to server
    client_socket.connect((host,port))#host and port as tuple

    #getting the message to send to the server
    message = input("Enter the msg to send to server:")

    while message.lower().srip() !='exit':
        #if the msg is not 'exit', send to the server
        client_socket.send(message.encode())
        #receive any reply data from the server
        data=client_socket.recv(1024).decode()
        #print the received data as text
        print("Received from server: "+data)

    client_socket.close()

if __name__=='main':
    client_program()