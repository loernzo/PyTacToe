def get_coordinates(turn: bool)  -> int:
    player = 'Crosses' if turn else 'Circles'
    coordinates=input(player + ' (format: x, y): ')
    coordinates=coordinates.replace(' ', '')
    coordinates=coordinates.split(',')

    try:
        x=int(coordinates[0])
        y=int(coordinates[1])
    except ValueError:
        return 0,0

    except IndexError:
        try:
            x=int(coordinates[0][0])
            y=int(coordinates[0][1])
        except:
            return 0,0

    if x < 1 or y < 1:
        return -1, -1

    if x > 3 or y > 3:
        return 4, 4

    return x, y

def check (crosses: list, circles: list) -> int:
    coordinates=crosses
    winner=1
    for j in range(2):
        count=0
        draw_count=0

        for i in range(3):
            if len(coordinates[i])==3:
                return winner

            if i in coordinates[0] and i in coordinates[1] and i in coordinates[2]:
                return winner

            if i in coordinates[0] and i in coordinates[1] and i in coordinates[2]:
                return winner

            for n in coordinates[i]:
                if n+i+1==4:
                    count+=1
                if count==3:
                    return winner

            draw_count+=len(coordinates[i])
            if draw_count==5:
                return 0
                
        coordinates=circles
        winner=2

def drawchart(crosses: list, circles: list)  -> str:
    chart='    x 1     2     3\ny\n'
    for y in range(3):
        chart+=str(y+1)
        line=[]
        line[0:0]=crosses[y]
        line[0:0]=circles[y]
        line.sort()
        prev_x=0
        for x in line:
            for blank in range(x-prev_x):
                chart += '      ' if blank < x-prev_x-1 else '     '
            prev_x=x
            chart+='x' if x in crosses[y] else 'o'
        chart+='\n\n'
    return chart


def main():
    print("**Welcome to PyTacToe!**")
    turn=True
    crosses=[[],[],[]]
    circles=[[],[],[]]
    print(drawchart(crosses, circles))

    while True:

        x, y = get_coordinates(turn)
        if x==0:
            print('Invalid format!')
            continue
        elif x==-1:
            print('Minimum value is 0!')
            continue
        elif x==4:
            print('Maximum value is 3!')
            continue

        y-=1
        if x in crosses[y] or x in circles[y]:
            print('Spot taken!')
            continue

        if turn:
            crosses[y].append(x)
        else:
            circles[y].append(x)

        chart=drawchart(crosses, circles)
        print(chart)

        result = check(crosses, circles)
        if result==0:
            print('Draw!')
            exit()
        elif result==1:
            print('Crosses won!')
            exit()
        elif result==2:
            print('Circles won!')
            exit()

        turn = not turn

if __name__=='__main__' or __name__=='pytactoe':
    main()
