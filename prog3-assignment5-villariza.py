#Def-function with a return value is used for this program method.
def exhibit_age():
    input_age = float(input("\nWhat is your current age right now? Please type it down below. \n> "))
    return input_age;

#Calling out the def function pertaining to the parameter of a global variable (user_age).
user_age = exhibit_age()

#Different pathways of if-elif statements are introduced in this section regarding the user age being inputted on the program.
if user_age <= -1:
    print(f"\nThere is no such age as {user_age:,.0f} which produces a negative value of integer. \nTherefore, the description is invalid.\n")
elif user_age == 0 or user_age <= 12:
    print(f"\nSince your age is {user_age:,.0f}; your description would be: Kid\n")
elif user_age == 13 or user_age <= 17:
    print(f"\nSince your age is {user_age:,.0f}; your description would be: Teen\n")
elif user_age == 18:
    print(f"\nSince your age is {user_age}; your description would be: Debut\n")
elif user_age >= 19:
    print(f"\nSince your age is {user_age}; your description would be: Adult\n")
