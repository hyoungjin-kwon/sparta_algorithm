current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    room_map[r][c] = 2
    count = 1
    queue = [[r, c, d]]

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d
        for i in range(4):
            temp_d = (temp_d + 3) % 4
            new_r = r + dr[temp_d]
            new_c = c + dc[temp_d]
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                queue.append([new_r, new_c, temp_d])
                count += 1
                room_map[new_r][new_c] = 2
                break

            if i == 3:
                temp_d = (temp_d + 2) % 4
                new_r = r + dr[temp_d]
                new_c = c + dc[temp_d]

                if room_map[new_r][new_c] == 1:
                    return count
                else:
                    queue.append([new_r, new_c, d])
    #     r += dr[(r + 2) % 4]
    #     c += dc[(c + 2) % 4]
    #
    #     if d == next_d and room_map[r][c] == 1:
    #         break
    #     else:
    #         next_d = (next_d + 3) % 4
    #
    # return count


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 3, 1, current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7, 4, 1, current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 2, 0, current_room_map4))
