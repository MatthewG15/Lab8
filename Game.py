# -*- coding: utf-8 -*-

print "A monster approaches prepare to fight You have 100 health and the monster has 100 health"
PlayerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDamage = 10
fireballDmg = 30
while (PlayerHealth > 0 and monsterHealth > 0):
    print 'Which attack do you choose?'
    print '1-punch 2-sword 3-fireball'
    Attack = int(raw_input())
    if(Attack == 1):
        print 'punch does 5 damage'
        monsterHealth = monsterHealth - 5
    if(Attack == 2):
        print 'Sword does 10 damage'
        monsterHealth = monsterHealth - 10
    if(Attack == 3):
        print 'Fireball does 30 damage'    
        monsterHealth = monsterHealth - 30
    import random 
    DamagefromMonster = random.randint(10,50)
    PlayerHealth = PlayerHealth - DamagefromMonster
    print "ouch the monster hit you hard"
    print " "
    print "the monster did " + str(DamagefromMonster) + " damage"
    print " "
    print 'You now have ' + str(PlayerHealth) + " health"
    print " "
    print "the monster now has " + str(monsterHealth) + " health"
    
    if(monsterHealth <= 0):
        print "congrajulations you killed the monster"
    if(PlayerHealth <= 0):
        print "Oh no the monster killed you."
