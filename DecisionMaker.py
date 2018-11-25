from Measures import *

class DecisionMaker:
    
    # Receives matrix and measure then returns profitable.
    @staticmethod
    def compute(matrix, measure):
        if measure == LAPLACE:
            return DecisionMaker.__Laplace(matrix)
        elif measure == SAVAGE:
            return DecisionMaker.__Savage(matrix)
        elif measure == HURWITZ:
            return DecisionMaker.__Hurwitz(matrix)

    # Laplace measure.
    @staticmethod
    def __Laplace(matrix):
        values = []

        for row in matrix:
            values.append(sum(row)/len(row))

        return values.index(max(values))

    # Savage measure.
    @staticmethod
    def __Savage(matrix):
        max_col = []

        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            max_col.append(max(temp))

        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                matrix[j][i] = max_col[i] - matrix[j][i] 

        max_row = []
        for row in matrix:
            max_row.append(max(row))

        return max_row.index(min(max_row))

    # Hurwitz measure.
    @staticmethod
    def __Hurwitz(matrix):
        chance = 1 / len(matrix)

        min_max = []

        for row in matrix:
            min_max.append((min(row), max(row)))

        values = []

        for pair in min_max:
            values.append(chance * pair[1] + (1 - chance) * pair[0])
        
        return values.index(max(values))


