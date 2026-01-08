from .constants import ROOMS


def describe_current_room(game_state):
    title: str = game_state['current_room']
    current_room = ROOMS[title]
    description: str = current_room['description']
    items: list[str] = current_room['items']
    exits: dict[str, str] = current_room['exits']
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
        if title == 'treasure_room':
            attempt_open_treasure(game_state)
        else:
            print(puzzle[0])
            if input('Ваш ответ: ').strip().lower() == puzzle[1].lower():
                print("Правильно! Загадка решена. Вы получили ключевой предмет.")
                current_room['puzzle'] = None
                game_state['player_inventory'].append('treasure_key')
            else:
                print("Неверно. Попробуйте снова.")

def attempt_open_treasure(game_state):
    inventory = game_state['player_inventory']
    if 'treasure_key' in inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        game_state['game_over'] = True
    else:
        arg = input("Сундук заперт. ... Ввести код? (да/нет): ").strip().lower()
        if arg == 'да':
            ans = input("Введите код: ").strip()
            if ans == ROOMS['treasure_room']['puzzle'][1]:
                print("Код верен! Сундук открыт!")
                game_state['game_over'] = True
            else:
                print("Неверный код.")
        else:
            print("Вы отступаете от сундука.")

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение") 