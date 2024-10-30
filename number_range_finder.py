#Define valid input: Inside range 1-50, must be numbers
#Create a list for every range 1-10, 11-20, 21-30, 31-40, 41-50
#Create a loop
    # Ask the user to input
    #Use if,else to find the range, and append to add input to list
#Use len() to count the numbers in range

def valid_input(number):
    try:
        number == int(number): #number must be integers
        if 1 >= number <= 50: #number must be 1 to 50
            return True
        return False
    except ValueError:
        return False
    
range_1_10 = []
range_11_20 = []
range_21_30 = []
range_31_40 = []
range_41_50 = []


