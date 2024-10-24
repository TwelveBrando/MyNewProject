import random
import sys


def up_lvl(stats, lvl_counter, enemy):
    print("чтобы прокачать лвл, ты отправляешься в подземелье. Отработка ударов по скалам прокачивает урон "
          "и шанс критического урона, а перетаскивание камней - здоровье. Дак что ты выберешь?")
    while True:
        act_up_lvl = input("1 - отработка ударов по скалам;\n2 - перетаскивание камней;\n"
                           "3 - выйти из подземелья;\n")
        if act_up_lvl not in '123':
            while act_up_lvl not in '123':
                act_up_lvl = input("Ввести можно только 1, 2 или 3. Попробуй еще раз: ")
        match act_up_lvl:
            case "3":
                print(f"{stats['name']} выходит из подземелья...")
                menu(stats, lvl_counter, enemy)
                break
            case "2":
                num = random.randint(10, 39)
                print(f"{stats['name']} тащит тяжелый камень {num} метров...")
                if stats['health'] + num // 10 * 10 > 400:
                    print('Достигнуто максимальное значения здоровье. Дальше некуда качаться!')
                    continue
                stats['health'] += num // 10 * 10
                print(f'Здоровье персонажа {stats["name"]} было увеличено на {num // 10 * 10} единиц')
            case "1":
                num = random.randint(10, 59)
                print(f"{stats['name']} отработал {num} ударов по скале")
                if stats['chance_krit_damage'] + num // 10 > 50:
                    print("Достигнуто максимальное значение шанса критического урона. Дальше некуда качаться!")
                    continue
                elif stats['damage'] + num // 10 > 80:
                    print("Достигнуто максимальное значение урона. Дальше некуда качаться!")
                    continue
                stats['chance_krit_damage'] += num // 10
                stats['damage'] += num // 10
                print(f'Шанс критического урона и урон персонажа {stats["name"]} было увеличено на {num // 10} единиц')


def fight(stats, lvl_counter, enemy):
    health, damage, chance_krit_damage = stats['health'], stats['damage'], stats['chance_krit_damage']
    print(f"И так, перед тобой {lvl_counter + 1} босс. Его прозвище {enemy[lvl_counter]['name']}.\nЕго здоровье: "
          f"{enemy[lvl_counter]['health']}\nЕго урон: {enemy[lvl_counter]['damage']}")
    print(f'Ты можете попытаться сбежать от него в самом начале, но в таком случае шанс смерти будет 50 на 50.')
    act_fight = input(f'1 - Вступить в бой, 2 - попытаться сбежать\n')
    if act_fight not in '12':
        while act_fight not in '12':
            act_fight = input('Выбрать можно только 1 или 2! Давай еще раз: ')
    if act_fight == '2':
        chance = random.randint(1, 2)
        if chance == 1:
            print(f'Сбежать не удалось. {stats["name"]} погиб. GG')
            sys.exit()

        if chance == 2:
            print(f'В этот раз тебе удалось удрать. В следующий раз приходи подготовленным!')
            menu(stats, lvl_counter, enemy)
    else:
        while True:
            punch = input('Напиши "удар", чтобы нанести удар противнику: ')
            if punch != 'удар':
                while punch != 'удар':
                    punch = input('Ты можешь выбрать только удар)). Давай еще разок: ')
            chance_na_krit = random.randint(1, 2)
            if chance_na_krit == 1:
                final_damage = damage * 1.1
                if enemy[lvl_counter]['health'] - final_damage <= 0:
                    break
                else:
                    enemy[lvl_counter]['health'] -= final_damage
                    print(f'боссу {enemy[lvl_counter]["name"]} был нанесен урон: {final_damage}. '
                          f'Текущее здоровье босса: {enemy[lvl_counter]["health"]}')
            else:
                if enemy[lvl_counter]['health'] - damage <= 0:
                    break
                else:
                    enemy[lvl_counter]['health'] -= damage
                    print(f'боссу {enemy[lvl_counter]["name"]} был нанесен урон: {damage}. '
                          f'Текущее здоровье босса: {enemy[lvl_counter]["health"]}')
            print(f'{enemy[lvl_counter]["name"]} Замахивается и...')
            chance_of_miss = random.randint(1, 2)
            if chance_of_miss == 1:
                print('Промахивается! На этот раз ты увернулся')
            else:
                print('Наносит тебе удар..')
                if health - enemy[lvl_counter]["damage"] <= 0:
                    health -= enemy[lvl_counter]["damage"]
                    break
                else:
                    health -= enemy[lvl_counter]["damage"]
                    print(f"{enemy[lvl_counter]['name']} снес тебе {enemy[lvl_counter]['damage']} урона. "
                          f"Твое текущее здоровье: {health}")
    if health <= 0:
        print('Ты погиб. GG')
        sys.exit()
    else:
        print(f'Ты победил {lvl_counter + 1} босса. Поздравляю!')
        lvl_counter += 1
        menu(stats, lvl_counter, enemy)


def menu(stats, lvl_counter, enemy):
    while True:
        if lvl_counter == 10:
            print("Ты прошел игру! GG <3")
            sys.exit()
        print("                                 МЕНЮ                                 ")
        print("----------------------------------------------------------------------")
        print(f"Статы персонажа {stats['name']}:                            Пройдено уровней: {lvl_counter}\nЗдоровье: {stats['health']}\nУрон: {stats['damage']}\n"
        f"chance_krit_damage: {stats['chance_krit_damage']}%")
        print(f"Ты можете выбрать следующие действия:\n1) Спуститься в подземелье (повышает статы)\n"
        f"2) Перейти к новому уровню\n3) Закончить игру")
        print("----------------------------------------------------------------------")
        act = input("Что ты выберешь(1/2/3)? ")
        if act not in '123':
            while act not in '123':
                print("Выбрать можно только 1, 2, или 3!")
                act = input("давай еще раз: ")
        match act:
            case "3":
                print("Ты вышел из игры. До новых встреч!")
                sys.exit()
            case "1":
                up_lvl(stats, lvl_counter, enemy)
            case "2":
                fight(stats, lvl_counter, enemy)


def start():
    enemy = [{'name': 'Обезьянка в ширме', 'health': 50, 'damage': 12}, {'name': 'Обезьянка-страж', 'health': 75, 'damage': 18},
             {'name': 'Госпожа бабочка', 'health': 100, 'damage': 23}, {'name': 'Гёбу Масатака Онива', 'health': 125, 'damage': 28},
             {'name': 'Гэнитиро Асина', 'health': 150, 'damage': 33}, {'name': 'Великий Змей', 'health': 175, 'damage': 38},
             {'name': 'Великий Синоби Филин', 'health': 200, 'damage': 43}, {'name': 'Токудзиро обжора', 'health': 225, 'damage': 48},
             {'name': 'Эмма', 'health': 250, 'damage': 53}, {'name': 'Обезьянка в ширме', 'health': 275, 'damage': 58}]
    lvl_counter = 0
    print("Здравствуй, дорогой игрок")
    entry = input("Хочешь ли ты войти в игру (да/нет)? ").lower()
    if entry not in ['да', 'нет']:
        while entry not in ['да', 'нет']:
            print("Ввести можно только 'да' или нет'!")
            entry = input("попробуйте еще раз: ")
    if entry == 'нет':
        print("Как пожелаешь.")
    else:
        print(f'И так, давай начнем. Всего в игре 10 уровней, которые тебе предстоит пройти ни разу не умерев. \n'
        'У твоего персонажа будут основные атрибуты: урон, уровень здоровья, шанс критического урона и \n'
        'уровень брони. Также у тебя будет возможность прокачать атрибуты за счет выполнения каких-то заданий \n'
        'или тренировок. Пока что это все.')
        name = input("Введи имя своего персонажа: ")
        stats = {'name': name, 'damage': 25, 'health': 150, 'chance_krit_damage': 3}
        menu(stats, lvl_counter, enemy)


start()