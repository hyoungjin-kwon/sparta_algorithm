k = 4  # 말의 개수

# chess_map = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]
# start_horse_location_and_directions = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 2, 0],
#     [2, 2, 2]
# ]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
chess_map = [
[0, 0, 2, 0],
[0, 0, 1, 0],
[0, 0, 1, 2],
[0, 2, 0, 0]
]
start_horse_location_and_directions = [
[1, 0, 0],
[2, 1, 2],
[1, 1, 0],
[3, 0, 1]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!

# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

# 말은 순서대로 이동합니다 -> 말의 순서에 따라 반복문
# 말이 쌓일 수 있습니다 -> 맵에 말이 쌓이는 걸 저장해놔야 합니다
# 쌓인 순서대로 이동합니다 -> stack 써야겠구나
# 현재 맵에 어떻게 말이 쌓일지를 저장하기 위해서는  chess map에  linked lkist
def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    current_stacked_horse_map = [
        [
            [] for _ in range(n)
        ] for _ in range(n)
    ]

    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)
    turn_count = 1

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]
            # 파란색이거나 맵을 나갔을 때
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 가기로 한 곳이 막혀있으면 안감
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_c][new_r].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c

            # 턴이 진행되는 중 말이 4개 이쌍 쌓이는 순간 게임이 종료된다
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count += 1
    #print(current_stacked_horse_map)

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다