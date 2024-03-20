from square_generator import SquareGenerator
from cubic_generator import CubicGenerator


if __name__ == "__main__":
    begin_num = int(input("Enter begin num: "))
    end_num = int(input("Enter ending num: "))

    output = SquareGenerator.e_squares(begin_num, end_num)
    output_two = CubicGenerator.e_squares(begin_num, end_num)
    print(output)
    print(output_two)
