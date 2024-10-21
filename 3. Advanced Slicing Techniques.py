
# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90,
                 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

week_temperature = temperatures [7:14]
print(f" The second week temperatures wil be : {week_temperature}")

# Task 2: Extract all the temperatures above 100:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91,
                 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures.sort()
print (temperatures)
    
temperatur_over_100 = [ temp for temp in temperatures if temp >100 ]
print(f" the temperatur over 100 is :{temperatur_over_100}")
