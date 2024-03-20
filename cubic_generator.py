from square_generator import SquareGenerator
import math


class CubicGenerator(SquareGenerator):
    @staticmethod
    def e_squares(begin, end):
        if end < begin:
            begin, end = end, begin
            print("begin num was larger than ending num, so they were switched")
            # optionally = raise ValueError("begin num is larger tan ending num!")
        cubes = [(x, x ** 3) for x in range(begin, end + 1)]
        return cubes

    @staticmethod
    def e_squares(begin, end):
        if end < begin:
            begin, end = end, begin
            raise ValueError("begin num is larger tan ending num!")
        squares = [(x, math.sqrt(x)) for x in range(begin, end + 1)]
        return squares
