mat = int(input('Matematika: '))
fiz = int(input('Fizika: '))
kim = int(input('Kimija: '))

if mat >= 65 and fiz >= 65 and kim >= 50:
    print('Var sākt studijas')

elif mat + fiz + kim >= 190:
    print('Var sākt studijas')
elif mat + fiz >= 140:
    print('Var sākt studijas')
else:
     print('Nevar sākt studijas')

# 2 var

# maths = int(input('Matemākas rezultāts: '))
# physics = int(input('Fizikas rezultāts: '))
# chemistry = int(input('Ķīmijas rezultāts: '))
#
# criteria_1 = maths >= 65 and physics >= 65 and chemistry >= 50
# criteria_2 = maths + physics >= 140
# criteria_3 = maths + physics + chemistry >= 190
#
# if criteria_1 or criteria_2 or criteria_3:
#     print('Apsveicu, tu kļuvi par studentu!')
#
# else:
#     print('Mēģini nākamajā semestrī :(')
