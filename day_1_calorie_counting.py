file_number = open('input_data/day_1.txt', 'r')

a = 0
max_sum = 0
przed_max_sum = 0
przed_przed_max_sum = 0
sum_last_number = 0

for string in file_number:
    if string != '\n':
        sum_last_number += int(string)
    else:
        if przed_przed_max_sum < sum_last_number:
            przed_przed_max_sum = sum_last_number
            if przed_max_sum < przed_przed_max_sum:
                przed_max_sum, przed_przed_max_sum = przed_przed_max_sum, przed_max_sum
                if max_sum < przed_max_sum:
                    max_sum, przed_max_sum = przed_max_sum, max_sum
        sum_last_number = 0

print(max_sum)
print(max_sum + przed_max_sum + przed_przed_max_sum)
