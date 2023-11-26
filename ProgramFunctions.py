# Includes functions used in the main program


def CalcInsPremium(NumCars, ADDTL_CAR_DISC, BASIC_PREMIUM):
# Calculate the insurance premium based on the insurance option entered by the user

    if NumCars > 1:
        InsPremium = BASIC_PREMIUM + ((NumCars - 1) * ( 1 - ADDTL_CAR_DISC ) * BASIC_PREMIUM)
    else:
        InsPremium = BASIC_PREMIUM
    return InsPremium


def CalcMonthlyPay(PayOption, TotalCost, PROCESSING_FEE, DownPay):
# Calculate the monthly payment based on the payment option entered by the user

    if PayOption == "M": 
        MonthlyPay = ( TotalCost + PROCESSING_FEE ) / 8
    elif PayOption == "D":
        MonthlyPay = ( TotalCost + PROCESSING_FEE - DownPay ) / 8 
    else:
        MonthlyPay = 0
    return MonthlyPay
