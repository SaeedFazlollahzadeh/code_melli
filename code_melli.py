national = '2080570889'
last_digit = int(national[-1])
print(189 % 11)
result = ''
text = ''
text_sum = 0
for i in range(len(national)-1):
    text = text + f'({national[i]}*{-i + len(national)}) + '
    # result = sum(i * int(c) for i, c in enumerate(national[-2::-1], 2))
    text_sum = text_sum + (int(national[i]) * (-i + len(national)))
text = text[:len(text)-3]
modulus = text_sum % 11

if modulus + last_digit == 11 and modulus >= 2:
    print(f'Entered Code Meli {national} is correct')
elif modulus <= 2 and 11 - modulus:
    print(f'Entered Code Meli {national} is correct')
else:
    print('Error')

print(f'all the calculation: {text}')
print(f'final result: {text_sum}')
print(f'the result of "result % 11" is {modulus}')
