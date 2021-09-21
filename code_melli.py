attempts = 0
while True:
    national = input('Enter Your Code Melli: ')
    if len(national) == 10:
        pass
        break
    elif len(national) >= 10 or len(national) <= 10:
        attempts += 1
        print(f'Your talash so far was {attempts} times. Entered Code Melli is not equal to digits, try again...')
        if attempts >= 3:
            print(f'Please jam your havas dige, you have tried {attempts} times tahala, base:)')
            if attempts == 10:
                print(f'Base dige, there\'s no need to try more:)')
                break

if len(national) == 10:
    last_digit = int(national[-1])
    result = ''
    text = ''
    text_sum = 0
    for i in range(len(national)-1):
        text = text + f'({national[i]}*{-i + len(national)}) + '
        result = sum(i * int(c) for i, c in enumerate(national[-2::-1], 2))
        text_sum = text_sum + (int(national[i]) * (-i + len(national)))
    text = text[:len(text)-3]
    modulus = text_sum % 11

    def final_result():
        if modulus + last_digit == 11 and modulus >= 2:
            return f'Entered Code Melli {national} is correct. Hooray:)\n'
        elif 2 >= modulus == last_digit:
            return f'Entered Code Melli {national} is correct. Hooray:)\n'
        else:
            return f'Error, Code Melli {national} is not correct.\n'

    final_result = final_result()
    output = open('data.txt', 'a')
    output.write(f'''First, we calculate: {text}.
The sum is: {text_sum}.
Then we calculate the remainder of the division "text_sum % 11" is {modulus}.
Now we\'ll check if Code Melli is correct in the next line:
{final_result}\n\n''')

print('The End of the Script')
