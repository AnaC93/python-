class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([self.matrix[i][j] + other.matrix[i][j] for i in range(len(self.matrix))]
                      for j in range(len(self.matrix[0])))


rows = int(input("Enter the amount of rows and columns: "))
columns = rows


matrix_1 = Matrix([[i * j for j in range(rows)] for i in range(columns)])
matrix_2 = Matrix([[i + j for j in range(rows)] for i in range(columns)])


print('First matrix:\n', matrix_1, end='\n\n')
print('Second matrix:\n', matrix_2, end='\n\n')