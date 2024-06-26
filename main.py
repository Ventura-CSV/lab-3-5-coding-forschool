def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """

    duplication = 0
    if num1 == num2 == num3:
        duplication = 3
    elif num1 == num2 or num2 == num3 or num1 == num2:
        duplication = 2
    else:
        duplicaiton = 0
        
    print(f'Duplication {duplication}')
    ########################################
    # Do not delete the return statement
    ########################################
    return duplication


if __name__ == '__main__':
    main()
