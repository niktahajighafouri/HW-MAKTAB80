from sys import exit
def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x,3)+0 for x in row])
        
def print_matrices(Action, Title1, M1, Title2, M2):
    print(Action)
    print(Title1, '\t'*int(len(M1)/2)+"\t"*len(M1), Title2)
    for i in range(len(M1)):
        row1 = ['{0:+7.3f}'.format(x) for x in M1[i]]
        row2 = ['{0:+7.3f}'.format(x) for x in M2[i]]
        print(row1,'\t', row2)
        
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
        exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C





# def invert_matrix(A, tol=None):
#     """
#     Returns the inverse of the passed in matrix.
#         :param A: The matrix to be inversed
 
#         :return: The inverse of the matrix A
#     """
#     # Section 1: Make sure A can be inverted.
#     check_squareness(A)
#     check_non_singular(A)
 
#     # Section 2: Make copies of A & I, AM & IM, to use for row ops
#     n = len(A)
#     AM = copy_matrix(A)
#     I = identity_matrix(n)
#     IM = copy_matrix(I)
 
#     # Section 3: Perform row operations
#     indices = list(range(n)) # to allow flexible row referencing ***
#     for fd in range(n): # fd stands for focus diagonal
#         fdScaler = 1.0 / AM[fd][fd]
#         # FIRST: scale fd row with fd inverse. 
#         for j in range(n): # Use j to indicate column looping.
#             AM[fd][j] *= fdScaler
#             IM[fd][j] *= fdScaler
#         # SECOND: operate on all rows except fd row as follows:
#         for i in indices[0:fd] + indices[fd+1:]: 
#             # *** skip row with fd in it.
#             crScaler = AM[i][fd] # cr stands for "current row".
#             for j in range(n): 
#                 # cr - crScaler * fdRow, but one element at a time.
#                 AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
#                 IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
 
#     # Section 4: Make sure IM is an inverse of A with specified tolerance
#     if check_matrix_equality(I,matrix_multiply(A,IM),tol):
#         return IM
#     else:
#         raise ArithmeticError("Matrix inverse out of tolerance.")

A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
I = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
# print_matrix('A Matrix', A)
# print()
# print_matrix('I Matrix', I)

AM = copy_matrix(A)
IM = copy_matrix(I)
n = len(AM)

# exString = """
# Since the matrices won't be the original A and I as we start row operations, 
#     the matrices will be called: AM for "A Morphing", and IM for "I Morphing" 
# """
# print(exString)
# print_matrix('AM Matrix', AM)
# print()
# print_matrix('IM Matrix', IM)

# Run this cell then the next cell for fd = 0
# Then run for the remaining columns using cell 6
# Then check for identity matrix in cell 7.

fd = 0 # fd stands for focus diagonal OR the current diagonal
fdScaler = 1. / AM[fd][fd]

for j in range(n): # using j to indicate cycling thru columns
    AM[fd][j] = fdScaler * AM[fd][j]
    IM[fd][j] = fdScaler * IM[fd][j]

# print_matrix('AM Matrix', AM)
# print()
# print_matrix('IM Matrix', IM)


n = len(A)
indices = list(range(n))

for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
    crScaler = AM[i][fd] # cr stands for "current row".
    for j in range(n): # cr - crScaler * fdRow, but one element at a time.
        AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
        IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    
# print_matrix('AM Matrix', AM)
# print()
# print_matrix('IM Matrix', IM)

indices = list(range(n)) # to allow flexible row referencing ***
# We've already run for fd = 0, now let's run for fd = 1 to the last fd
for fd in range(1,n): # fd stands for focus diagonal
    fdScaler = 1.0 / AM[fd][fd]
    # FIRST: scale fd row with fd inverse. 
    for j in range(n): # Use j to indicate column looping.
        AM[fd][j] *= fdScaler
        IM[fd][j] *= fdScaler

# Section to print out current actions:
    string1 = '\nUsing the matrices above, Scale row-{} of AM and IM by '
    string2 = 'diagonal element {} of AM, which is 1/{:+.3f}.\n'
    stringsum = string1 + string2
    val1 = fd+1; val2 = fd+1
    Action = stringsum.format(val1,val2,round(1./fdScaler,3))

    # SECOND: operate on all rows except fd row.
for i in indices[:fd] + indices[fd+1:]: # *** skip row with fd in it.
        crScaler = AM[i][fd] # cr stands for "current row".
        for j in range(n): # cr - crScaler * fdRow, but one element at a time.
            AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
        
        # Section to print out current actions:
        string1 = 'Using the matrices above, subtract {:+.3f} * row-{} of AM from row-{} of AM, and \n'
        string2 = '\tsubtract {:+.3f} * row-{} of IM from row-{} of IM\n'
        val1 = i+1; val2 = fd+1
        stringsum = string1 + string2
        Action = stringsum.format(crScaler, val2, val1, crScaler, val2, val1)

A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
print_matrix('Proof of Inversion', matrix_multiply(A,IM))

def invert_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed
 
        :return: The inverse of the matrix A
    """
    # Section 1: Make sure A can be inverted.
    check_squareness(A)
    check_non_singular(A)
 
    # Section 2: Make copies of A & I, AM & IM, to use for row ops
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)
 
    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: 
            # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): 
                # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
 
    # Section 4: Make sure IM is an inverse of A with specified tolerance
    if check_matrix_equality(I,matrix_multiply(A,IM),tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")