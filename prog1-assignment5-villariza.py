#Program inception for the clarification of this system program.
print("\n\033[1mThe\033[0m \033[31;1mPUP Student Handbook 2014\033[0m: \033[1m\x1B[3mSection 8. Grading System\x1B[0m")

#Def-function with a return value is used for this program method.
def exhibit_percentage():
    raw_grade = input("\nEnter your \033[92;1mInput Grade\033[0m in the provided text below. \n\033[34;1mGrade\033[0m >\033[33;1m ")
    return raw_grade;

#Calling out the def function pertaining to the parameter of a global variable (input_grade).
input_grade = exhibit_percentage()

#Different pathways of if-elif statements are introduced in this section regarding the integer grades being inputted from the user.
if input_grade.replace(".","",1).isdigit() == True:
    final_grade = round(float(input_grade))
    if final_grade > 100:
        print(f"\n\033[0mThere is no such grade that exceeds the maximum grade of \033[92;1m100\033[0m. \nYour \033[92;1mInput Grade\033[0m as shown.: \033[94;1m{final_grade}\033[0m\n")
    elif final_grade >= 97 or final_grade == 100:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m1.0\033[0m \nDescription: \033[35;1mExcellent\033[0m\n")
    elif final_grade >= 94 or final_grade == 96:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m1.25\033[0m \nDescription: \033[35;1mExcellent\033[0m\n")
    elif final_grade >= 91 or final_grade == 93:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m1.5\033[0m \nDescription: \033[35;1mVery Good\033[0m\n")
    elif final_grade >= 88 or final_grade == 90:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m1.75\033[0m \nDescription: \033[35;1mVery Good\033[0m\n")
    elif final_grade >= 88 or final_grade == 90:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m2.0\033[0m \nDescription: \033[35;1mGood\033[0m\n")
    elif final_grade >= 85 or final_grade == 87:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m2.25\033[0m \nDescription: \033[35;1mGood\033[0m\n")
    elif final_grade >= 82 or final_grade == 84:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m2.5\033[0m \nDescription: \033[35;1mSatisfactory\033[0m\n")
    elif final_grade >= 82 or final_grade == 84:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m2.75\033[0m \nDescription: \033[35;1mSatisfactory\033[0m\n")
    elif final_grade >= 79 or final_grade == 81:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m3.0\033[0m \nDescription: \033[35;1mPassing\033[0m\n")
    elif final_grade >= 65 or final_grade == 74:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1m5.0\033[0m \nDescription: \033[35;1mFailure\033[0m\n")
    elif final_grade >= 0 or final_grade == 64:
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{final_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m could be one of the following: \nDescription: \033[31;1mIncomplete\033[0m, \033[31;1mWithdrawn\033[0m, or \033[31;1mDropped\033[0m\n")
    elif final_grade <= -1:
        print(f"\n\033[0mYour \033[92;1mInput Grade\033[0m: \033[33;1m{input_grade}\033[0m, is not included in \033[1mThe\033[0m \033[31;1mPUP Student Handbook 2014\033[0m: \033[1m\x1B[3mSection 8. Grading System\x1B[0m \nPlease try again with the appropriate user input.\n")
#Included the three alphabetical grades (Inc., W, and D) with congruence in its specified description used into the program being inputted from the user.
else:
    peripheral_grade = input_grade.title()
    if input_grade == "INC." or input_grade == "Inc." or input_grade == "inc." or input_grade == "inc":
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{peripheral_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1mN/A\033[0m \nDescription: \033[31;1mIncomplete\033[0m\n")
    elif input_grade == "W" or input_grade == "w":
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{peripheral_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1mN/A\033[0m \nDescription: \033[31;1mWithdrawn\033[0m\n")
    elif input_grade == "D" or input_grade == "d":
        print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[33;1m{peripheral_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be: \033[34;1mN/A\033[0m \nDescription: \033[31;1mDropped\033[0m\n")
    else:
        print(f"\n\033[0mYour \033[92;1mInput Grade\033[0m: \033[33;1m{input_grade}\033[0m, is not included in \033[1mThe\033[0m \033[31;1mPUP Student Handbook 2014\033[0m: \033[1m\x1B[3mSection 8. Grading System\x1B[0m \nPlease try again with the appropriate user input.\n")