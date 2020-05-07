def get_coordinates(turn: bool) -> int:
    player = 'Crosses' if turn else 'Circles'
    coordinates = input(player + ' (format: x, y): ')
    coordinates = coordinates.replace(' ', '')
    coordinates = coordinates.split(',')

    try:
        x = int(coordinates[0])
        y = int(coordinates[1])
    except ValueError:
        return 0, 0

    except IndexError:
        try:
            x = int(coordinates[0][0])
            y = int(coordinates[0][1])
        except:
            return 0, 0

    if x < 1 or y < 1:
        return -1, -1

    if x > 3 or y > 3:
        return 4, 4

    return x, y


def check(crosses: list, circles: list) -> int:
    coordinates = crosses
    winner = 1
    for j in range(2):
        count_1 = 0
        count_2 = 0
        draw_count = 0

        for y in range(3):

            # Horizontal tris check
            if len(coordinates[y]) == 3:
                return winner

            # Vertical tris check
            if y+1 in coordinates[0] and y+1 in coordinates[1] and y+1 in coordinates[2]:
                return winner

            # Top-left bottom-right tris check
            count_1 += 1 if y + 1 in coordinates[y] else 0
            if count_1 == 3:
                return winner

            # Top-right bottom-left tris check
            for n in coordinates[y]:
                count_2 += 1 if n + y + 1 == 4 else 0
                if count_2 == 3:
                    return winner

            draw_count += len(coordinates[y])
            if draw_count == 5:
                return 0

        coordinates = circles
        winner = 2


def drawchart(crosses: list, circles: list) -> str:
    # Draw top line
    chart = '    x 1     2     3\ny\n'
    for y in range(3):
        chart += str(y+1)
        line = []

        # Merge lines from both players
        line[0:0] = crosses[y]
        line[0:0] = circles[y]
        line.sort()
        prev_x = 0
        for x in line:
            # Draw as many blank lines as many empty spots are present.
            for blank in range(x - prev_x - 1):
                chart += '      '
            chart += '     '
            prev_x = x
            chart += 'x' if x in crosses[y] else 'o'
        chart += '\n\n'
    return chart


def main():
    print("**Welcome to PyTacToe!**")
    turn = True
    crosses = [[], [], []]
    circles = [[], [], []]
    print(drawchart(crosses, circles))

    while True:

        x, y = get_coordinates(turn)
        if x == 0:
            print('Invalid format!')
            continue
        elif x == -1:
            print('Minimum value is 0!')
            continue
        elif x == 4:
            print('Maximum value is 3!')
            continue

        y -= 1
        if x in crosses[y] or x in circles[y]:
            print('Spot taken!')
            continue

        if turn:
            crosses[y].append(x)
        else:
            circles[y].append(x)

        chart = drawchart(crosses, circles)
        print(chart)

        winner = check(crosses, circles)
        if winner == 0:
            print('Draw!')
            exit()
        elif winner == 1:
            print('Crosses won!')
            exit()
        elif winner == 2:
            print('Circles won!')
            exit()

        turn = not turn

if __name__ == '__main__' or __name__ == 'pytactoe':
    main()
