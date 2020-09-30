naam = 'daan'
level = 'lv 50'
headgear = 'headgear   knight helmed'
bodygear = 'bodygear   caveman outfit'
boots = 'boots   strong boots'
special_ability = 'special_ability   dash attack'
headgear_level = 'headgear   lv 20'
bodygear_level = 'bodygear   lv 20'
boots_level = 'boots   lv 25'
weapon = 'weapon   master axe'
bow = 'bow   valkarie bow'
original_weapon_durability = 1000
weapon_durability = 100
original_bow_durability = 500
bow_durability = 300
special_ability2 = ('double jump')
print (naam)
print (level)
(special_ability) = True
if special_ability == True:
    special_ability = 'special_ability   dash attack'
    print (special_ability)
else:
    print (special_ability2)
print ("choose gear to upgrade")
print ('choose: headgear lv 20, bodygear lv 20 or boots lv 25')
print ('also you have to input it multible times for no reason')
if level == 'lv 50':
    input()
else:
    print ('to low level')
if input() == 'headgear':
    headgear_level = 'headgear   lv 21'
elif input() == 'bodygear':
    bodygear_level = 'bodygear   lv 21'
elif input() == 'boots':
    boots_level = 'boots   lv 26'
else:
    print ('quess your not upgrading')
print (headgear)
print (headgear_level)
print (bodygear)
print (bodygear_level)
print (boots)
print (boots_level)
print (weapon)
print (original_weapon_durability)
print ('----')
print (weapon_durability)
print (bow)
print (original_bow_durability)
print ('---')
print (bow_durability)
