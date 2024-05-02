# CREDIT CARD VALIDATOR PROGRAM
def check_card():    
    # Take user input and process card number into suitable form for checking
    def get_card():
        card_no = input('Enter credit card number>> ')

        # Step 1 (Removing spaces and dashes)
        card_no = card_no.replace('-','')
        card_no = card_no.replace(' ','')
        print(f'Stripped: {card_no}')

        # Reversing the string
        card_no = card_no[::-1]
        print(f'Reversed: {card_no}')
        return card_no

    def validate(card_no):
        # Initializing variables to store sum of elements in odd and even positions
        odd_sum = 0
        even_sum = 0

        # Step 2
        for i in card_no[::2]: # Iterating through items in odd positions
            odd_sum += int(i) # Summing digits in odd positions 

        # Step 3
        for i in card_no[1::2]: # Iterating through items in even positions
            n = int(i) + int(i) # Doubling the value of each item in even position
            if n >= 10:
                even_sum += (1 + (n%10))
            else:
                even_sum += n

        # Step 4
        total = even_sum + odd_sum

        # Step 5
        if total % 10 == 0:
            print('VALID')
        else:
            print('INVALID')

    validate(get_card())        

def main():
    print('''
               *** CREDIT CARD VALIDATOR ***

                ''')
    while True:
        check_card()
        option = input('Enter 1 to re-run code or any other key to exit >> ')
        try:
            if int(option) != 1:
                print('Program has ended')
                break
            else:
                print(' ')
        except ValueError:
            print('Program has ended')
            break

main()
