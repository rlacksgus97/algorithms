def man_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def check(place,x,y):
    for i in range(-2,3):
        for j in range(3):
            if 0<=x+i<5 and 0<=y+j<5:
                if man_dist(x,y,x+i,y+j) == 1 and place[x+i][y+j] == 'P':
                    return False
                elif man_dist(x,y,x+i,y+j) == 2 and place[x+i][y+j] == 'P':
                    if i == 1 and j == 1:
                        if place[x+i-1][y+j] != 'X' or place[x+i][y+j-1] != 'X':
                            return False
                    if i == -1 and j == 1:
                        if place[x+i+1][y+j] != 'X' or place[x+i][y+j-1] != 'X':
                            return False
                    if i == 2 and j == 0:
                        if place[x+i-1][y+j] != 'X':
                            return False
                    if i == -2 and j == 0:
                        if place[x+i+1][y+j] != 'X':
                            return False
                    if i == 0 and j == 2:
                        if place[x+i][y+j-1] != 'X':
                            return False
                    
    return True

def valid(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not check(place,i,j):
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        if valid(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
