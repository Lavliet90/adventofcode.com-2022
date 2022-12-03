file_number = open('input_data/day_2.txt', 'r')
# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

draw = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
win_combo = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
lose_combo = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]

# Y = draw, Z = win, X = lose
we_lose = {'A': 3, 'B': 1, 'C': 2}
we_win = {'A': 2, 'B': 3, 'C': 1}
we_draw = {'A': 1, 'B': 2, 'C': 3}

sum_point = 0
sum_point_2 = 0
for string in file_number:
    list_answer = string.split()
    elf_figure = list_answer[0]
    my_figure = list_answer[1]
    if my_figure == 'X':
        sum_point += 1
        sum_point_2 += we_lose.get(elf_figure)

    elif my_figure == 'Y':
        sum_point += 2
        sum_point_2 += 3 + we_draw.get(elf_figure)
    else:
        sum_point += 3
        sum_point_2 += 6 + we_win.get(elf_figure)

    if list_answer in draw:
        sum_point += 3
    elif list_answer in win_combo:
        sum_point += 6
    elif list_answer in lose_combo:
        sum_point += 0

print(sum_point)
print(sum_point_2)
