from .constants import ROOMS
from .utils import describe_current_room


def show_inventory(game_state) -> None:
    inventory: list[str] = game_state['player_inventory']
    if not inventory:
        print("Ваш инвентарь пуст.")
    else:
        print("В вашем инвентаре:")
        for item in inventory:
            print(f"- {item}")

def get_input(prompt:str="> ") -> str:
    try:
        input_str: str = input(prompt)
        return input_str.strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        exit()

def move_player(game_state, direction: str) -> None:
    current_exits: dict[str, str] = ROOMS[game_state['current_room']]['exits']
    if direction in current_exits:
        game_state['steps_taken'] += 1
        game_state['current_room'] = current_exits[direction]
        describe_current_room(game_state)
    else:
        print("Невозможно пойти в этом направлении.")

def take_item(game_state, item_name: str) -> None:
    current_items: list[str] = ROOMS[game_state['current_room']]['items']
    if item_name in current_items:
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
                print("Вы открыли bronze_box и нашли внутри rusty_key.")
                if 'rusty_key' not in inventory:
                    inventory.append('rusty_key')
            case _:
                print(f'Вы не знаете, как использовать {item_name}.')