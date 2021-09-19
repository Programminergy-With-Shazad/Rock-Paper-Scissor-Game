import random

print('''Welcome to rock, paper, scissor game
Here are the rules:

You will play with rock, paper, scissor
:Rock will get over Scissor
:Paper will get over Rock
:Scissor will get over Paper

Enjoy your game with the AI Robot!
''')

play = "yes"

while play == "yes":
    choice = input("Choose your object: Rock, Paper, Scissor : ")
    print(choice)
    robot_choice = ["Rock", "Paper", "Scissor"]
    r_choice = robot_choice[random.randint(0, 2)]
    print("The robot will use {}".format(r_choice))

    if r_choice == "Rock":
        if choice == "Paper":
            print("Cool! You win")
        elif choice == "Scissor":
            print("Ohh! Robot won")

    if r_choice == "Paper":
        if choice == "Scissor":
            print("Cool! You win")
        elif choice == "Rock":
            print("Ohh! Robot won")

    if r_choice == "Scissor":
        if choice == "Paper":
            print("Oops! You lose")
        elif choice == "Rock":
            print("Yay! You win")
    if choice == r_choice:
        print("Hmm! Both put the same thing, Draw!")

    play = input("Do you wish to replay with the AI Robot? Yes / No")

    play = play.lower()
