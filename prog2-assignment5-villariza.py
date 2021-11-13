#Def-function with a return value is used for this program method.
def exhibit_num(quantity1, quantity2, quantity3):
    if quantity1 < quantity2 and quantity1 < quantity3:
        return quantity1;
    elif quantity2 < quantity1 and quantity2 < quantity3:
        return quantity2;
    elif quantity3 < quantity1 and quantity3 < quantity2:
        return quantity3;

#Input of a user that is to be used for variables in if-else statements.
digit1 = float(input("\nEnter your FIRST NUMBER down below. \n> ")) #2
digit2 = float(input("\nEnter your SECOND NUMBER down below. \n> ")) #3
digit3 = float(input("\nEnter your THIRD NUMBER down below. \n> ")) #4

#A global variable calls out the result of the def function congruent to the parameter as positional argument (final_answer).
final_answer = exhibit_num(quantity1 = digit1, quantity2 = digit2, quantity3 = digit3)
print(f"\nThe lowest number that you just inputted into the program is {final_answer:,.2f}.\n")