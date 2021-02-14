import numpy as np

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.matrix = []

    def board(self):
        proba = []
        matrix = []
        cont = 0
        for i in self.sudoku:
            proba.append(i)
            cont += 1
            if cont == 9:
                self.matrix.append(proba)
                proba = []
                cont = 0
        return self.matrix

    def get_row(self, numero):
        self.numero = numero
        return self.matrix[self.numero]

    def get_col(self,columna):
        self.columna = columna
        col_list = []
        for i in range(0,9):
            col_list.append(self.matrix[i][self.columna])
        return col_list

    def get_sqr(self,posicion):
        self.posicion = posicion
        sqr = []
        if self.posicion == 0:
            sqr = self.matrix[0][0:3]
            sqr += self.matrix[1][0:3]
            sqr += self.matrix[2][0:3]
            return sqr
        elif self.posicion == 1:
            sqr = self.matrix[0][3:6]
            sqr += self.matrix[1][3:6]
            sqr += self.matrix[2][3:6]
            return sqr
        elif self.posicion == 2:
            sqr = self.matrix[0][6:9]
            sqr += self.matrix[1][6:9]
            sqr += self.matrix[2][6:9]
            return sqr


game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
print(game.board())
print(game.get_row(0))
print(game.get_col(8))
print(game.get_sqr(1))