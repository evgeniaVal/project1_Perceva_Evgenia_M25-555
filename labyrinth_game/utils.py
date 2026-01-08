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
    