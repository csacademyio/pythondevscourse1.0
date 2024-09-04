##24-hour clock
reminder = 12
current_time = 12
second_reminder = 14
new_current_time = 13

# Conditional Statement - Code that allows to execute an outbased on a comparision between two or more data points
# True, False

# if Statement
if (reminder == current_time) and not (new_current_time > second_reminder):
    print("Alarm has Triggered")
else:
    print("Alarm is Not Triggered")


print(new_current_time > second_reminder) #False
print(not(new_current_time > second_reminder))#True

##Tenrary Operator

alarm = "Alarm has Triggered" if current_time == reminder else "Alarm is Not Triggered"
#print(alarm)
## Step 1. Declare the outcome if the if statement (condition) is true
## Step 2. Write out the condition 
## Step 3. Write out the outcome if the if statement conditions are NOT true

#Logical Operators
##and 
##or 
#not - If something False - asking if this value is not false

