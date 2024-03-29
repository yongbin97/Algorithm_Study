
# 경주
# [토끼 선정]
# 명령어: 100
# 우선순위 높은 토끼를 뽑기
# 우선순위
#   1. 총 점프 횟수 낮은 순

#   2. 현재 서있는 (row, col)합 적은 순
#   3. row 낮은순
#   4. col 낮은 순
#   5. pid 낮은 순

# [경주 진행]
# 명령어: 200 K S
# 상하좌우 4개 방향으로 d_i 만큼 이동
# 이동 도중에 격자 벗어나면 반대 방향으로 1칸 이동
# 4개 위치 중 우선 순위 높은 칸으로 이동
# 우선 순위:
#   1. row + col 큰 칸
#   2. row 큰 칸
#   3. col 큰 칸
# 이동 한 칸이 (r, c)일 때 움직인 토끼 제외 r+c 만큼의 점수 획득
#
# K번의 턴이 끝난 후 우선순위 기준으로 정렬 후 가장 높은 토끼는 점수 S 추가
# 우선 순위:
#   1. row + col 큰 토끼
#   2. row 큰 토끼
#   3. col 큰 토끼
#   4. pid 큰 토끼

# *주의*: K번동안 한 번이라도 뽑혔던 토끼 중 가장 높은 토끼

# [이동거리 변경]
# 명령어: 300 pid_t L
# pid_t의 토끼의 이동거리를 L배 한다

# [최고의 토끼 선정]
# 명령어: 400
# 가장 점수가 높은 토끼 출력
