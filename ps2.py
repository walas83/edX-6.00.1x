
balance = 4000 
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0
for month in range(1, 13):
    monthlyInterestRate= (annualInterestRate) / 12.0
    minimumMonthlyPayment = (monthlyPaymentRate) * (balance)
    monthlyUnpaidBalance = (balance) - (minimumMonthlyPayment)
    updatedBalanceEachMonth = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance) 
    total += minimumMonthlyPayment
    balance = updatedBalanceEachMonth
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2))
    print 'Remaining balance: ' + str(round(updatedBalanceEachMonth, 2))

print 'Total paid: ' + str(round(total,2 ))
print 'Remaining balance: '  + str(round(updatedBalanceEachMonth, 2))