def solution(arr):
    answer = [0,0]
    l = len(arr)

    def quad_tree(x,y,l):
        for i in range(x, x+l):
            for j in range(y, y+l):
                if arr[i][j] != arr[x][y]:
                    l = l//2
                    quad_tree(x,y,l)
                    quad_tree(x,y+l,l)
                    quad_tree(x+l,y,l)
                    quad_tree(x+l,y+l,l)
                    return
        answer[arr[x][y]] += 1
            
    quad_tree(0, 0, l)
    return answer
