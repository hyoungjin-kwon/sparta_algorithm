seat_count = 9
vip_seat_array = [4, 7]
memo = {
    1: 1,
    2: 2
}


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    prev_fixed_index = 0
    count = 1
    for seat in fixed_seat_array:
        interval = seat - prev_fixed_index - 1
        prev_fixed_index = seat
        count *= fibo_dynamic_programming(interval, memo)
    interval = total_count - seat
    count *= fibo_dynamic_programming(interval, memo)

    return count


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_memo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_memo

    return nth_memo


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [2, 4, 7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11, [2, 5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10, [2, 6, 9]))
