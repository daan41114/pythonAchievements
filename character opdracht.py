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
weapon_durability = 'weapon   100/1000'
bow_durability = 'bow   300/500'
special_ability2 = ('double jump')
print (naam)
print (level)
if level == 'lv 50':
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
print (weapon_durability)
print (bow)
print (bow_durability)
