#Maisha Mage
#12/6/25
#Final Project
#Create a Txt-based Python game 



import random

# Emojis
SWORD = "⚔️"
DAGGER = "🗡️"
SHIELD = "🛡️"
WOLF = "🐺"
MONSTER = "👹"
SKULL = "☠️"
POTION = "🧪"
COIN = "🪙"

def create_geralt():
    """Creates the one and only main character: Geralt."""
    strength = 15
    agility = 10
    stamina = 12
    health = 100 + (stamina * 2)

    geralt = {
        "name": "Geralt of Rivia",
        "strength": strength,
        "agility": agility,
        "stamina": stamina,
        "health": health,
        "max_health": health,
        "potions": 2,
        "gold": 0,
        "weapon": "steel",   # steel or silver
        "quen": False        # shield on/off
    }
    return geralt

def show_stats(player):
    weapon_icon = "⚔️" if player["weapon"] == "steel" else "🗡️"
    print("\n--- GERALT STATS ---")
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Strength: {player['strength']} | Agility: {player['agility']} | Stamina: {player['stamina']}")
    print(f"Potions: {POTION} x{player['potions']} | Gold: {COIN} {player['gold']}")
    print(f"Weapon: {weapon_icon} {player['weapon'].upper()} | Quen: {'ON' if player['quen'] else 'OFF'}")

def make_monster():
    monsters = [
        {"name": f"{WOLF} Drowner", "health": 40, "attack": 8, "reward": 5},
        {"name": f"{MONSTER} Ghoul", "health": 55, "attack": 10, "reward": 8},
        {"name": f"{SKULL} Wraith", "health": 65, "attack": 12, "reward": 12},
    ]
    return random.choice(monsters)

def switch_weapon(player):
    if player["weapon"] == "steel":
        player["weapon"] = "silver"
        print("🗡️ Geralt switches to the SILVER sword.")
    else:
        player["weapon"] = "steel"
        print("⚔️ Geralt switches to the STEEL sword.")

def activate_quen(player):
    player["quen"] = True
    print("🛡️ Quen activated! The next hit will be blocked.")

def geralt_attack(player, monster):
    damage = player["strength"] + random.randint(0, 5)

    # silver does bonus damage vs monsters
    if player["weapon"] == "silver":
        damage += 5
        print("🗡️ Silver sword bites into the monster!")
    else:
        print("⚔️ Steel sword slashes!")

    monster["health"] -= damage
    print(f"{SWORD} Geralt hits {monster['name']} for {damage} damage!")

def monster_attack(player, monster):
    # If Quen shield is on, block the hit and turn it off
    if player["quen"] == True:
        print("🛡️ Quen absorbs the damage!")
        player["quen"] = False
        return

    # dodge chance
    dodge_roll = random.randint(1, 20)
    if dodge_roll <= player["agility"]:
        print(f"{DAGGER} Geralt dodges the attack!")
        return

    damage = monster["attack"] + random.randint(0, 3)
    player["health"] -= damage
    print(f"{monster['name']} hits Geralt for {damage} damage!")

def drink_potion(player):
    if player["potions"] <= 0:
        print("No potions left!")
        return

    heal = 25
    player["health"] = min(player["max_health"], player["health"] + heal)
    player["potions"] -= 1
    print(f"{POTION} Geralt drinks a potion and heals {heal}! (Left: {player['potions']})")

def fight_loop(player):
    monster = make_monster()
    print(f"\nA monster appears! {monster['name']} (HP: {monster['health']})")

    while player["health"] > 0 and monster["health"] > 0:
        print(f"\nGeralt HP: {player['health']} | {monster['name']} HP: {monster['health']}")
        print("1) Attack ⚔️")
        print("2) Drink Potion 🧪")
        print("3) Switch Weapon 🔄")
        print("4) Cast Quen 🛡️")
        print("5) Run 🏃")

        choice = input("Choose: ")

        if choice == "1":
            geralt_attack(player, monster)
            if monster["health"] > 0:
                monster_attack(player, monster)
        else:
            if choice == "2":
                drink_potion(player)
                if monster["health"] > 0:
                    monster_attack(player, monster)
            else:
                if choice == "3":
                    switch_weapon(player)
                    if monster["health"] > 0:
                        monster_attack(player, monster)
                else:
                    if choice == "4":
                        activate_quen(player)
                        # monster still gets a turn (but Quen blocks it)
                        if monster["health"] > 0:
                            monster_attack(player, monster)
                    else:
                        if choice == "5":
                            run_chance = random.randint(1, 10)
                            if run_chance <= player["agility"]:
                                print("Geralt escaped!")
                                return
                            print("Geralt failed to escape!")
                            monster_attack(player, monster)
                        else:
                            print("Invalid choice.")

    if player["health"] <= 0:
        print(f"\n{SKULL} Geralt has fallen...")
    else:
        print(f"\n{SWORD} Geralt defeated {monster['name']}!")
        player["gold"] += monster["reward"]
        print(f"Earned {COIN} {monster['reward']} gold.")

        # small chance to find a potion
        if random.randint(1, 3) == 1:
            player["potions"] += 1
            print(f"Found a potion! {POTION} (+1)")

def main():
    print("=== THE WITCHER: TEXT HUNT ===")
    geralt = create_geralt()

    while True:
        print("\n--- MAIN MENU ---")
        print("1) Explore the path 🌲")
        print("2) Show Geralt stats 📜")
        print("3) Rest at campfire 🔥 (heal a bit)")
        print("4) Quit 🚪")
        choice = input("Choose: ")

        if choice == "1":
            print("\nGeralt walks the road...")
            if random.randint(1, 2) == 1:
                fight_loop(geralt)
                if geralt["health"] <= 0:
                    break
            else:
                print("No monsters... this time.")
        else:
            if choice == "2":
                show_stats(geralt)
            else:
                if choice == "3":
                    heal = 10
                    geralt["health"] = min(geralt["max_health"], geralt["health"] + heal)
                    print(f"🔥 Geralt rests and heals {heal}. (HP: {geralt['health']}/{geralt['max_health']})")
                else:
                    if choice == "4":
                        print("Farewell, witcher.")
                        break
                    else:
                        print("Invalid choice.")

if __name__ == "__main__":
    main()
