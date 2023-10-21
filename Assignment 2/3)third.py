#Getting the number of seconds from the user
seconds = int(input("Enter the seconds: "))

#Formula
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60


#Printing the result
print(f"{hours} hour(s), {minutes} minute(s), and {seconds} second(s).")