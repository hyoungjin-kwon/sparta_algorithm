numbers = [1, 1, 1, 1, 1]
target_number = 3
count = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array):
        if target == current_sum:
            global count
            count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - array[current_index])

get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(count)  # 5를 반환해야 합니다!
