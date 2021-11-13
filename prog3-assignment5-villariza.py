#Math is imported because the floor string will be used.
import math

#Def-function with a return value is used for this program method.
#The Supplementation of Python Color Class
def exhibit_age():
    input_age = input("\nWhat is your \033[32;1m\x1B[3mcurrent age\x1B[0m right now? Please type it down below. \n\033[32;1m>>\033[0m \033[33;1m")
    return input_age;

#Calling out the def function pertaining to the parameter of a global variable (user_age).
user_age = exhibit_age()

#Different pathways of if-elif statements are introduced in this section regarding the user age being inputted on the program.
if user_age.replace(".","",1).isdigit() == True:
    final_age = math.floor(float(user_age))
    if final_age <= -1:
        print(f"\n\033[0mThere is no such \033[32;1mAge\033[0m as \033[33;1m{final_age}\033[0m which produces a \033[31;1m\x1B[3mnegative value\x1B[0m of integer. \nTherefore, the description is invalid.\n")
    elif final_age == 0 or final_age <= 12:
        print(f"\n\033[0mSince your \033[32;1mAge\033[0m is \033[33;1m{final_age}\033[0m; \nyour \033[34;1mdescription\033[0m would be: \033[36;1mKid\033[0m\n")
    elif final_age == 13 or final_age <= 17:
        print(f"\n\033[0mSince your \033[32;1mAge\033[0m is \033[33;1m{final_age}\033[0m; \nyour \033[34;1mdescription\033[0m would be: \033[36;1mTeen\033[0m\n")
    elif final_age == 18:
        print(f"\n\033[0mSince your \033[32;1mAge\033[0m is \033[33;1m{final_age}\033[0m; \nyour \033[34;1mdescription\033[0m would be: \033[36;1mDebut\033[0m\n")
    elif final_age >= 19:
        print(f"\n\033[0mSince your \033[32;1mAge\033[0m is \033[33;1m{final_age:,}\033[0m; \nyour \033[34;1mdescription\033[0m would be: \033[36;1mAdult\033[0m\n")
else:
    print(f"\n\033[0m\033[34;1mPython\033[0m cannot heed your request such as: \033[33;1m{user_age:}\033[0m. Please try again by inputting an \033[32;1m\x1B[3mappropriate value\x1B[0m\033[0m.\n")

