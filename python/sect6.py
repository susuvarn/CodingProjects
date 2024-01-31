# a=float(input("Enter value for a:"))
# b=float(input("Enter value for b:"))

# print("a+b: "+str(a+b))
# print("a-b: "+str(a-b))
# print("a*b: "+str(a*b))
# print("a/b: "+str(a/b))

# print("\nThat's all, folks!")

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
print("MINS:"+str(mins = mins + dura)) # find a total of all minutes
print("HOUR:"+str(hour = hour + mins)) // 60 # find a number of hours hidden in minutes and update the hour

mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')


