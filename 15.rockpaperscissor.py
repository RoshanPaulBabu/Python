import random

def get_user_choice():
        user_choice = input("Enter your choice(rock, paper, or scissors): ")
        return user_choice

def get_computer_choice():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        return "rock"
    elif computer_choice == 2:
        return "paper"
    else:
        return "scissors"


def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return("Its a tie")


    elif ((user_choice == "rock" and computer_choice == "scissors")or
          (user_choice == "paper" and computer_choice == "rock")or
          (user_choice == "scissors" and computer_choice == "paper")):
        return "You won"

    else:
        return "Computer wins!"

def main():
    while True:
        print("Let's play Rock, Paper, Sciccors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")
        result = determine_winner(user_choice,computer_choice)
        print(result)

        
        if result == "Its a tie":
                print()
                continue;

        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again !="yes":
            break
        print()
        
if __name__ == "__main__":
    main()
    
            
                   
        
    




    
