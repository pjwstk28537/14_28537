import math


class SquareGenerator:
    @staticmethod
    def e_squares(begin, end):
        if end < begin:
            begin, end = end, begin
            print("begin num was larger than ending num, so they were switched")
            # optionally = raise ValueError("begin num is larger tan ending num!")
        squares = [(x, math.sqrt(x)) for x in range(begin, end + 1)]
        return squares


if __name__ == "__main__":
    begin_num = int(input("Enter begin num: "))
    end_num = int(input("Enter ending num: "))

    output = SquareGenerator.e_squares(begin_num, end_num)
    print(output)
