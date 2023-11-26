# Project: One Stop Insurance Company
# Author: Joseph Flores
# Due Date: November 28, 2023



# Import libraries (functions will be included in ProgramFunctions.py)

from datetime import date, datetime
import FormatValues as ForVal
import ProgramFunctions as ProgFunc
import DateValues as DateVal


# Constants

POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
ADDTL_CAR_DISC = 0.25
XLIA_COVE_RPC = 130.00
GLASS_COVE_RPC = 86.00
LOANER_CAR_COVE_RPC = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99


# Main Program


while True: 
    
    # Input

    print()
    print()
    print("--- CUSTOMER INFORMATION ---")
    while True:
        print()
        FirstName = input("First name:                     ").title()
        FirstNameStrip = FirstName.strip()
        if FirstNameStrip.replace(" ","").isalpha() and str(FirstName) != '':
            break
        else:
            print()
            print("FIRST NAME IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

    while True:
        print()
        LastName = input("Last name:                      ").title()
        LastNameStrip = LastName.strip()
        if LastNameStrip.replace(" ","").isalpha() and str(LastName) != '':
            break
        else:
            print()
            print("LAST NAME IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

    while True:
        print()
        Address = input("Street Address:                 ").title()
        if str(Address) != '':
            break
        else:
            print()
            print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

    while True:
        print()
        City = input("City:                           ").title()
        if str(City) != '':
            break
        else:
            print()
            print("CANNOT BE BLANK. PLEASE TRY AGAIN.")

    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
    while True:
        print()
        Province = input("Province (XX):                  ").upper()
        print()
        if Province == "":
            print("PROVINCE CANNOT BE BLANK. PLEASE TRY AGAIN.")
        elif len(Province) != 2:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
        elif Province not in ProvLst:
            print("INVALID PROVINCE. PLEASE TRY AGAIN.")
        else:
            break

    while True:
        PostalCode = input("Postal code (A1A1A1):           ").upper()
        if len(PostalCode) != 6:
            print()
            print("POSTAL CODE IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
            print()
            continue
        PostNum = PostalCode[1] + PostalCode[3] + PostalCode[5]
        PostLet = PostalCode[0] + PostalCode[2] + PostalCode[4]
        if PostNum.isdigit() and PostLet.isalpha():
            break
        else:
            print()
            print("POSTAL CODE IS INVALID. PLEASE TRY AGAIN.")
            print()

    while True:
        print()
        PhoneNumber = input("Enter phone number (10-digits): ")
        PhoneNumberSet = PhoneNumber.replace("-","").replace(" ","").replace("(","").replace(")","")
        if PhoneNumberSet.isnumeric() and len(PhoneNumberSet) == 10:
            break
        else:
            print()
            print("PHONE NUMBER IS INVALID OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

    print()
    print()
    print("--- INSURANCE INFORMATION ---")
    while True:
        try:
            print()
            NumCars = int(input("Please enter the number of cars to insure:              "))
        except ValueError:
            print()
            print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
        else:
            if NumCars > 0:
                break
            else:
                print()
                print("SHOULD BE GREATER THAN ZERO. PLEASE TRY AGAIN.")

    while True:
        print()
        ExtraLiability = input("Would you like to add extra liability insurance? (Y/N): ").upper()
        if ExtraLiability == "Y" or ExtraLiability == "N":
            break   
        else:
            print()
            print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

    while True:
        print()
        GlassCoverage = input("Would you like to add glass coverage? (Y/N):            ").upper()
        if GlassCoverage == "Y" or GlassCoverage == "N":
            break   
        else:
            print()
            print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")

    while True:
        print()
        LoanerCar = input("Would you like to add loaner car coverage? (Y/N):       ").upper()
        if LoanerCar == "Y" or LoanerCar == "N":
            break   
        else:
            print()
            print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
    print()
    print()
    print("--- PAYMENT INFORMATION ---")
    print()
    print("The payment options are:")
    print("F - Full payment")
    print("M - Monthly payment with zero downpayment")
    print("D - Monthly payment with downpayment")
    PayOpList = ["F", "M", "D"]
    while True:
        print()
        PayOption = input("How would you like to pay (F/M/D):    ").upper()
        if PayOption == "":
            print()
            print("CANNOT BE BLANK. PLEASE TRY AGAIN.")
        elif PayOption not in PayOpList:
            print()
            print("INVALID INPUT. PLEASE TRY AGAIN.")
        else:
            break

    DownPay = 0
    if PayOption == "D":
            while True:
                print()
                try:
                    DownPay = float(input("Please enter the down payment:        "))
                    if DownPay < 0 or DownPay == "":
                        print()
                        print("INVALID INPUT OR CANNOT BE BLANK. PLEASE TRY AGAIN.")
                    else:
                        break
                except ValueError:
                    print()
                    print("INVALID INPUT. PLEASE TRY AGAIN.")

    counter = 0
    DateClaimSt = []
    CostClaimSt = []
    print()
    print()
    print("--- CLAIM INFORMATION ---")
    print()
    print("If there are no claims, just press enter.")
    while True:
        print()    
        DateClaim = input("Date of claim (YYYY-MM-DD):           ")
        if DateClaim == "":
            break
        try:
            datetime.strptime(DateClaim, "%Y-%m-%d")
        except ValueError:
            print()
            print("INVALID DATE. PLEASE TRY AGAIN.")
            continue
        DateClaimSt.insert(counter, DateClaim)
        while True:
            try:
                print()
                CostClaim = float(input("Cost of the claim:                    "))
                if CostClaim < 0:
                    print()
                    print("CANNOT BE NEGATIVE. PLEASE TRY AGAIN.")
                else:
                    break
            except ValueError:
                print()
                print("INVALID INPUT. PLEASE TRY AGAIN.")
        CostClaimSt.insert(counter,CostClaim)
        counter += 1


    # Computation / Processing

    Today = date.today()

    InsPremium = ProgFunc.CalcInsPremium(NumCars, ADDTL_CAR_DISC, BASIC_PREMIUM)

    TotalExtraCost = 0
    XLiaCoveCost = 0
    GlassCoveCost = 0
    LoanerCarCoveCost = 0

    if ExtraLiability == "Y":
        XLiaCoveCost = XLIA_COVE_RPC * NumCars
    if GlassCoverage == "Y":
        GlassCoveCost = GLASS_COVE_RPC * NumCars
    if LoanerCar == "Y":
        LoanerCarCoveCost = LOANER_CAR_COVE_RPC * NumCars

    TotalExtraCost = XLiaCoveCost + GlassCoveCost + LoanerCarCoveCost


    HST =  (InsPremium + TotalExtraCost) * HST_RATE 
    TotalCost = InsPremium + TotalExtraCost + HST

    MonthlyPay = ProgFunc.CalcMonthlyPay(PayOption, TotalCost, PROCESSING_FEE, DownPay)


    # Output

    print()
    print()
    print()
    print(f"============================================================")
    print(f"                 One Stop Insurance Company                 ")
    print(f"============================================================")
    print()
    print(f"")
    print(f"Date: {ForVal.FDateS(Today):>10s}                         Policy Number: {POLICY_NUMBER}")
    print()
    print(f"CUSTOMER DETAILS:")
    print()
    print(f"  Name        : {FirstName} {LastName}")
    print(f"  Address     : {Address}")
    print(f"                {City}, {Province}, {PostalCode}")
    print(f"  Phone Number: {ForVal.FPhoneNum(PhoneNumberSet):>13s}")
    print()
    print()
    print(f"INSURANCE DETAILS:")
    print()
    print(f"Number of Cars: {NumCars:<4d}          Extra Liability Insurance: {ForVal.FYesNo(ExtraLiability):>3s}")
    print(f"                              Glass Coverage:            {ForVal.FYesNo(GlassCoverage):>3s}")
    print(f"                              Loaner Car Coverage:       {ForVal.FYesNo(LoanerCar):>3s}")
    print()
    print()
    print("DETAILED COMPUTATION OF INSURANCE COST:")
    print()
    print(f"Insurance Premium:                                {ForVal.FDollar2(InsPremium):>10s}")
    print(f"  Basic Rate ({ForVal.FDollar2(BASIC_PREMIUM):<7s} x {NumCars:>2d} car/s): {ForVal.FDollar2(BASIC_PREMIUM * NumCars):>10s}")
    if NumCars > 1:
        print(f"  Discount for additional cars   : {ForVal.FDollar2((NumCars - 1) * -ADDTL_CAR_DISC  * BASIC_PREMIUM):>10s}")
    print()
    if TotalExtraCost > 0:
        print(f"Extra Cost:                                       {ForVal.FDollar2(TotalExtraCost):>10s}")
        if ExtraLiability == "Y":
            print(f"  Liability Insurance ({ForVal.FDollar0(XLIA_COVE_RPC):<4s} /car): {ForVal.FDollar2(XLiaCoveCost):>10s}")
        if GlassCoverage == "Y":
            print(f"  Glass Coverage      ({ForVal.FDollar0(GLASS_COVE_RPC):<4s} /car): {ForVal.FDollar2(GlassCoveCost):>10s}")
        if LoanerCar == "Y":
            print(f"  Loaner Car Coverage ({ForVal.FDollar0(LOANER_CAR_COVE_RPC):<4s} /car): {ForVal.FDollar2(LoanerCarCoveCost):>10s}")
        print()
    print(f"                                                  ----------")
    print(f"Subtotal:                                         {ForVal.FDollar2(InsPremium + TotalExtraCost):>10s}")
    print(f"HST:                                              {ForVal.FDollar2(HST):>10s}")
    print(f"                                                  ----------")
    print(f"Total Cost:                                       {ForVal.FDollar2(TotalCost):>10s}")
    print()
    print()
    print(f"PAYMENT DETAILS:")
    print()
    if PayOption == "F":
        print(f"Paid in full.")
    else:
        if DownPay <= TotalCost:
            print(f"  Payment option:       Monthly")
            print(f"  Downpayment:          {ForVal.FDollar2(DownPay):<10s}")
            print(f"  Monthly payment:      {ForVal.FDollar2(MonthlyPay):<10s}")
            FirstNextMonth = DateVal.GetFirstNextMonth()
            print(f"  First payment due on: {ForVal.FDateS(FirstNextMonth):>10s}")
            print()
            print(f"  Notes:")
            print(f"    1. A {ForVal.FDollar2(PROCESSING_FEE)} processing fee will apply.")
            print(f"    2. Payments are due on the first day of each month.")
            print(f"    3. If not paid in full, insurance cost is payable")
            print(f"       within 8 months.")
        else:
            Refund = DownPay - TotalCost
            PayOption = "F"
            print("Since the downpayment is greater than the total cost,")
            print("the payment option will be changed to full payment.")
            print("The refund amount is ", ForVal.FDollar2(Refund),".")
        
    print()
    print()
    if counter !=0:
        print(f"------------------------------------------------------------")
        print()
        print(f"PAST CLAIM DETAILS:")
        print()
        print(f"        Claim #     Claim Date               Amount ")
        print(f"        --------------------------------------------")
        for i in range(counter):    
            DateClaimSt[i] = datetime.strptime(DateClaimSt[i], "%Y-%m-%d")
            print(f"           {i+1:<9d}{ForVal.FDateS(DateClaimSt[i]):<18s}{ForVal.FDollar2(CostClaimSt[i]):>14s}")

    print()
    print("============================================================")    
    print()
    print()
    Repeat = input("If you would like to enter another policy, please press Y. Otherwise, press any key to exit. ").upper()
    if Repeat != "Y":
        print()
        print("Thank you for using the One Stop Insurance Company.")
        print()
        break

# End of Program