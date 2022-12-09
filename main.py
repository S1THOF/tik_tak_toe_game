playground = ['', '', '', '', '', '', '', '', '']
win_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def draw_playground(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


def winner(state, combination):
    for (x, y, z) in combination:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == "x" or state[x] == "o"):
            return state[x]
    return ''


def game_process(playground):
    p1_name, p2_name = input("Имя первого игрока: "), input("Имя второго игрока: ")
    symbol = "x"
    draw_playground(playground)
    while winner(playground, win_combination) == '':

        if symbol == "x":
            current_step = p1_name
        else:
            current_step = p2_name

        index = input(f'Делайте ход, {current_step}: ')

        playground[index] = symbol
        draw_playground(playground)
        winner_kit = winner(playground, win_combination)
        if winner_kit != '':
            print(f'Победил, {winner_kit}!')

        symbol = "x" if symbol == 'o' else 'o'


game_process(playground)
