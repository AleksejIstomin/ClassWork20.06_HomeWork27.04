# Lietotājs ievada skaitli 0, 1 vai 2. Skaitlis 0 apzīmē akmeni, 1 – šķēres, 2 – papīru.
# Programma nejauši izvēlās akmeni, šķēres, vai papīru.
# Uz ekrāna tiek parādīts ko ir izvēlējies lietotājs, ko – dators.
# Tiek parādīts kas ir uzvarējis – dators vai lietotājs, vai neizšķirts.

user_input = int(input('Please enter: Rock - 0, Paper - 1 or Scissors - 2: '))
rock = 0
paper = 1
scissors = 2
if 0:
    print(f'Rock')
import random
computer_choice = random.randint(0, 2)
print(computer_choice)
criteria_0 = rock == rock
criteria_1 = paper == paper
criteria_2 = scissors == scissors
criteria_3 = rock > scissors
criteria_4 = rock < paper
criteria_5 = paper < scissors
criteria_6 = paper > rock
criteria_7 = scissors > paper
criteria_8 = scissors < rock
if criteria_0 or criteria_1 or criteria_2:
    print(user_input, 'vs', computer_choice)
    # print('No one wins')
elif criteria_3 or criteria_6 or criteria_7:
    print(user_input, 'vs', computer_choice)
    # print('User wins, computer loose')
elif criteria_4 or criteria_5 or criteria_8:
    print(user_input, 'vs', computer_choice)