#!/usr/bin/env python3

from .constants import ROOMS
from .player_actions import get_input, move_player, show_inventory, take_item, use_item
from .utils import describe_current_room, solve_puzzle


def process_command(game_state, command: str):
    parts = command.split()
    command = parts[0]
    arg = parts[1] if len(parts) > 1 else ''
    match command:
        case 'look':
            describe_current_room(game_state)
        case 'use':
            use_item(game_state, arg)
        case 'go':
            move_player(game_state, arg)
        case 'take':
            take_item(game_state, arg)
        case 'inventory':
            show_inventory(game_state)
        case 'solve':
            solve_puzzle(game_state)
        case 'quit' | 'exit':
            game_state['game_over'] = True

def main() -> None:
    print('Добро пожаловать в Лабиринт сокровищ!')
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
    }
    describe_current_room(game_state)
    while not game_state['game_over']:
        process_command(game_state, get_input())

if __name__ == "__main__":
    main()
