def e_squares(begin, end):
    squares = [x**2 for x in range(begin, end+1)]
    return squares

if __name__ == "__main__":
    begin_num = int(input("Enter begin num: "))
    end_num = int(input("Enter ending num: "))

    output = e_squares(begin_num, end_num)

    print(output)
