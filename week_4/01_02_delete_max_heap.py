class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
    # 1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
    # 2. 맨 뒤에 있는 원소를 (원래 루트 노드)를 삭제한다.
    # 3. 변경된 노드와 자식 노드들을 비교한다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크면 자리를 바꿉니다.
    # 4. 자식 노드 둘 보다 부모 노드가 크거나 가장 바닥에 도달하지 않을 때까지 3. 과정을 반복합니다.
    # 5. 2에서 제거한 원래 루트 노드를 반환합니다.
    def delete(self):
        last_index = len(self.items) - 1
        cur_index = 1
        self.items[cur_index], self.items[last_index] = self.items[last_index], self.items[cur_index]
        prev_max = self.items.pop()

        # while True:
        while cur_index <= len(self.items) - 1:
            max_index = cur_index
            left_child_index = 2 * cur_index
            right_child_index = 2 * cur_index + 1
            if left_child_index <= len(self.items) - 1 and self.items[max_index] < self.items[left_child_index]:
                max_index = left_child_index
            if right_child_index <= len(self.items) - 1 and self.items[max_index] < self.items[right_child_index]:
                max_index = right_child_index

            if cur_index == max_index:
                break
            self.items[max_index], self.items[cur_index] = self.items[cur_index], self.items[max_index]
            cur_index = max_index
            # max_child = max(self.items[2 * cur_index], self.items[2 * cur_index + 1])
            # if self.items[cur_index] < max_child:
            #     max_child_index = list.index(max_child)
            #     self.items[cur_index], self.items[max_child] = self.items[max_child], self.items[cur_index]
            #     cur_index = max_child_index
            # else:
            #     break
        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]