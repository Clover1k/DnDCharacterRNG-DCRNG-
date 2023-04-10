
#Clover1k DCRNG V1.2 4/9/2023, If you have any suggestions please tell me!

import time
import random
import numpy as np
import pandas as pd

#Begins the code

print('Hello and welcome to the Character Creator V1.2!')

while True:

    slctrc = input('What race? 1.Gnome 2.Human 3.Orc 4.Tabaxi 5.Elf 6.Dragonborn: ')
    chrctrnm = input('What is the name of the character to be created? ')
    chrctrbkgrnd = input('What is this character\'s background? ')
    chrctrclss = input('What is the character\'s class? ')

#Makes the random numbers

    traitnum = random.sample(range(1, 641), 3)
    traitnumf = iter(traitnum)

#Output

    if slctrc == '1':
        gnomesize = np.random.uniform(3, 3.5)
        gnomeskincol = ['Reddish Tan', 'Brown', 'Grey-ish Tan']
        gnomebeardcol = ['Reddish Tan', 'Brown', 'Grey-ish Tan', 'White']
        gnomebeardcolfinal = random.randint(0, 3)
        gnomeskincolfinal = random.randint(0, 2)
        gnomesizefinal = round(gnomesize, 1)

        traitfr = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

        print('Your character is... Drum roll please... Bum Bum Bum!')
        time.sleep(1)
        print(f'{chrctrnm} the {traitfr.iloc[0,0]} & {traitfr.iloc[1,0]} Gnome!')
        print(f'Class: {chrctrclss}')
        print(f'Background: {chrctrbkgrnd}')
        print('Specifics V')
        print('Eye Color: Blue')
        print(f'Size: {gnomesizefinal}ft')
        print(f'Skin Color: {gnomeskincol[gnomeskincolfinal]}')
        print(f'Beard color(If you want it to have a beard): {gnomebeardcol[gnomebeardcolfinal]}')
        rerun = input('Rerun? Y/N: ')

        if rerun == 'Y':
            print('Rerunning...')
            time.sleep(1)
            print(' ')
        elif rerun == 'N':
            print('Thank You for using the Character Creator V1.2 Beta!')
            break
        else:
            print('INVALID INPUT')
            break
    elif slctrc == '2':

        humanheight = np.random.uniform(5, 6.6)
        humanskincol = ['Black', 'White', 'Tan-ish', 'Caucasian']
        humanbeardcol = ['White', 'Black', 'Tan', 'Reddish Tan', 'Brown', 'Grey']
        humaneyecol = ['Blue', 'Gold', 'Yellow', 'Green', 'Brown']
        humanheightfinal = round(humanheight, 1)
        humanskincolfinal = random.randint(0, 3)
        humanbeardcolfinal = random.randint(0, 5)
        humaneyecolfinal = random.randint(0, 4)

        traitfrhuman = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

        print('Your character is... Drum roll please... Bum Bum Bum!')
        time.sleep(1)
        print(f'{chrctrnm} the {traitfrhuman.iloc[0,0]} & {traitfrhuman.iloc[1,0]} Human!')
        print(f'Class: {chrctrclss}')
        print(f'Background: {chrctrbkgrnd}')
        print('Specifics V')
        print(f'Eye Color: {humaneyecol[humaneyecolfinal]}')
        print(f'Size: {humanheightfinal}ft')
        print(f'Skin Color: {humanskincol[humanskincolfinal]}')
        print(f'Beard color(If you want it to have a beard): {humanbeardcol[humanbeardcolfinal]}')
        rerun = input('Rerun? Y/N: ')

        if rerun == 'Y':
            print('Rerunning...')
            time.sleep(1)
            print(' ')
        elif rerun == 'N':
            print('Thank You for using the Character Creator V1.2 Beta!')
            break
        else:
            print('INVALID INPUT')
            break

    elif slctrc == '3':

        orcsize = np.random.uniform(6, 7.1)
        orcskincol = ['Grey', 'Grey-ish Green', 'Green', 'Blue-ish Grey']
        orceyecol = ['Grey', 'Black', 'Grey', 'Black', 'Green']
        orcbeardcol = ['Black', 'Tan', 'Reddish Tan', 'Brown', 'Grey']
        orcskincolfinal = random.randint(0, 3)
        orcbeardcolfinal = random.randint(0, 4)
        orceyecolfinal = random.randint(0, 4)
        orcsizefinal = round(orcsize, 1)

        traitfrorc = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

        print('Your character is... Drum roll please... Bum Bum Bum!')
        time.sleep(1)
        print(f'{chrctrnm} the {traitfrorc.iloc[0,0]} & {traitfrorc.iloc[1,0]} Orc!')
        print(f'Class: {chrctrclss}')
        print(f'Background: {chrctrbkgrnd}')
        print('Specifics V')
        print(f'Eye Color: {orceyecol[orceyecolfinal]}')
        print(f'Size: {orcsizefinal}ft')
        print(f'Skin Color: {orcskincol[orcskincolfinal]}')
        print(f'Beard color(If you want it to have a beard): {orcbeardcol[orcbeardcolfinal]}')
        rerun = input('Rerun? Y/N: ')

        if rerun == 'Y':
            print('Rerunning...')
            time.sleep(1)
            print(' ')
        elif rerun == 'N':
            print('Thank You for using the Character Creator V1.2 Beta!')
            break
        else:
            print('INVALID INPUT')
            break

    elif slctrc == '4':

        tabaxisize = np.random.uniform(4, 6.9)
        tabaxifurcol = ['Tan', 'Lion-ish', 'Grey', 'Tortoise-Shell', 'Black', 'Orange Tabby', 'Grey Tabby', 'Siamese']
        tabaxieyecol = ['Yellow', 'Green', 'Blue', 'Brown']
        tabaxibeardcol = ['Tan', 'Black', 'Grey', 'Orange']
        tabaxisizefinal = round(tabaxisize, 1)
        tabaxifurcolfinal = random.randint(0, 7)
        tabaxibeardcolfinal = random.randint(0, 3)
        tabaxieyecolfinal = random.randint(0, 3)

        traitfrtabaxi = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

        print('Your character is... Drum roll please... Bum Bum Bum!')
        time.sleep(1)
        print(f'{chrctrnm} the {traitfrtabaxi.iloc[0,0]} & {traitfrtabaxi.iloc[1,0]} Tabaxi!')
        print(f'Class: {chrctrclss}')
        print(f'Background: {chrctrbkgrnd}')
        print('Specifics V')
        print(f'Eye Color: {tabaxieyecol[tabaxieyecolfinal]}')
        print(f'Size: {tabaxisizefinal}ft')
        print(f'Skin Color: {tabaxifurcol[tabaxifurcolfinal]}')
        print(f'Beard color(If you want it to have a beard): {tabaxibeardcol[tabaxibeardcolfinal]}')
        rerun = input('Rerun? Y/N: ')

        if rerun == 'Y':
            print('Rerunning...')
            time.sleep(1)
            print(' ')
        elif rerun == 'N':
            print('Thank You for using the Character Creator V1.2 Beta!')
            break
        else:
            print('INVALID INPUT')
            break
    
    elif slctrc == '5':
    
        elfheight = np.random.uniform(4, 7.5)
        elfskincol = ['Copper', 'Bronze', 'Bluish', 'White']
        elfeyecol = ['Blue', 'Green', 'Gold']
        elfbeardcol = 'None(Elfs cannot have beards)'
        elfheightfinal = round(elfheight, 1)
        elfskincolfinal = random.randint(0, 3)
        elfeyecolfinal = random.randint(0, 2)

        traitfrelf = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

        print('Your character is... Drum roll please... Bum Bum Bum!')
        time.sleep(1)
        print(f'{chrctrnm} the {traitfrelf.iloc[0,0]} & {traitfrelf.iloc[1,0]} Elf!')
        print(f'Class: {chrctrclss}')
        print(f'Background: {chrctrbkgrnd}')
        print('Specifics V')
        print(f'Eye Color: {elfeyecol[elfeyecolfinal]}')
        print(f'Size: {elfheightfinal}ft')
        print(f'Skin Color: {elfskincol[elfskincolfinal]}')
        print(f'Beard color(If you want it to have a beard): {elfbeardcol}')
        rerun = input('Rerun? Y/N: ')

        if rerun == 'Y':
            print('Rerunning...')
            time.sleep(1)
            print(' ')
        elif rerun == 'N':
            print('Thank You for using the Character Creator V1.2 Beta!')
            break
        else:
            print('INVALID INPUT')
            break

    elif slctrc == '6':

        dragonbornheight = np.random.uniform(6, 8.1)
        dragonbornskincol = ['Black', 'Blue', 'Bronze', 'Brass', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White']
        dragonbornbeardcol = ['Tan', 'Black', 'Grey', 'Orange', 'White']
        dragonborneyecol = ['Red', 'Gold', 'Black']
        dragonbornheightfinal = round(dragonbornheight, 1)
        dragonbornskincolfinal = random.randint(0, 9)
        dragonbornbeardcolfinal = random.randint(0, 4)
        dragonborneyecolfinal = random.randint(0, 2)


        traitfrdrgn = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

        print('Your character is... Drum roll please... Bum Bum Bum!')
        time.sleep(1)
        print(f'{chrctrnm} the {traitfrdrgn.iloc[0,0]} & {traitfrdrgn.iloc[1,0]} Dragonborn!')
        print(f'Class: {chrctrclss}')
        print(f'Background: {chrctrbkgrnd}')
        print('Specifics V')
        print(f'Eye Color: {dragonborneyecol[dragonborneyecolfinal]}')
        print(f'Size: {dragonbornheightfinal}ft')
        print(f'Skin Color: {dragonbornskincol[dragonbornskincolfinal]}')
        print(f'Beard color(If you want it to have a beard): {dragonbornbeardcol[dragonbornbeardcolfinal]}')
        rerun = input('Rerun? Y/N: ')

        if rerun == 'Y':
            print('Rerunning...')
            time.sleep(1)
            print(' ')
        elif rerun == 'N':
            print('Thank You for using the Character Creator V1.2 Beta!')
            break
        else:
            print('INVALID INPUT')
            break

    else:
        print('INVALID SELECTION, WHAT YOU SELECTED MAY STILL BE UNDER CONSTRUCTION')