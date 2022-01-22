n = int(input())
preference = [[] for _ in range(n**2+1)]
order = [0 for _ in range(n**2)]
for i in range(n**2):
    my_input = list(map(int, input().split()))
    order[i] = my_input[0]
    preference[my_input[0]].append(my_input[1:])
room = [[0 for _ in range(n)] for _ in range(n)]

#해당 학생이 해당 칸 주위에 (좋아하는 학생 수, 비어있는 칸) return
def like_student(student, x, y):
    pref_count = 0
    empty_count = 0
    for coord in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx = x + coord[0]
        ny = y + coord[1]
        if 0 <= nx < n and 0 <= ny < n:
            if room[nx][ny] == 0:
                empty_count += 1
            else:
                if room[nx][ny] in preference[student][0]:
                    pref_count += 1
    return (pref_count, empty_count)

#비어있는 칸(인접한 좋아하는 학생 수, 인접한 비어있는 칸 수, 칸의 좌표) 목록 리턴
def rule1(student):
    candidate1 = []
    max_pref = 0
    for i in range(n):
        for j in range(n):
            if room[i][j] == 0:
                pref_count, empty_count = like_student(student, i, j)
                if pref_count > max_pref:
                    candidate1 = []
                    candidate1.append((pref_count, empty_count, i, j))
                    max_pref = pref_count
                elif pref_count == max_pref:
                    candidate1.append((pref_count, empty_count, i, j))
    return candidate1

def rule2_rule3(candidate1):
    candidate2 = []
    for cand in candidate1:
        pref_count, empty_count, i, j = cand
        candidate2.append((empty_count, i, j))
    candidate2.sort()
    max_empty = candidate2[-1][0]
    for cand in candidate2:
        if cand[0] == max_empty:
            return (cand[1], cand[2])

def happiness():
    total = 0
    for i in range(n):
        for j in range(n):
            pref_count, empty_count = like_student(room[i][j], i, j)
            if pref_count == 0:
                total += 0
            else:
                total += 10**(pref_count-1)
    return total

for i in range(n**2):
    student = order[i]
    first_step = rule1(student)
    if len(first_step) > 1:
        x, y = rule2_rule3(first_step)
        room[x][y] = student
    else:
        x, y = first_step[0][2], first_step[0][3]
        room[x][y] = student

print(happiness())
