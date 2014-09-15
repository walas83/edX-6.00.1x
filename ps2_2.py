
balance = 999999
annualInterestRate = 0.18

def f(balance, minimumMonthlyPayment):
    for month in range(1, 13):
        monthlyInterestRate = (annualInterestRate) / 12.0
        monthlyUnpaidBalance = (balance) - minimumMonthlyPayment
        updatedBalanceEachMonth = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance) 
        balance = updatedBalanceEachMonth
    return balance

delta = 0.001
monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

while True:
    minimumMonthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2.0
    fret = f(balance, minimumMonthlyPayment)

    if  abs(fret) <= delta:
        break
    elif fret > 0:
        monthlyPaymentLowerBound = minimumMonthlyPayment
    else:
        monthlyPaymentUpperBound = minimumMonthlyPayment    
print 'Lowest Payment: ' + str(round(minimumMonthlyPayment,2))