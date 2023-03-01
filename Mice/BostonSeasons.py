seasons = int(input("Enter a season number: "))

if 4 <= seasons <= 6:
    print("Boston is in Spring")
elif 7 <= seasons <= 9:
    print("Boston is in Summer")
elif 10 <= seasons <= 11:
    print("Boston is in Autumn")
elif seasons == 12 or 1 <= seasons <= 3:
    print("Boston is in winter")
else:
    print("There are 12 months in a year")
    
