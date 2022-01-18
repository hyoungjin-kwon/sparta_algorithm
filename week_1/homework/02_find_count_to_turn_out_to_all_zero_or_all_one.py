input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_change_from_zero_to_one = 0
    count_change_from_one_to_zero = 0

    # for initial value
    prev_state_for_zero = 0  # 0 if prev char is zero or 1 if prev char is one
    prev_state_for_one = 1  # 0 if prev char is zero or 1 if prev char is one
    if string[0]== '1':
        count_change_from_one_to_zero += 1
    else:
        count_change_from_zero_to_one += 1
    for char in string[1:]:
        if char == '1':
            if not prev_state_for_zero:
                count_change_from_one_to_zero += 1
        else:
            if prev_state_for_one:
                count_change_from_zero_to_one += 1
        prev_state_for_zero = int(char)
        prev_state_for_one = int(char)

    if count_change_from_zero_to_one < count_change_from_one_to_zero:
        return count_change_from_zero_to_one
    else:
        return count_change_from_one_to_zero


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)