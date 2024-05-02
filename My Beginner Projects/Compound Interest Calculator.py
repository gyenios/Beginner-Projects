# Compound Interest Calculator
# A = P(1+r/n)^t

def line():
    print(" ")

def comp_int_calc():
    print('COMPOUND INTEREST CALCULATOR')
    line()
    while True:
        p = float(input('Initial amount deposited(Principal)>> $ '))
        try:
            if p > 0:
                while True:
                    r = float(input('Rate of interest >> % '))
                    try:
                        if r > 0:
                            while True:
                                t = float(input('Period of investment(in years) >> '))
                                try:
                                    if t > 0:
                                        accum_rate = pow((1+(r/100)),t)
                                        A = p*accum_rate
                                        return [A,p,t]
                                    else:
                                        print('Period must be greater than 0 years')
                                        line()
                                except ValueError:
                                    print('Enter a valid period in numbers')
                                    line()
                        else:
                            print('Rate must be greater than 0%')
                            line()
                    except ValueError:
                        print('Enter a valid rate')
                        line()
            else:
                print('Principal must be greater than $ 0.00')
                line()
        except ValueError:
            print('Amount can only contain numbers')
            line()
            
def menu():
    print('''
            What would you like to do?
            [1] Re-run program
            [2] Exit
        ''')
    while True:
        option = int(input('Option >> '))
        try:
            if option == 1 or option == 2:
                if option == 2:
                    option = 0
                return bool(option)
            else:
                print('Invalid option. Enter 1 or 2')
        except ValueError:
            print('Enter an integer as option')
            
def main(option):
    while option:
        A,p,t = comp_int_calc()
        print(f'The compound interest on ${p:.2f} after {int(t)}years is ${(A-p):.2f}. The total amount is ${A:.2f}')
        option = menu()
main(True)
