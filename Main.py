from DecisionMaker import DecisionMaker
from Measures import *

def main():
    matrix = [
        [60, 66, 72, 78],
        [57, 70, 76, 82],
        [54, 67, 80, 86],
        [51, 64, 77, 90],
    ]

    for row in matrix:
        print(row)
    print("[Laplace]Profitable -> a%s" % (DecisionMaker.compute(matrix.copy(), LAPLACE) + 1))
    print("[Savage]Profitable -> a%s" % (DecisionMaker.compute(matrix.copy(), SAVAGE) + 1))
    print("[Hurwitz]Profitable -> a%s" % (DecisionMaker.compute(matrix.copy(), HURWITZ) + 1))

main()