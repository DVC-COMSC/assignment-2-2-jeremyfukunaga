def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = float(input("Enter temperature in Celsius: "))

    # Conversion formula
    fahrenheit = (celsius * 9/5) + 32

    print("Fahrenheit: {:.2f}".format(fahrenheit))


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
