import random

game = ['rock','paper','scissors']
user_score = 0
computer_score = 0
user_set = 0
computer_set = 0
# winer_set = []

def user_choises():
    user =input("rock,paper or scissors?")
    while user not in game:
        user =input("plees choice rock, paper or scissors ? ")
    return user
    
def computer_choises():
    game = ['rock','paper','scissors']
    return random.choice(game) 

def winer (user_choises, computer_choice):
    global user_score , computer_score
    if user_choises == computer_choice:
        return "equle"
    elif (user_choises == 'rock' and computer_choice == 'scissors') or \
         (user_choises == 'paper' and computer_choice == 'rock') or \
         (user_choises == 'scissors' and computer_choice == 'paper'):
        user_score += 1 
        return "{^_^} happy you be winned {^_^}"
    else: 
        computer_score += 1
        return "{!haha, you lose, the computer wins!}"

# while user_score < 5 and computer_score < 5:
    
def play_game():
    user = user_choises()
    computer = computer_choises()
    print(f"you: {user}", " \n " ,f"you score: {user_score}")
    print(f"computer: {computer}", " \n " ,f"computer score: {computer_score}")
    print(winer(user,computer))

print()
print("                 {Ali Nazari}")
print()

while user_score < 5 and computer_score < 5:
    play_game()
    print("----------------------------------------------------")
    print(f"           you: {user_score}  computer: {computer_score}")
    again = input("Do you want to play again? (yes/no): ") 
    if again.lower() != "yes":
        print("Thanks for playing! goodbay!")
        print(f"    you: {user_score}  computer: {computer_score}")
        break
    
    print()
    print("                 {Ali Nazari}")
    print()
    # play_game()

if user_score >= 5 or computer_score >= 5 :
    if user_score > computer_score :
        # winer_set.append("you")
        print (f"winer set you: {user_set}  |  lose set computer: {computer_set}")
        user_set += 1
    elif computer_score > user_score :
        # winer_set.append("computer")
        print (f"winer set computer: {computer_set}  |  lose set you: {user_set}")
        computer_set += 1
    else :
        print("!you and computer equal to!")

again = input("Do you want to play again? (yes/no): ")
if again.lower() == "yes" :
    print("----------------------------------------------------")
    print("                 Wellcom set 2")
    play_game()

if again.lower() != "yes" :
    print(f"    you: {user_score}  computer: {computer_score}")
    print()
    print("      {^_~}finish the game{^_~}    ")
    print("     Thanks for playing! goodbay!  ")