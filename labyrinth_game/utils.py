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
    current_coom = ROOMS[game_state['current_room']]
    puzzle = current_coom['puzzle']
    if not puzzle:
        print("Загадок здесь нет.")
    else:
        print(puzzle[0])
        if input('Ваш ответ: ').strip().lower() == puzzle[1].lower():
            print("Правильно! Загадка решена.")
            current_coom['puzzle'] = None
            game_state['player_inventory'].append('reward')
        else:
            print("Неверно. Попробуйте снова.")