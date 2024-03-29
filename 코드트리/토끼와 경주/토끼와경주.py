import sys
import heapq


class Rabbit:
    def __init__(self, pid: int, d: int):
        self.pid = pid
        self.d = d
        self.score = 0
        self.jump_count = 0
        self.row = 0
        self.col = 0

    def __lt__(self, other):
        if self.jump_count != other.jump_count:
            return self.jump_count < other.jump_count
        if self.row + self.col != other.row + other.col:
            return self.row + self.col < other.row + other.col
        if self.row != other.row:
            return self.row < other.row
        if self.col != other.col:
            return self.col < other.col
        return self.pid < other.pid

    def __repr__(self):
        return f"[pid:{self.pid}, curr:({self.row}, {self.col}), d:{self.d}, score:{self.score}, jump:{self.jump_count}]"


import time

start = time.time()
sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/토끼와 경주/test.txt", "r")
Q = int(sys.stdin.readline())
first_op = list(map(int, sys.stdin.readline().split()))
N, M, P = first_op[1:4]

rabbit_dict = {}
rabbit_list = []
for i in range(P):
    pid = first_op[2 * i + 4]
    d = first_op[2 * i + 5]
    new_rabbit = Rabbit(pid, d)
    rabbit_dict[pid] = new_rabbit
    heapq.heappush(rabbit_list, new_rabbit)


def set_racer_rabbit() -> Rabbit:
    rabbit = heapq.heappop(rabbit_list)
    rabbit.jump_count += 1
    return rabbit


def move(rabbit: Rabbit):
    dr_dis = rabbit.d % (2 * N - 2)
    dc_dis = rabbit.d % (2 * M - 2)

    dr_list = [dr_dis, -1 * dr_dis, 0, 0]
    dc_list = [0, 0, dc_dis, -1 * dc_dis]

    next_list = []
    for dr, dc in zip(dr_list, dc_list):
        next_r = (rabbit.row + dr) % (2 * N - 2)
        next_c = (rabbit.col + dc) % (2 * M - 2)
        #
        # if next_r >= N:
        #     next_r = 2 * N - 2 - next_r
        #
        # if next_c >= M:
        #     next_c = 2 * N - 2 - next_c

        next_list.append([next_r, next_c])

    row, col = sorted(next_list, key=lambda x: (-(x[0] + x[1]), -x[0], -x[1]))[0]
    rabbit.row, rabbit.col = row, col
    for pid, r in rabbit_dict.items():
        if pid != rabbit.pid:
            r.score += row + col + 2


def add_score(jump_rabbit_pid_list, s):
    # jump_rabbit_list.sort(key=lambda r: (-(r.row + r.col), -r.row, -r.col, -r.pid))
    # rabbit = jump_rabbit_list[0]
    # rabbit.score += s
    # rabbit_list.extend(sorted(jump_rabbit_list, key=lambda r: (r.jump_count, r.row + r.col, r.row, r.col, r.pid)))
    # #
    jump_rabbits = [rabbit_dict[pid] for pid in jump_rabbit_pid_list]
    rabbit = sorted(jump_rabbits, key=lambda r: (-(r.row + r.col), -r.row, -r.col, -r.pid))[0]
    rabbit.score += s


for _ in range(Q - 1):
    op_list = list(map(int, sys.stdin.readline().split()))

    # 경주 진행
    if op_list[0] == 200:
        jump_rabbit_pid_list = []
        for _ in range(op_list[1]):
            rabbit = set_racer_rabbit()
            jump_rabbit_pid_list.append(rabbit.pid)
            move(rabbit)
            heapq.heappush(rabbit_list, rabbit)
        add_score(jump_rabbit_pid_list, op_list[2])

    # 이동거리 변경
    elif op_list[0] == 300:
        rabbit_dict[op_list[1]].d *= op_list[2]

    # 경기 끝
    else:
        winner = sorted(rabbit_dict.values(), key=lambda r: -r.score)[0]
        print(winner.score)

print(time.time() - start)
