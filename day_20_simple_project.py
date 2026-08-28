# ============================================DIGITAL CHECK GENERATOR=========================================
# PROBLEM STATEMENT
# ================You have been hired as a software intern for Apex Bank. The accounting department wants to automate their digital check printer. On a physical bank check,
#                  dollar amounts must be written in both numeric format (e.g., $123 ) and formal words (e.g., "One hundred twenty three dollars").
#                  Your manager has tasked you with writing a Python prototype script that prompts a bank teller for an integer check amount and converts it accurately into spoken words.
# =================================================================================


print("============================= WELCOME TO MY TEXT GENERATOR =============================")
print("Enter an amount between 0 to 999\n")


def firstNinteen(amu):

    if amu == 1:
        return "One"

    elif amu == 2:
        return "Two"

    elif amu == 3:
        return "Three"

    elif amu == 4:
        return "Four"

    elif amu == 5:
        return "Five"

    elif amu == 6:
        return "Six"

    elif amu == 7:
        return "Seven"

    elif amu == 8:
        return "Eight"

    elif amu == 9:
        return "Nine"

    elif amu == 10:
        return "Ten"

    elif amu == 11:
        return "Eleven"

    elif amu == 12:
        return "Twelve"

    elif amu == 13:
        return "Thirteen"

    elif amu == 14:
        return "Fourteen"

    elif amu == 15:
        return "Fifteen"

    elif amu == 16:
        return "Sixteen"

    elif amu == 17:
        return "Seventeen"

    elif amu == 18:
        return "Eighteen"

    elif amu == 19:
        return "Nineteen"


def Tens(amu):

    if amu == 2:
        return "Twenty"

    elif amu == 3:
        return "Thirty"

    elif amu == 4:
        return "Forty"

    elif amu == 5:
        return "Fifty"

    elif amu == 6:
        return "Sixty"

    elif amu == 7:
        return "Seventy"

    elif amu == 8:
        return "Eighty"

    elif amu == 9:
        return "Ninety"


def Hundreds(amu):

    if amu == 1:
        return "One Hundred"

    elif amu == 2:
        return "Two Hundred"

    elif amu == 3:
        return "Three Hundred"

    elif amu == 4:
        return "Four Hundred"

    elif amu == 5:
        return "Five Hundred"

    elif amu == 6:
        return "Six Hundred"

    elif amu == 7:
        return "Seven Hundred"

    elif amu == 8:
        return "Eight Hundred"

    elif amu == 9:
        return "Nine Hundred"

# INPUT

try:

    amount = int(input("Please Enter any Amount between 0 to 999: "))

except ValueError:

    print("ERROR: Invalid Input! Please enter numbers only.")

else:

    # VALIDATION

    if amount < 0 or amount > 999:

        print("ERROR: Amount must be between 0 and 999.")

    # ZERO

    elif amount == 0:

        print("Zero")

    # 1 TO 19

    elif amount < 20:

        print(firstNinteen(amount))

    # 20 TO 99

    elif amount < 100:

        tens = amount // 10
        ones = amount % 10

        if ones == 0:

            print(Tens(tens))

        else:

            print(Tens(tens), firstNinteen(ones))
    # 100 TO 999
    else:

        hundreds = amount // 100
        remaining = amount % 100

        if remaining == 0:

            print(Hundreds(hundreds))

        elif remaining < 20:

            print(Hundreds(hundreds), firstNinteen(remaining))

        else:

            tens = remaining // 10
            ones = remaining % 10

            if ones == 0:

                print(Hundreds(hundreds), Tens(tens))

            else:

                print(
                    Hundreds(hundreds),
                    Tens(tens),
                    firstNinteen(ones)
                )