finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    numbers.sort()

    cur_min = 0
    cur_max = len(numbers) - 1
    cur_guess = (cur_min + cur_max) // 2
    find_count = 0

    while cur_min <= cur_max:
        find_count += 1
        if numbers[cur_guess] == target:
            print(find_count)
            return True
        elif numbers[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)