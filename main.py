# Comment like a pro
# Purpose....To help the One Stop Insurance Company with a program to calculate new insurance information.
# Author.....Ian Reid
# Date...... December 8th 2021

import datetime

# Constants
MONTHS = 12

# Files
f = open("OSICDef.dat", "r")
PolNum = int(f.readline())
BasicPrem = float(f.readline())
DisCar = float(f.readline())
ExLiabCover = float(f.readline())
GlassCover = float(f.readline())
LoanCarCover = float(f.readline())
HSTRATE = float(f.readline())
ProcFeeMonthPay = float(f.readline())
f.close()

# Inputs
CustFirst = input("What is your first name?                               ")
CustFirst = CustFirst.title()
CustLast = input("What is your last name?                                ")
CustLast = CustLast.title()
Address = input("What is your address?                                  ")
Address = Address.title()
City = input("What city do you live in?                              ")
City = City.title()
Province = input("What province do you live in?                          ")
Province = Province.title()
PstlCde = input("What is your postal code?                              ")
PhNum = input("What is your phone number?                             ")
CarInsur = int(input("How many cars are being insured?                       "))
ExLiab = input("Would you like extra liability up to 1000000? (Y or N) ")
ExLiab = ExLiab.title()
GlassCoverage = input("Would you like glass coverage? (Y or N)                ")
GlassCoverage = GlassCoverage.capitalize()
LoanerCar = input("Would you like to loan your car? (Y or N)              ")
LoanerCar = LoanerCar.capitalize()
FullorMonthly = input("Would you like to pay in full or monthly? (F or M)     ")
FullorMonthly = FullorMonthly.capitalize()

# Loops
while True:
    if CarInsur == 1:
        TotalInsurPrem = BasicPrem
        break
    elif CarInsur > 1:
        TotalInsurPrem = BasicPrem + ((BasicPrem * DisCar) * CarInsur)
        break
    else:
        print("Invalid. Try again")

TotOptionsCosts = 0

# If statements
if ExLiab == "Y":
    TotalInsurPrem = TotalInsurPrem + ExLiabCover
    TotOptionsCosts = TotOptionsCosts + ExLiabCover
else:
    TotalInsurPrem = TotalInsurPrem

if GlassCoverage == "Y":
    TotalInsurPrem = TotalInsurPrem + GlassCover
    TotOptionsCosts = TotOptionsCosts + GlassCover
else:
    TotalInsurPrem = TotalInsurPrem

if LoanerCar == "Y":
    TotalInsurPrem = TotalInsurPrem + LoanCarCover
    TotOptionsCosts = TotOptionsCosts + LoanCarCover
else:
    TotalInsurPrem = TotalInsurPrem

# Processing
HST = TotalInsurPrem * HSTRATE
TotalInsurPrem_Tax = HST + TotalInsurPrem
TotOptionCosts = ExLiabCover + GlassCover + LoanCarCover

if FullorMonthly == "F":
    pass
elif FullorMonthly == "M":
    Months12Pay = (TotalInsurPrem_Tax + ProcFeeMonthPay / MONTHS)

# Dates
CurrentDate = datetime.datetime.now()

# Output
print()
print("-"*40)
print("      The One Stop Insurance Company ")
print("-"*40)
print("                Users Info")
print(f"Policy Number:              {PolNum:>10}")
print(f"First name:                 {CustFirst:>10}")
print(f"Last name:                  {CustLast:>10}")
print(f"Address:                    {Address:>10}")
print(f"City:                       {City:>10}")
print(f"Province:                   {Province:>10}")
print(f"Postal Code:                {PstlCde:>10}")
print(f"Phone number:               {PhNum:>10}")
print("-"*40)
print("              Policy Info")
print(f"Cars insured:               {CarInsur:>10}")

if ExLiab == "Y":
    print(f"Extra Liability:        {ExLiabCover:>14,.2f}")
else:
    print("Extra Liability:                     N")

if GlassCoverage == "Y":
    print(f"Glass Coverage:         {GlassCover:>14,.2f}")
else:
    print("Glass Coverage:                      N")

if LoanerCar == "Y":
    print(f"Loaner Coverage:        {LoanCarCover:>14,.2f}")
else:
    print("Loaner Coverage:                     N")
print(f"Total Options Cost:         {TotOptionCosts:>10,.2f}")
print("-"*40)
print("              Cost Info")
print(f"Policy Date:                 ", (CurrentDate.strftime("%d-%m-%y")))
print(f"Tax Amount:                 {HST:>10,.2f}")
print(f"Total Cost of Policy:       {TotalInsurPrem_Tax:>10,.2f}")
print("-"*40)
print("              Payment Info")
if FullorMonthly == "M":
    print(f"Policy Date:                 ", (CurrentDate.strftime("%d-%m-%y")))
    print(f"First Monthly Payment Date:  ", (CurrentDate.strftime("%d-%m-%y")))
    print(f"Monthly Payment Length:  {MONTHS:>13}")
    print(f"Monthly Payment Amount:  {Months12Pay:>13,.2f}")
    print("-"*40)
print()

# Policy.dat

f = open("Policy.dat", "a")
f.write(f"{PolNum}-{CustFirst[0]}-{CustLast[0]}, ")
f.write(f"{CustFirst}, ")
f.write(f"{CustLast}, ")
f.write(f"{Address}, ")
f.write(f"{City}, ")
f.write(f"{Province}, ")
f.write(f"{PstlCde}, ")
f.write(f"{PhNum}, ")
f.write(f"{CarInsur}, ")
f.write(f"{ExLiabCover}, ")
f.write(f"{GlassCover}, ")
f.write(f"{LoanCarCover}, ")
f.write(f"{FullorMonthly}, ")
f.write(f"{TotalInsurPrem_Tax:.2f}\n")
f.close()

PolNum = PolNum + 1

# OSICDef.dat updating
f = open("OSICDef.dat", "w")
f.write("{}\n".format(str(PolNum)))
f.write("{}\n".format(str(BasicPrem)))
f.write("{}\n".format(str(DisCar)))
f.write("{}\n".format(str(ExLiabCover)))
f.write("{}\n".format(str(GlassCover)))
f.write("{}\n".format(str(LoanCarCover)))
f.write("{}\n".format(str(HSTRATE)))
f.write("{}\n".format(str(ProcFeeMonthPay)))
f.close()
print("Thank you for using One Stop Insurance Company!")
print()

# Report 1
ViewReports = input("Press anything to view reports...")
print()
print("123456789012345678901234567890123456789012345678901234567890")
print()
print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTINGS AS OF", (CurrentDate.strftime("%d-%m-%y")))
print()
print("POLICY   CUSTOMER       INSURANCE   EXTRA   TOTAL")
print("NUMBER   NAME           PREMIUM     COSTS   PREMIUM")
print("="*55)
print()

PolicyCounter = 0

f = open("Policy.dat", "r")
for PolicydatLine in f:
    Policydat = PolicydatLine.split(",")
    reportPolNum = Policydat[0].strip()
    reportCustFirst = Policydat[1].strip()
    reportInsurPrem = Policydat[13].strip()
    reportTotOptionsCosts = Policydat[12].strip()
    reportInsurPrem_Tax = Policydat[13].strip()
    print("{:>4} {:>7} {:>19,.2f} {:>9,.2f} {:>9,.2f}".format(PolNum, CustFirst, TotalInsurPrem, TotOptionCosts, TotalInsurPrem_Tax))
    PolicyCounter += 1

f.close()
print("="*55)
print(f"Total Policies: {PolicyCounter}")
print()
ViewReports2 = input("Press anything to see the next report...")
print()

# Report 2
print("123456789012345678901234567890123456789012345678901234567890")
print()
print("ONE STOP INSURANCE COMPANY")
print("MONTHLY PAYMENT LISTING AS OF ", (CurrentDate.strftime("%d-%m-%y")))
print()
print("POLICY   CUSTOMER        TOTAL                TOTAL    MONTHLY")
print("NUMBER   NAME           PREMIUM      HST      COST     PAYMENT")
print("="*64)
print("="*64)
print(f"Total Policies: {PolicyCounter}")

