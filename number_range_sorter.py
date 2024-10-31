#Create a list for every range 1-10, 11-20, 21-30, 31-40, 41-50
#Create a loop
    # Ask the user to input
    #Use if,else to find the range, and append to add input to list
#Use len() to count the numbers in range

range_1_10 = []
range_11_20 = []
range_21_30 = []
range_31_40 = []
range_41_50 = []

while True:
    try:
        number = int(input("Please Enter a Number ranging from 1 to 50: "))
    except ValueError:
        print("Invalid Input! Enter Numbers ranging from 1 to 50.")
        continue

    if 1 <= number <= 50:
        if 1 <= number <= 10:
            range_1_10.append(number)
        elif 11 <= number <= 20:
            range_11_20.append(number)
        elif 21 <= number <= 30:
            range_21_30.append(number)
        elif 31 <= number <= 40:
            range_31_40.append(number)
        elif 41 <= number <= 50:
            range_41_50.append(number)
    else:
        print("Invalid Input! Now Leaving Number Range Sorter.")
        break

print(f"Range 1 to 10: ", len(range_1_10))
print(f"Range 11 to 20: ", len(range_11_20))
print(f"Range 21 to 30: ", len(range_21_30))
print(f"Range 31 to 40: ", len(range_31_40))
print(f"Range 41 to 50: ", len(range_41_50))