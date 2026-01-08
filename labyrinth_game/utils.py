from math import sin

from labyrinth_game.player_actions import get_input

from .constants import ROOMS


def describe_current_room(game_state):
    title = game_state['current_room']
    current_room = ROOMS[title]
    description = current_room['description']
    items = current_room['items']
    exits = current_room['exits']
    puzzle = current_room['puzzle']

    print(f'== {title.upper()} ==')
    print(description)
    if items:
        print('Заметные предметы:')
        for item in items:
            print(f'- {item}')
    print('Выходы:')
    for exit in exits:
        print(f'- {exit}')
    if puzzle:
        print('Кажется, здесь есть загадка (используйте команду solve).')

def solve_puzzle(game_state):
    title = game_state['current_room']
    current_room = ROOMS[title]
    puzzle = current_room['puzzle']
    if not puzzle:
        print("Загадок здесь нет.")
    else:
        print(puzzle[0])
        if get_input('Ваш ответ: ').strip().lower() == puzzle[1].lower():
            print("Правильно! Загадка решена. Вы получили ключевой предмет.")
            current_room['puzzle'] = None
            game_state['player_inventory'].append('treasure_key')
        else:
            if title != 'trap_room':
                print("Неверно. Попробуйте снова.")
            else:
                trigger_trap(game_state)

def attempt_open_treasure(game_state):
    inventory = game_state['player_inventory']
    if 'treasure_key' in inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        game_state['game_over'] = True
    else:
        arg = get_input("Сундук заперт. ... Ввести код? (да/нет): ").strip().lower()
        if arg == 'да':
            ans = get_input("Введите код: ").strip()
            if ans == ROOMS['treasure_room']['puzzle'][1]:
                print("Код верен! Сундук открыт!")
                ROOMS['treasure_room']['items'].remove('treasure_chest')
                game_state['game_over'] = True
            else:
                print("Неверный код.")
        else:
            print("Вы отступаете от сундука.")

def show_help(COMMANDS):
    print("\nДоступные команды:")
    for command, description in COMMANDS.items():
        print(f" {command:<16}: {description}")

def pseudo_random(seed, modulo):
    value = sin(seed) * 12.9898 * 43758.5453
    value -= int(value)
    return int(value * modulo)

def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state['player_inventory']
    if not inventory:
        if pseudo_random(game_state['steps_taken'], 10) < 3:
            game_state['game_over'] = True
            print("Вы попали в ловушку и проиграли!")
        else:
            print("Вам удалось избежать ловушки на этот раз.")
    else:
        del inventory[pseudo_random(game_state['steps_taken'], len(inventory))]

def random_event(game_state):
    if pseudo_random(game_state['steps_taken'], 10) == 0:
        match pseudo_random(game_state['steps_taken'], 3):
            case 0:
                print("Вы нашли на полу монетку!")
                ROOMS[game_state['current_room']]['items'].append('coin')
            case 1:
                print("Вы услышали странный шум.")
                if 'sword' in game_state['player_inventory']:
                    print("Ваш меч отпугивает невидимую угрозу.")
            case 2:
                if game_state['current_room'] == 'trap_room' and \
                  'torch' not in game_state['player_inventory']:
                    trigger_trap(game_state)
