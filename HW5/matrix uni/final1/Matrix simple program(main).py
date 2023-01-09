#This is a test and simple menu of some project elements 
# from matrix_2 import Square
import pprint


class Matrix:

    def __init__(self) -> None:
        pass

    @staticmethod
    def Duct_tape(mat1, mat2):
        """
        Duct-tape mat2's columns to the right of mat1
        Return a new matrix.
        """
        retval = []
        for i in range(len(mat1)):
            r = mat1[i]
            newrow = r[:] + mat2[i]
            retval.append(newrow)
        return retval

    @staticmethod
    def from_vector(vector):
        """
        Convert a vector into a column matrix.
        """
        retval = []
        for r in vector:
            retval.append([r])
        return retval


    @staticmethod
    def getMatrixMinor(mat, i, j):
        return [row[:j] + row[j+1:] for row in (mat[:i]+mat[i+1:])]

    def getMatrixDeternminant(self, mat):
        # base case for 2x2 matrix
        if len(mat) == 2:
            return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

        determinant = 0
        for c in range(len(mat)):
            determinant += ((-1)**c)*mat[0][c] * \
                self.getMatrixDeternminant(self.getMatrixMinor(mat, 0, c))
        return determinant

    @staticmethod
    def transpose(mat):
        retval = []
        for c in range(len(mat[0])):
            newrow = []
            for r in range(len(mat)):
                newrow.append(mat[r][c])
            retval.append(newrow)
        return retval

    @staticmethod
    def eliminate(r1, r2, col, target=0):
        fac = (r2[col]-target) / r1[col]
        for i in range(len(r2)):
            r2[i] -= fac * r1[i]

    def gauss(self, a):
        for i in range(len(a)):
            if a[i][i] == 0:
                for j in range(i+1, len(a)):
                    if a[i][j] != 0:
                        a[i], a[j] = a[j], a[i]
                        break
                else:
                    raise ValueError("Matrix is not invertible")
            for j in range(i+1, len(a)):
                self.eliminate(a[i], a[j], i)
        for i in range(len(a)-1, -1, -1):
            for j in range(i-1, -1, -1):
                self.eliminate(a[i], a[j], i)
        for i in range(len(a)):
            self.eliminate(a[i], a[i], i, target=1)
        return a

    def inverse(self, a):
        tmp = [[] for _ in a]
        for i, row in enumerate(a):
            assert len(row) == len(a)
            tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
        self.gauss(tmp)
        ret = []
        for i in range(len(tmp)):
            ret.append(tmp[i][len(tmp[i])//2:])
        return ret

    @staticmethod
    def like_a_gauss(mat):
        """
        Changes mat into Reduced Row-Echelon Form.
        """
        # Let's do forward step first.
        # at the end of this for loop, the matrix is in Row-Echelon format.
        for i in range(min(len(mat), len(mat[0]))):
            # every iteration, ignore one more row and column
            for r in range(i, len(mat)):
                # find the first row with a nonzero entry in first column
                zero_row = mat[r][i] == 0
                if zero_row:
                    continue
                # swap current row with first row
                mat[i], mat[r] = mat[r], mat[i]
                # add multiples of the new first row to lower rows so lower
                # entries of first column is zero
                first_row_first_col = mat[i][i]
                for rr in range(i + 1, len(mat)):
                    this_row_first = mat[rr][i]
                    scalarMultiple = -1 * this_row_first / first_row_first_col
                    for cc in range(i, len(mat[0])):
                        mat[rr][cc] += mat[i][cc] * scalarMultiple
                break

        # At the end of the forward step
        print(mat)
        # Now reduce
        for i in range(min(len(mat), len(mat[0])) - 1, -1, -1):
            # divide last non-zero row by first non-zero entry
            first_elem_col = -1
            first_elem = -1
            for c in range(len(mat[0])):
                if mat[i][c] == 0:
                    continue
                if first_elem_col == -1:
                    first_elem_col = c
                    first_elem = mat[i][c]
                mat[i][c] /= first_elem
            # add multiples of this row so all numbers above the leading 1 is zero
            for r in range(i):
                this_row_above = mat[r][first_elem_col]
                scalarMultiple = -1 * this_row_above
                for cc in range(len(mat[0])):
                    mat[r][cc] += mat[i][cc] * scalarMultiple
            # disregard this row and continue
        print(mat)

    


class Menu:

    def __init__(self) -> None:

        self.oper = None
        self.num_row = None
        self.raw_matrix = None
        self.num_col = None
        self.matrix_operation = Matrix()
        self.run()


    def entry(self):
        print('| Welcome to matrix calculator')
        print('| Which operation do you want to do? ')
        print('|0 -> Det')
        print('|1 -> LU')
        print('|2 -> Inverse')
        print('|3 -> Elementry row operation')
        print('|4 -> RREF')
        print('|5 -> Transpose')
        print('|6 -> Print')
        self.oper = int(input('|'))

    def check_oper(self):
        if self.oper == 0:
            print('|->>', self.matrix_operation.getMatrixDeternminant(self.raw_matrix))
        elif self.oper == 1:
            pass
        elif self.oper == 2:
            print('|Result:')
            self.print_matrix(self.matrix_operation.inverse(self.raw_matrix))
        elif self.oper == 3:
            print('|Result:')
            self.matrix_operation.like_a_gauss(self.raw_matrix)
        elif self.oper == 4:
            vec = list(map(int, input('|Enter solution vector:').split()))
            col_mat = self.matrix_operation.from_vector(vec)
            duct_taped_matrix = self.matrix_operation.Duct_tape(self.raw_matrix,col_mat)
            self.matrix_operation.like_a_gauss(duct_taped_matrix)
        elif self.oper == 5:
            print('|Result:')
            self.print_matrix(self.matrix_operation.transpose(self.raw_matrix))
        elif self.oper == 6:
            self.print_matrix(self.raw_matrix)

    def init_matrix(self):
        self.raw_matrix = []
        self.num_row = int(input('|Enter the number of rows: '))
        self.num_col = int(input('|Enter the number of colums: '))
        print('|Enter your matrix: ')
        # taking 2x2 matrix from the user
        for i in range(self.num_row):
            row = list(map(int, input('|').split()))
            if len(row) is not self.num_col:
                for i in range(self.num_col - len(row)):
                    row.append(0)

            self.raw_matrix.append(row)

    @staticmethod
    def print_matrix(Mat):
        for row in Mat:
            print('       ', [round(x, 3)+0 for x in row])



    def run(self):
        self.entry()
        self.init_matrix()
        self.check_oper()

        


start = Menu()
