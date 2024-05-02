# Username Validation exercise
while True:
    user_name = input('Username: ')
    if len(user_name) <= 12:
        if user_name.count(' ') == 0:
            if user_name.isalpha() == True:
                print('''
                        Success! Username is valid.

                        ''')
                break
            else:
                print('''
                        Username should not contain digits

                        ''')
        else:
            print('''
                  Username should not contain spaces

                  ''')
    else:
        print('''
                Username should have a maximum of 12 characters

                ''')
