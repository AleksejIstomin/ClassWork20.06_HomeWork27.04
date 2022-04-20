number_1 = float(input('Ievadi skaitli: '))
number_2 = float(input('Ievadi skaitli: '))

print(f'Vai {number_1} ir lielāks par {number_2}?')

if number_1 > number_2:
    # šis kods pildās TIKAI, ja nosacījums izpildās
    print('Ir lielāks')

else: # citādāk
    # šis kods pildas TIKAI, ja nosacījums NEizpildās
    print('Nav lielāks')
