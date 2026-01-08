def show_inventory(game_state):
    inventory = game_state['player_inventory']
    if not inventory:
        print("Ваш инвентарь пуст.")
    else:
        print("В вашем инвентаре:")
        for item in inventory:
            print(f"- {item}")