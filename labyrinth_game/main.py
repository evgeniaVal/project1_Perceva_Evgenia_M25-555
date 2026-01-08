#!/usr/bin/env python3

from .constants import ROOMS
from .player_actions import show_inventory
from .utils import describe_current_room


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
        pass
    show_inventory(game_state)

if __name__ == "__main__":
    main()
