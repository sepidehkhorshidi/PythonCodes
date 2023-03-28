def check_even_odd(num):
    """Function to check if a number is even or odd"""
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

if __name__ == '__main__':
    # Take user input for a number
    num = int(input("Enter a number: "))
    
    # Call function to check if the number is even or odd
    check_even_odd(num)