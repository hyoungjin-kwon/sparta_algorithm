def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if char.isalpha():
            arr_idx = ord(char)-ord('a')
            # print(idx)
            alphabet_occurrence_array[arr_idx] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))