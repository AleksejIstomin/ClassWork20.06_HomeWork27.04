# Lietotājs ievada skaitli 0, 1 vai 2. Skaitlis 0 apzīmē akmeni, 1 – šķēres, 2 – papīru.
# Programma nejauši izvēlās akmeni, šķēres, vai papīru.
# Uz ekrāna tiek parādīts ko ir izvēlējies lietotājs, ko – dators.
# Tiek parādīts kas ir uzvarējis – dators vai lietotājs, vai neizšķirts.

user_input = int(input('Please enter: Rock - 0, Paper - 1 or Scissors - 2: '))
rock = Rock = 0
paper = Paper = 1
scissors = Scissors = 2

import random
computer_choice = random.randint(0, 2)
print(computer_choice)
criteria_0 = 0 == 0
criteria_1 = 1 == 1
criteria_2 = 2 == 2
criteria_3 = 0 > 2
criteria_4 = 0 < 1
criteria_5 = 1 < 2
criteria_6 = 1 > 0
criteria_7 = 2 > 1
criteria_8 = 2 < 1
if criteria_0 or criteria_1 or criteria_2:
    print(user_input, 'vs', computer_choice)
    print('No one wins')