class Matrix:
    def __init__(self, arr_1: list, arr_2: list):
        self.matr = [arr_1, arr_2]
        self.arr_1 = arr_1
        self.arr_2 = arr_2

    def __add__(self):
        mat = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.arr_1)):
            for j in range(len(self.arr_2)):
                mat[i][j] = self.arr_1[i][j] + self.arr_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i])for i in mat]))

    def __str__(self):
        return str(self.matr)


matrix = Matrix([[15, 8, 1],
              [5, 71, 43],
              [14, 5, 90]],
              [[19, 4, 22],
              [16, 23, 11],
              [19, 2, 7]])
print(matrix.__add__())
print(matrix)

# Не разобрался с заданием: каким образом необходимо перегрузить метод __str__, чтобы он выдавал матрицу в
# привычном виде, если изначально мы создаем класс Matrix, который собой уже представляет две разные матрицы?