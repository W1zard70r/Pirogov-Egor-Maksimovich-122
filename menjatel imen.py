import random, os
def zxc():
    x=int(input('Нужна ли справка об авторе?(1-да,2-нет): '))
    if x==1:
        print(f' Всё сделал-Пирогов Егор')
    a=input('Введи имя: ')
    pol=int(input('Вы мужчина?(1-да,2-нет): '))
    if pol==1:
        b=list(a)
        c=b[1:]
        var=b[2:]
        var2=''.join(var)
        d=''.join(c)
        v=random.choice(['Мар','Муд','Зиг','Муха'])
        z=random.choice(['нер','ор','кс','бек','ммед'])
        k=random.choice(['Мар','Муд','Зиг','Муха'])
        l=random.choice(['нер','ор','кс','бек','ммед'])
        print(f'Ваше имя: {v}{d}{z}.\nАльтернативный вариант: {k}{var2}{l}')
    elif pol==2:
        b=list(a)
        c=b[1:]
        var=b[2:]
        var2=''.join(var)
        d=''.join(c)
        v=random.choice(['Мар','Муд','Зиг'])
        z=random.choice(['лина','на','ла'])
        k=random.choice(['Мар','Муд','Зиг'])
        l=random.choice(['нер','ор','кс'])
        print(f'Ваше имя: {v}{d}{z}.\nАльтернативный вариант: {k}{var2}{l}')
    m=int(input('Хотите ещё раз запустить?(1-да 2-нет)'))
    if m==1:
        os.system('cls')
        return zxc()
zxc()
