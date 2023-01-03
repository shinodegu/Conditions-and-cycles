
while True:
    name = (input('Enter your name: '))
    age = (input('Enter your age: '))

    if not age.isdigit() or int(age) <= 0:
     print('Ошибка, повторите ввод')
     continue

    elif int(age) >0 and int(age) <10:
     print('Привет, шкет ' + name)

    elif int(age) >=10 and int(age) <=18 :
     print('Как жизнь ' + name)

    elif int(age) >18 and int(age) <100:
     print('Что хотите ' + name)

    else: print(name + ' Вы лжете - в наше время столько не живут...')

    gameover = input('Желаете выйти (У/Д)')
    if gameover.upper() in ('У', 'Д'):
         break
