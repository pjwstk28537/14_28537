from square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    @staticmethod
    def e_squares(begin, end):
        if end < begin:
            begin, end = end, begin
            print("begin num was larger than ending num, so they were switched")
            # optionally = raise ValueError("begin num is larger tan ending num!")
        cubes = [(x, x ** 3) for x in range(begin, end + 1)]
        return cubes
