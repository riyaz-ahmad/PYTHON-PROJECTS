from classes.game import person, bcolors

magic=[{"name": "Fire", "cost": 10, "dmg": 100},
       {"name": "Thunder", "cost": 10, "dmg": 120},
       {"name": "Blizzard", "cost": 10, "dmg": 100}]

player= person(460, 65, 60, 34, magic)
enemy= person(460,65,45,25,magic)

running= True
i= 0

print(bcolors.FAIL+ bcolors.BOLD+ "An Enemy Attack"+ bcolors.ENDC)

while running:
    print("========================================")
    player.choose_action()
    choice= input("Choose action")
    index= int(choice)-1
    if index== 0:
        dmg= player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg , "points ")

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic"))-1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell= player.get_spell_name(magic_choice)
        cost= player.get_spell_mp(magic_choice)
        current_mp= player.get_mp()
        if cost > current_mp:
            print(bcolors.FAIL+ "\nNot enough MP \n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + "deals", str(magic_dmg), "points of damage", bcolors.ENDC)


    enemy_choice= 1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Attacked for", enemy_dmg)
    print("-----------------------------------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp())+ bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp())+ bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)

    if enemy.get_hp()== 0:
        print(bcolors.OKGREEN+ "You Win"+ bcolors.ENDC)
        running= False
    elif player.get_hp()== 0:
        print(bcolors.FAIL+ "YOU LOST!!!"+ bcolors.ENDC)
        running= False
