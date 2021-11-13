#Program inception for the clarification of this system program.
print("\nIn this \033[34;1mPython\033[0m \033[1m3.0\033[0m \033[33;1mLanguage\033[0m, the program will identify what digit or value is the \033[32;1m\x1B[3mlowest\x1B[0m between the \033[32;1mthree (3) statements\033[0m inputted from a user.")

#Def-function with a return value is used for this program method.
def exhibit_num(quantity1, quantity2, quantity3):
    if quantity1 < quantity2 and quantity1 < quantity3:
        return quantity1;
    elif quantity2 < quantity1 and quantity2 < quantity3:
        return quantity2;
    elif quantity3 < quantity1 and quantity3 < quantity2:
        return quantity3;

#Input of a user that is to be used for variables in if-else statements.
#The Supplementation of Python Color Class
digit1 = float(input("\n\033[0mEnter your \033[32;1mFIRST NUMBER\033[0m down below. \n\033[32;1m>>\033[0m \033[33;1m"))
digit2 = float(input("\n\033[0mEnter your \033[32;1mSECOND NUMBER\033[0m down below. \n\033[32;1m>>\033[0m \033[33;1m"))
digit3 = float(input("\n\033[0mEnter your \033[32;1mTHIRD NUMBER\033[0m down below. \n\033[32;1m>>\033[0m \033[33;1m"))

#A global variable calls out the result of the def function congruent to the parameter as positional argument (final_answer).
final_answer = exhibit_num(quantity1 = digit1, quantity2 = digit2, quantity3 = digit3)
print(f"\n\033[0mThe \033[32;1mLOWEST NUMBER\033[0m that you just inputted into the program is \033[33;1m{final_answer:,.2f}\033[0m.\n")