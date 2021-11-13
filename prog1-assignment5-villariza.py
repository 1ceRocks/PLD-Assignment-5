#Program inception for the clarification of this system program.
print("\n\033[1mThe\033[0m \033[31;1mPUP Student Handbook 2014\033[0m: \033[1m\x1B[3mSection 8. Grading System\x1B[0m")

#Def-function with a return value is used for this program method.
def exhibit_percentage():
    raw_grade = round(float(input("\nEnter your \033[92;1mInput Grade\033[0m in the provided text below. \n\033[96;1mGrade\033[0m > ")))
    return raw_grade;

#Calling out the def function pertaining to the parameter of a global variable (input_grade).
input_grade = exhibit_percentage()

#Different pathways of if-elif statements are introduced in this section regarding the integer grades being inputted from the user.
if input_grade >= 97 or input_grade == 100:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m1.0\033[0m \nDescription: \033[35;1mExcellent\033[0m\n")
elif input_grade >= 94 or input_grade == 96:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m1.25\033[0m \nDescription: \033[35;1mExcellent\033[0m\n")
elif input_grade >= 91 or input_grade == 93:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m1.5\033[0m \nDescription: \033[35;1mVery Good\033[0m\n")
elif input_grade >= 88 or input_grade == 90:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m1.75\033[0m \nDescription: \033[35;1mVery Good\033[0m\n")
elif input_grade >= 85 or input_grade == 87:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m2.0\033[0m \nDescription: \033[35;1mGood\033[0m\n")
elif input_grade >= 82 or input_grade == 84:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m2.25\033[0m \nDescription: \033[35;1mGood\033[0m\n")
elif input_grade >= 79 or input_grade == 81:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m2.5\033[0m \nDescription: \033[35;1mSatisfactory\033[0m\n")
elif input_grade >= 76 or input_grade == 78:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m2.75\033[0m \nDescription: \033[35;1mSatisfactory\033[0m\n")
elif input_grade == 75:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m3.0\033[0m \nDescription: \033[35;1mPassing\033[0m\n")
elif input_grade >= 65 or input_grade == 74:
    print(f"\n\033[0mAccording to your provided \033[92;1mInput Grade\033[0m: \033[96;1m{input_grade}\033[0m \nYour \033[92;1mGrade/Mark\033[0m shall be \033[96;1m5.0\033[0m \nDescription: \033[35;1mFailure\033[0m\n")