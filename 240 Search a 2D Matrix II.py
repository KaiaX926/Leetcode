class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target in matrix[i]:
                return  True
        return False
    
#################################################################################    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width, long = len(matrix[0]), len(matrix)
        path = [[False for i in range(width)] for i in range(long)]  
        print(len(path) == long, len(path[0]) == width)
        
        def around(i,j, status):
            loc = [[i-1,j], [i+1,j], [i, j-1], [i, j+1]]
            a = []
            for l in loc:
                if l[0] < long and l[1] < width and l[0] >= 0 and l[1] >= 0:
                    if path[l[0]][l[1]] == False:
                        a.append(l)
            if not a:
                return 
            v = [matrix[l[0]][l[1]] for l in a]
            if status == 'mini':
                return a[v.index(min(v))]
            else:
                return a[v.index(max(v))]
        
        def find(i,j,matrix):
            print(i,j)
            path[i][j] = True

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                ar = around(i,j, 'maxi')
                print(ar)
                if not ar:
                    return False
                return find(ar[0],ar[1],matrix)
            else:
                ar = around(i,j, 'mini')
                print(ar)
                if not ar:
                    return False
                return find(ar[0],ar[1],matrix)
            
                    
        return find(0,0,matrix)
