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
        exit()