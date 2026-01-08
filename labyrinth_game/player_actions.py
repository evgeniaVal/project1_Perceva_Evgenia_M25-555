from .constants import ROOMS
from .utils import describe_current_room, random_event


def show_inventory(game_state):
    inventory = game_state['player_inventory']
    if not inventory:
        print("Ваш инвентарь пуст.")
    else:
        print("В вашем инвентаре:")
        for item in inventory:
            print(f"- {item}")

def get_input(prompt="> "):
    try:
        input_str = input(prompt)
        return input_str.strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"

def move_player(game_state, direction):
    current_exits = ROOMS[game_state['current_room']]['exits']
    if direction in current_exits:
        if current_exits[direction] == 'treasure_room':
            if 'rusty_key' in game_state['player_inventory']:
                print("Вы используете найденный ключ, чтобы открыть путь в комнату" \
                " сокровищ.")
            else:
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
                return
        game_state['steps_taken'] += 1
        game_state['current_room'] = current_exits[direction]
        describe_current_room(game_state)
        random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")

def take_item(game_state, item_name):
    current_items = ROOMS[game_state['current_room']]['items']
    if item_name in current_items:
        if item_name == 'treasure_chest':
            print("Вы не можете поднять сундук, он слишком тяжелый.")
        else:
            game_state['player_inventory'].append(item_name)
            current_items.remove(item_name)
            print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name):
    inventory = game_state['player_inventory']
    if item_name not in inventory:
        print("У вас нет такого предмета.")
    else:
        match item_name:
            case 'torch':
                print("Вы зажгли факел. Теперь вокруг светлее.")
            case 'sword':
                print("Вы взяли меч в руки. Чувствуете себя увереннее.")
            case 'bronze_box':
                if 'rusty_key' not in inventory:
                    print("Вы открыли bronze_box и нашли внутри rusty_key.")
                    inventory.append('rusty_key')
            case _:
                print(f'Вы не знаете, как использовать {item_name}.')