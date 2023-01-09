class Matrix:

    def __init__(self , row:int , col:int) -> None:
        
        self.row = row
        self.col = col
        self.initialize_matrix()

    def initialize_matrix(self):
        mat = [[0 for m in range(self.row)] for n in range(self.col)]
        # print(f'matrix of dimension {self.row} x {self.col} is {mat}')

    

x = Matrix(8 , 5)

# n = 4
# matrix = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
# matrix = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
# print("The created matrix of {} * {}: ".format(n,n))
# # for m in matrix:
# print(matrix)

# initializing an empty matrix
matrix = []
# taking 2x2 matrix from the user
for i in range(2):
   # taking row input from the user
   row = list(map(int, input().split()))
   # appending the 'row' to the 'matrix'0
   matrix.append(row)
# printing the matrix
print(matrix)


# rows = 5
# cols = 10
 
# mat = [[0 for _ in range(cols)] for _ in range(rows)]
# print(f'matrix of dimension {rows} x {cols} is {mat}')
# for m in mat:
#     print(m)

