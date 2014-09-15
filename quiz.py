print("Please think of a number between 0 and 100!")
low = 0
high = 100
answer = ''
while True:
    secret_number = (high + low)/2
    print "Is your secret number " + str(secret_number) + "?"
    answer = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if answer == 'h':
       high = secret_number
    elif answer == 'l':    
       low = secret_number
    elif answer == 'c':
        break
    else:
        print "Sorry, I did not understand your input."
print "Game over. Your secret number was: " + str(secret_number)
