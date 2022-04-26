# Lietotājs ievada skaitli 0, 1 vai 2. Skaitlis 0 apzīmē akmeni, 1 – šķēres, 2 – papīru.
# Programma nejauši izvēlās akmeni, šķēres, vai papīru.
# Uz ekrāna tiek parādīts ko ir izvēlējies lietotājs, ko – dators.
# Tiek parādīts kas ir uzvarējis – dators vai lietotājs, vai neizšķirts.

user_input = int(input('Please enter: Rock - 1,  Paper - 2, Scissors - 3\nUser chose:'))
if user_input == 1:
    print('User: Rock')
elif user_input == 2:
    print('User: Paper')
elif user_input == 3:
    print('User: Scissors')
else:
    print('User number is wrong ')
    exit()
import random
computer_choice = random.randint(1, 3)
if computer_choice == 1:
    print('Computer: Rock')
elif computer_choice == 2:
    print('Computer: Paper')
elif computer_choice == 3:
    print('Computer: Scissors')
if user_input == computer_choice:
    print('Nobody wins')
elif user_input == 1 and computer_choice == 2 or user_input == 2 and computer_choice == 3 or user_input == 3 and computer_choice == 1:
    print('Computer wins')
elif user_input == 3 and computer_choice == 2 or user_input == 2 and computer_choice == 1 or user_input == 1 and computer_choice == 3:
    print('User wins')
