# todo:
# rewrite class methods
# sample
# create menu
# test menu
# adding new methods and classes

class Matrix:

    def __init__(self, n_row: int, n_col: int):

        self.n_col = n_col
        self.n_row = n_row
        self.mat_null = Matrix.nulls(self.n_row, self.n_col)
        self.mat_zero = Matrix.zeros(self.n_row, self.n_col)

    @staticmethod
    def zeros(n_row: int, n_col: int) -> list:
        return [[0 for i in range(n_col)] for i in range(n_row)]

    @staticmethod
    def nulls(n_row: int, n_col: int) -> list:
        return [[None for i in range(n_col)] for i in range(n_row)]

    def update_members(self, *args):

        if len(args) == self.n_col*self.n_row:
            index = 0
            for i in range(self.n_row):
                for j in range(self.n_col):
                    self.mat_null[i][j] = args[index]
                    index += 1
        else:
            raise Exception(
                "dimension error.please add a tuple having requiered number of arguments -->" + self.n_col*self.n_row)


    # to do :  add two matrix sample , menu
    def __add__(self, other: "object") -> "object":

        if self.n_col==other.n_col and self.n_row==other.n_row:
            sum_mat = Matrix(self.n_row, self.n_col)
            for i in range(self.n_row):
                for j in range(self.n_col):
                    sum_mat.mat[i][j] = self.mat[i][j]+other.mat[i][j]
        return sum_mat
    # to do : sample, menu

    def transpose(self) -> "object":

        trans_mat = Matrix(self.n_col, self.n_row)
        for i in range(self.n_row):
            for j in range(self.n_col):
                trans_mat.mat_null[j][i] = self.mat_null[i][j]
        return trans_mat

    @staticmethod
    def dot_prod(vec1: list, vec2: list) -> float:
        res = 0
        if len(vec1) == len(vec2):
            for i in range(len(vec1)):
                res += vec1[i]*vec2[i]
        return res

    # to do : sample, menu
    def __eq__(self, other: object) -> bool:

        if (self.n_row, self.n_col) == (other.n_row, other.n_col):
            for i in range(self.n_row):
                for j in range(self.n_col):
                    if self.mat_null[i][j] != other.mat_null[i][j]:
                        return False
            return True
        raise Exception("Dimension Error.")
    def __mul__(self, other: "object") -> "object":
        """
        return the result of multiplying a number and a Matrix Object.

        Parameters
        ----------
        other:"object"

        Returns
        -------
        a Matrix object

        """
        if self.n_col == other.n_row:
            res = Matrix(self.n_row, other.n_col)
            for i in range(self.n_row):
                for j in range(other.n_col):
                    res.mat[i][j] = Matrix.dot_prod(
                        self.mat[i], other.transpose().mat[j])
            return res
        raise Exception("Dimension Error.")

    # to do : sample, menu
    def __len__(self) -> int:

        return self.n_row*self.n_col
    def mul_num(self, num: float) -> object:
        """"
        return the result of multiplying a number and a Matrix Object.

        Parameters
        ----------
        num:float

        Returns
        -------
        A matrix object
        """
        new_mat = Matrix(self.n_row, self.n_col)
        for i in range(self.n_row):
            for j in range(self.n_col):
                new_mat.mat[i][j] = num*self.mat[i][j]
        return new_mat

        
    def __str__(self):
        print_mat = ""
        for i in range(self.n_row):
            for j in range(self.n_col):
                print_mat += f"{self.mat_null[i][j]}\t"
            print_mat += "\n"
        return print_mat
        
    # # to do : check,menu
    # def det_bast(self):
    #     new_mat = Matrix.zeros(self.n_row-1, self.n_col-1)
    #     i1 = 0
    #     index == 0
    #     new_mat.n_row == self.n_row-1
    #     new_mat.n_col == self.n_col-1
    #     sum = 1
    #     total = 0

    #     for j1 in range(self.n_col):
    #         for i in range(self.n_row):
    #             for j in range(self.n_col):
    #                 if i != i1 or j != j1:
    #                     args_exp[index] = self.mat[i][j]
    #                     index += 1
    #         index = 0
    #         for i in range(new_mat.n_row):
    #             for j in range(new_mat.n_col):
    #                 self.new_mat[i][j] = args[index]
    #                 index += 1
    #         sum = sum * (self.mat[i1][j1]*((-1) ^ (i1+1 + j1+1)))
    #         if new_mat.n_row != 2 or new_mat.n_col != 2:
    #             det_bast(new_mat)

    #         else:
    #             sum*((new_mat[0][0]*new_mat[1][1]) -
    #                  (new_mat[0][1]*new_mat[1][0]))
    #         total += sum
    #         return total



class Square(Matrix):
    """
    A class for creating square matrix and doing some related calculation.

    ...
    Attributes
    ----------
    n:int
        representing the number of rows and columns which are equal.

    Methods
    -------
    principal_diag()->list:
        retuen the principal diagonal of a Square matrix object as a list.
    secondary_diag(self)->list:
        retuen the secondary diagonal of a Square matrix object as a list.
    trace(self)->float:
        return the trace of a square matrix object.
    lu(self)->tuple:
        decompose a squre matrix to a upper triangular matrix and lower triangular matrix and return them in a tuple.
    det(self)->float:
        returning the determinent of a square matrix.
    """

    def __init__(self, n: int):
        super().__init__(n, n)

    def principal_diag(self) -> list:
        """
        return the principal diagonal of a Square matrix object as a list.

        parameters
        ----------

        Returns
        -------
        A list containg principal diagonal members
        """
        p_diag = []
        for i in range(self.n_row):
            p_diag.append(self.mat[i][i])
        return p_diag

    def secondary_diag(self) -> list:
        """
        retuen the secondary diagonal of a Square matrix object as a list.

        parameters
        ----------

        Returns
        -------
        A list containg secondary diagonal members
        """
        s_diag = []
        for i, j in enumerate(range(self.n_row-1, -1, -1)):
            s_diag.append(self.mat[i][j])
        return s_diag

    def trace(self) -> float:
        """
        return the trace of a square matrix object.

        Parameters
        ----------

        Returns
        -------
        A floate number representing sum of the principal diagonal of a squre matrix.
        """
        return sum(self.principal_diag())

    # A=LU
    def lu(self) -> tuple:
        """
        decompose a squre matrix to a upper triangular matrix and a lower triangular matrix and return them in a tuple.

        Parametres
        ----------

        Returns
        -------
        a tuple of Square object,(lower tiangular matrix,upper triangular matrix)
        """
        l = Square(self.n_row)
        u = Square(self.n_row)
        # step1
        for i in range(self.n_row):
            l.mat[i][i] = 1
        # step2
        for i in range(self.n_row):
            if i == 0:
                for j in range(self.n_row):
                    u.mat[i][j] = self.mat[i][j] - \
                        Matrix.dot_prod(l.mat[i], u.transpose().mat[j])
            else:
                for k in range(i):
                    l.mat[i][k] = (self.mat[i][k]-Matrix.dot_prod(l.mat[i],
                                                                  u.transpose().mat[k]))/(u.transpose().mat[k][k])
                for j in range(i, self.n_row):
                    u.mat[i][j] = self.mat[i][j] - \
                        Matrix.dot_prod(l.mat[i], u.transpose().mat[j])
        return l, u

    # determinant
    def det(self) -> float:
        """r
        returning the determinent of a square matrix.

        Parameters
        ----------

        Returns
        -------
        return a float number as determinent of a square matrix
        """
        l, u = self.lu()
        det = 1
        for i in range(self.n_row):
            det *= u.mat[i][i]
        return det


# ************************************
# Driver Code:


mat1 = Matrix(2, 3)
print(mat1.mat_null)
# [[None, None, None], [None, None, None]]
mat1 = Matrix(2, 3)
print(mat1.mat_zero)
# [[0, 0, 0], [0, 0, 0]]

mat1.update_members(1, 2, 3, 4, 5, 6)
print(mat1.__str__())
# 1       2       3
# 4       5       6
mat1 = Matrix(2, 3)
print(mat1.mat)
mat1.update_members(1, 2, 3, 4, 5, 6)
print(f"mat1=\n{mat1}")
print(f"transpose_mat1=\n{mat1.transpose()}")
print(f"len(mat1)={len(mat1)}")
print(f"mat1 * 2=\n{mat1.mul_num(2)}")

print("*"*50)

mat2 = Matrix(2, 3)
mat2.update_members(10, 20, 30, 40, 50, 60)
print(f"mat2=\n{mat2}")
print(f"transpose_mat2=\n{mat2.transpose()}")
print(f"len(mat2)={len(mat2)}")
print(f"mat1 * 0.5=\n{mat1.mul_num(0.5)}")


print("*"*50)
print(f"mat1+mat2=\n{mat1+mat2}")
print(f"mat1+mat2=\n{mat1*mat2}")
print(f"mat1*transpose_mat1=\n{mat1*mat1.transpose()}")
# ****************************************
print("*"*50)
square1 = Square(3)
square1.update_members(2, -1, 1, 1, 2, 1, -1, -4, 3)
l, u = square1.lu()
print(f"p_diag={square1.principal_diag()}")
print(f"s_diag={square1.secondary_diag()}")
print(f"tr(square1)={square1.trace()}")
print(f"lower_square1=\n{l}")
print(f"upper_square1=\n{u}")
print(f"det_square1={square1.det()}")
# ************************************
# MENU code:


def menu():

    option = 0
    while option != 6:
        print("1)write a matrix\n"
              "2)len matrix \n"
              "6)exit\n")
        option = int(input("choose option :"))
        if option == 1:
            n, m = input("enter n,m use space in between:").split()
            n = int(n)
            m = int(m)
            my_matris = Matrix.nulls(n, m)
            print(f"{my_matris} was added:")
            mount = tuple(
                input("please enter the arguments of your matrix without space:"))
            res = map(int, mount)
            print(mount, res)
            # Convert Tuple to integer
            # # Using int() + join() + map()

            # # printing result
            # print("Tuple to integer conversion : " + str(res))
            # ('1', '2', '3', '4', '5', '6')
            # ?
            my_matris = Matrix.update_members(mount)
            # ?
            # my_matris.update_members(1,2,3,4,5,6)
            # update_members(my_matris,mount)
            print(f"{my_matris.__str__()} was added:")
        # elif option == 2:
        #     print("the len of your matris is :", __len__(my_matris))
        #     #  ?
        else:
            print("invalid option")


menu()

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