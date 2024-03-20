from square_generator import SquareGenerator


if __name__ == "__main__":
    begin_num = int(input("Enter begin num: "))
    end_num = int(input("Enter ending num: "))

    output = SquareGenerator.e_squares(begin_num, end_num)
    print(output)
