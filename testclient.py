from tkinter import *
from PIL import Image, ImageTk
from random import randint
import socket
import threading

server = "127.0.0.1"
port = 5555
g_round = 0
TOTAL_NO_OF_ROUNDS = 5
your_name = ""
your_score = 0

# main window
root = Tk()
root.title("Rock Scissor Paper Client")
root.configure(background="#9b59b6")

# picture
rock_img_p1 = ImageTk.PhotoImage(Image.open("image/rock-p1.png"))
rock_img_p2 = ImageTk.PhotoImage(Image.open("image/rock-p2.png"))
scissor_img_p1 = ImageTk.PhotoImage(Image.open("image/scissors-p1.png"))
scissor_img_p2 = ImageTk.PhotoImage(Image.open("image/scissors-p2.png"))
paper_img_p1 = ImageTk.PhotoImage(Image.open("image/paper-p1.png"))
paper_img_p2 = ImageTk.PhotoImage(Image.open("image/paper-p2.png"))

#Entry name
welcomeLabel = Label(root, font=100, text = "Welcome to the Game"
                    , bg="#9b59b6", fg="white").grid(row = 0, column = 2)
nameLabel = Label(root, font=100, text="Name"
                    , bg="#9b59b6", fg="white").grid(row=1, column=1, padx = 5)

#Entry form name
name_entry = StringVar()
entryNameform = Entry(root, font=100, width = 20, bg="#ABB2B9", fg="white")
entryNameform.grid(row=1, column=2,padx = 5, ipadx=15, ipady=15)

def displaygame():
    # indicators
    loginButton['state'] = "disabled"
    pname = entryNameform.get()
    your_name = pname
    print("Player Name:", pname)

    threading._start_new_thread(connect_sever, (pname, " "))

    user_indicator = Label(root, font=50, text = pname,bg="#9b59b6", fg="white")
    
    comp_indicator = Label(root, font=50, text="COMPUTER",
                        bg="#9b59b6", fg="white")
    user_indicator.grid(row=2, column=1)
    comp_indicator.grid(row=2, column=3)


loginButton = Button(root, font=100, text="Login" , state = NORMAL
                    , bg="#9b59b6", fg="white"
                    , command = displaygame
                    )
loginButton.grid(row=1, column=3,padx = 5, pady = 5, ipadx=15, ipady=15)

# Round
ground_lb = Label(root, font=50,text = "Round", bg="#9b59b6", fg="white")
ground_lb.grid(row=2, column=2)

# insert picture
player_picture = Label(root, image=scissor_img_p1, bg="#9b59b6")
comp_picture = Label(root, image=scissor_img_p2, bg="#9b59b6")
comp_picture.grid(row=3, column=4)
player_picture.grid(row=3, column=0)

# scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
compScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
compScore.grid(row=3, column=3)
playerScore.grid(row=3, column=1)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=5, column=2)

# update message
def update_status(x):
    msg['text'] = x

# update user score
def update_userscore():
    global your_score
    if g_round < TOTAL_NO_OF_ROUNDS:
        user_score = int(playerScore["text"])
        user_score += 1
        your_score += 1
        playerScore["text"] = str(user_score)



# update computer score
def update_compscore():
    if g_round < TOTAL_NO_OF_ROUNDS:
        score = int(compScore["text"])
        score += 1
        compScore["text"] = str(score)


# check winner
def check_winner(player, computer):
    if player == computer:
        update_status("Its a tie!!!")
        count_round()
    elif player == "rock":
        if computer == "paper":
            update_status("You loose")
            update_compscore()
            count_round()
        else:
            update_status("You Win")
            update_userscore()
            count_round()
    elif player == "paper":
        if computer == "scissor":
            update_status("You loose")
            update_compscore()
            count_round()
        else:
            update_status("You Win")
            update_userscore()
            count_round()
    elif player == "scissor":
        if computer == "rock":
            update_status("You loose")
            update_compscore()
            count_round()
        else:
            update_status("You Win")
            update_userscore()
            count_round()
    else:
        pass

#choices
choices = ["rock", "paper", "scissor"]

# buttons
rock = Button(root, width=20, height=2, text="ROCK", state = NORMAL,
                bg="#FF3E4D", fg="white", command=lambda: update_choice("rock"))
rock.grid(row=4, column=1)
paper = Button(root, width=20, height=2, text="PAPER", state = NORMAL,
                bg="#FAD02E", fg="white", command=lambda: update_choice("paper"))
paper.grid(row=4, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", state = NORMAL,
                bg="#0ABDE3", fg="white", command=lambda: update_choice("scissor"))
scissor.grid(row=4, column=3)

def update_choice(x):
    # for computer
    compchoice = choices[randint(0, 2)]
    if compchoice == "rock":
        comp_picture.configure(image=rock_img_p2)
        if g_round == TOTAL_NO_OF_ROUNDS:
            rock['state'] = "disabled"
            paper['state'] = "disabled"
            scissor['state'] = "disabled"
            
    elif compchoice == "paper":
        comp_picture.configure(image=paper_img_p2)
        if g_round == TOTAL_NO_OF_ROUNDS:
            rock['state'] = "disabled"
            paper['state'] = "disabled"
            scissor['state'] = "disabled"
           
    else:
        comp_picture.configure(image=scissor_img_p2)
        if g_round == TOTAL_NO_OF_ROUNDS:
            rock['state'] = "disabled"
            paper['state'] = "disabled"
            scissor['state'] = "disabled"

    # for user
    if x == "rock":
        player_picture.configure(image=rock_img_p1)
        if g_round == TOTAL_NO_OF_ROUNDS:
            rock['state'] = "disabled"
            paper['state'] = "disabled"
            scissor['state'] = "disabled"
            text = "Your score: " + str(your_score)
            threading._start_new_thread(connect_sever, (text, " "))

    elif x == "paper":
        player_picture.configure(image=paper_img_p1)
        if g_round == TOTAL_NO_OF_ROUNDS:
            rock['state'] = "disabled"
            paper['state'] = "disabled"
            scissor['state'] = "disabled"
            text = "Your score: " + str(your_score)
            threading._start_new_thread(connect_sever, (text, " "))

    else:
        player_picture.configure(image=scissor_img_p1)
        if g_round == TOTAL_NO_OF_ROUNDS:
            rock['state'] = "disabled"
            paper['state'] = "disabled"
            scissor['state'] = "disabled"
            text = "Your score: " + str(your_score)
            threading._start_new_thread(connect_sever, (text, " "))

    check_winner(x, compchoice)



def count_round():
    global g_round
    if g_round < TOTAL_NO_OF_ROUNDS:
        g_round = g_round + 1
    
    ground_lb["text"] = "Round: %s" % (str(g_round))

def connect_sever(player_name, y):
    try:
        dataname = bytes(player_name, 'utf-8')
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server, port))
        print('Successfully connected to ', server)

        client.sendall(dataname)
        
        data = client.recv(1024).decode('utf-8')

        print('Server says: welcome ' + str(data) + "ready to play!")
        
    except Exception as e:
        print("Cannot connect to host: " + str(server) + " on port: " + str(port) + " Server may be Unavailable. Try again later")
        print(e)


root.mainloop()
