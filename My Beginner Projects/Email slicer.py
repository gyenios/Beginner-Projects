# email slicer exercise
email = input('E-mail: ')
n = email.index('@')
username = email[:n]
domain = email[n+1:]
print(username,domain, sep = '    ')

