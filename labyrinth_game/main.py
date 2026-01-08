#!/usr/bin/env python3

from .constants import COMMANDS
from .player_actions import get_input, move_player, show_inventory, take_item, use_item
from .utils import attempt_open_treasure, describe_current_room, show_help, solve_puzzle


def process_command(game_state, command):
    parts = command.split()
    if not parts:
        return
    command = parts[0]
    arg = parts[1] if len(parts) > 1 else ''
    match command:
        case 'look':
            describe_current_room(game_state)
        case 'use':
            use_item(game_state, arg)
        case 'go' | 'north' | 'south' | 'east' | 'west':
            move_player(game_state, arg if command == 'go' else command)
        case 'take':
            take_item(game_state, arg)
        case 'inventory':
            show_inventory(game_state)
        case 'solve':
            solve_puzzle(game_state) if \
              game_state['current_room'] != 'treasure_room' \
              else attempt_open_treasure(game_state)
        case 'quit' | 'exit':
            game_state['game_over'] = True
        case 'help':
            show_help(COMMANDS)
        case _:
            print("Неизвестная команда. Введите 'help' для списка команд.")

def main():
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
