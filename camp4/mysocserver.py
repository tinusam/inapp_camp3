#import the socket module
import socket

def server_program():
    host= socket.gethostname() #getting the ip of host
    port = 5000
    #"127.0.01" or "localhost"
    #port can range from 1024 till 65535

    #create the instance of socket
    server_socket = socket.socket()

    #binding the host ip and port to our  socket instance
    #pass the host and port as a tuple into the bind() method
    server_socket.bind((host,port))

    #start listening to the socket
    server_socket.listen(2)

    #accept an incoming connection
    #the accept() method will give back the conn obj and
    # ip address of the incoming connection req
    conn, address = server_socket.accept()
    print("Connection acccepted from" +address)

    #now we can receive the messages
    #using a while loop,keep the connection active and
    #receive message until there is none

    while True:
        #infinite white loop to receive the data strem
        #receive the packets(max size of 1024 bytes)
        #decode the received data
        data = conn.recv(1024).decode()
        #if no data recived, then terminate the while loop
        if not data:
            break
        #if valid data we can print the data received
        print("Message from client" +str(address)+":"+str(data))
        #give provision to send reply back to the client
        data = input('Type reply here: ')
        #send encode the data to the client
        conn.send(data.encode())

    conn.close()#close the connection once the while loop break
if __name__ == '__main__':
    server_program()
#if our python program is imported, the just be there
#as an imported code and do not run until the user calls
#the function(default behavior)
#if we directly running it using the command python [prog.py]
#then start the function server_program ()automatically

