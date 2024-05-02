# Format specifiers  = {value:flags}
''' used to format a value based on the flags inserted'''

#:.(number)f = round to that many decimal places (fixed point)
#:(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use plus sign to indicate positive value
# := = place sign to the leftmost position
# :  = insert a space before positive numbers
# :, = comma separator (for separating numbers into thousands)

price = 5508.891
charge = -1002.765

print(f'''
# 2 decimal places
${price:.2f}
***************

# 10 spaces for output
${price:10}
***************

# 10 spaces for output left aligned
${price:<10}
***************

# 10 spaces for output right aligned
${price:>10}
***************

# 10 spaces for output center aligned
${price:^10}
***************

# Using the + sign to indicate positive values
${price:+}
${charge:+} #negative so no effect
***************

# Using space to indicate positive numbers
${price: }
${charge: } #negative so no effect
***************

# Placing sign to the leftmost position
${price:=}
***************

# Comma separator
${price:,}
${charge:,}
***************

# Combination of some format specifiers
${price:+,.2f}
''')      
      
