import random
def rock_paper_scissors():
    option_list = ['R', 'P', 'S']
    player_choice = str(input('Choose one: R, P, S: \n'))
    player_choice = player_choice.upper()
    option = random.choice(option_list)
    if player_choice in option_list:
        print('Player (' + player_choice+ ') : CPU (' + option + ')')
        if player_choice == option:
            print('Tie!')
            rock_paper_scissors()
        elif player_choice == 'R' and option == 'S':
            print('You win!')
        elif player_choice == 'R' and option == 'P':
            print('You lose!')
        elif player_choice == 'P' and option == 'R':
            print('You win!')
        elif player_choice == 'P' and option == 'S':
            print('You lose!')
        elif player_choice == 'S' and option == 'P':
            print('You win!')
        elif player_choice == 'S' and option == 'R':
            print('You lose!')
    elif player_choice != 'R' or 'P' or 'S':
        print('Invalid input!')
        rock_paper_scissors()
rock_paper_scissors()
