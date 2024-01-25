matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

dr=[-1,1,0,0]
dc = [0,0,1,-1]
r,c = 0,2
for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr <3 and 0<=nc <3:
                print(matrix[nr][nc])
