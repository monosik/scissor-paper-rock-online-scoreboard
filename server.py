from tkinter import *
import socket
import threading

server = "127.0.0.1"
port = 5555
client_list = []
clientname_list = []


#Login
login = Tk()
login.configure(background="#9b59b6")
login.title("Login")

#Entry name
welcomeLabel = Label(login, font=100, text = "Welcome to the Game"
                    , bg="#9b59b6", fg="white").grid(row = 0, column = 1,pady = 5)
#client scoreboard
pLabel = Label(login, font=100, text = "Client List"
                    , bg="#9b59b6", fg="white").grid(row=1, column=1,padx = 5, pady = 5)
pDisplay = Text(login, bg="#9b59b6", fg="white", font=100, height = 10, width = 30, padx = 10, pady = 10)
pDisplay.grid(row = 2, column = 1, padx = 20, pady = 20)

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server, port))
    s.listen()
    print("Waiting for a connection, Server Start")

    threading._start_new_thread(get_client, (s, " "))
    

def get_client(connection, y):
    while True:
        client, addr = connection.accept()
        client_list.append(client)
        print("A New Connection from:", str(addr))

        threading._start_new_thread(send_receive_client_message, (client, addr))

def send_receive_client_message(client_connection, client_addr):

    index = get_client_index(client_list, socket)
    while True:
        namedata = client_connection.recv(1024).decode('utf-8')
        clientname_list.append(namedata)
        update_player_display(clientname_list[index - 1])
        print("receive name from client:", str(clientname_list[index - 1]))
        print(type(clientname_list))
        #client_connection.send(namedata)
    
    
    del clientname_list[index - 1]
    del client_list[index - 1]
    client_connection.close()

    update_player_display(clientname_list)
    

def get_client_index(curr_client_list, curr_client):
    index = 0
    for conn in curr_client_list:
        if conn == curr_client:
            break
        index = index + 1

    return index


def update_player_display(name_list):
    c = name_list
    pDisplay.insert(END, c + "\n")


start_server() 

login.mainloop()