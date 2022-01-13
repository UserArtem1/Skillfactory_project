game_place='----------'#игровое поле
game_place_after = game_place
#- - -
#- - -
#- - -
print(game_place[0:3],game_place[3:6],game_place[6:-1],sep='\n')
count=1     #определение того ,кто ходит
new_place=''
while count != 9:
    if count % 2 == 1:
        print('Ходит крестик ')
        player_xod = int(input('Введите номер клетки от 1 до 9:'))
        #new_place=game_place_after[0:player_xod-1]+'x'+game_place_after[player_xod:]
        #i=game_place_after.index(game_place_after[player_xod])
        #game_place_after[i-1]=game_place_after.replace(game_place[player_xod], 'x', 1)
        if game_place_after[player_xod-1]=='o':
            print('Данная клетка уже занята.Введите номер другой клетки от 1 до 9:')
        else:
            count+=1
            new_place = game_place_after[0:player_xod - 1] + 'x' + game_place_after[player_xod:]
            print(new_place[0:3],new_place[3:6],new_place[6:-1],sep='\n')
            if (((new_place[0]=='x') and (new_place[4]=='x') and (new_place[8]=='x'))\
                or ((new_place[2]=='x') and (new_place[4]=='x') and (new_place[6]=='x'))\
                or (new_place[0:3]=='xxx') or (new_place[3:6]=='xxx') or (new_place[6:]=='xxx')\
                or ((new_place[0]=='x') and (new_place[3]=='x') and (new_place[6]=='x'))\
                or ((new_place[1]=='x') and (new_place[4]=='x') and (new_place[7]=='x'))\
                or ((new_place[2]=='x') and (new_place[5]=='x') and (new_place[8]=='x'))):
                print('Победил крестил')
                break
    else:
        print('Ходит нолик')
        player_xod = int(input('Введите номер клетки от 1 до 9:'))
        #new_place = game_place_after[0:player_xod - 1] + 'o' + game_place_after[player_xod:]
        #game_place_after[player_xod]=game_place_after.replace(game_place[player_xod], 'o', 1)
        if game_place_after[player_xod-1]=='x':
            print('Данная клетка уже занята.Введите номер другой клетки от 1 до 9:')
        else:
            count+=1
            new_place = game_place_after[0:player_xod - 1] + 'o' + game_place_after[player_xod:]
            print(new_place[0:3],new_place[3:6],new_place[6:-1],sep='\n')
            if (((new_place[0]=='o') and (new_place[4]=='o') and (new_place[8]=='o'))\
                or ((new_place[2]=='o') and (new_place[4]=='o') and (new_place[6]=='o'))\
                or (new_place[0:3]=='ooo') or (new_place[3:6]=='ooo') or (new_place[6:]=='ooo')\
                or ((new_place[0]=='o') and (new_place[3]=='o') and (new_place[6]=='o'))\
                or ((new_place[1]=='o') and (new_place[4]=='o') and (new_place[7]=='o'))\
                or ((new_place[2]=='o') and (new_place[5]=='o') and (new_place[8]=='o'))):
                print('Победил нолик')
                break
    game_place_after=new_place