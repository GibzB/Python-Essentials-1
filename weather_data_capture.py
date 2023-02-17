# Imagine that you're developing a piece of software for an automatic weather station. 
# The device records the air temperature on an hourly basis and does it throughout the month. 
# This gives you a total of 24 × 31 = 744 values. 

# Deciding which data type would be adequate for this application. In this case, a float would be best


temps = [[0.0 for h in range(24)] for d in range(31)]

# Average Temperature at Noon
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Average temperature at noon:", average)


# highest temperature during the whole month
highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

# count the days when the temperature at noon was at least 20 Degrees Celcius
hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

