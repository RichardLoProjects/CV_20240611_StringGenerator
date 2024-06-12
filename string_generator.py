from random import Random

def generate_password(
    length:int,
    incl_mixedcase:bool=True,
    incl_numbers:bool=True,
    incl_symbols:bool=True
) -> str:
    '''Generate a password with the given length and character type inclusions.'''
    min_length:int = 1 + incl_numbers + incl_mixedcase + incl_symbols
    if length < min_length:
        raise ValueError(f'Password length should be at least {min_length} characters to include all character types.')
    lower:str = 'abcdefghijklmnopqrstuvwxyz'
    upper:str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if incl_mixedcase else ''
    numbers:str = '0123456789' if incl_numbers else ''
    symbols:str = '`!"$%^&*()-_=+[]{}#~;:\'@,.<>/?\\|' if incl_symbols else ''
    ## Symbols not included: £ and ¬
    rand:Random = Random()
    password:list = [rand.choice(lower)]
    password += rand.choice(upper) if incl_mixedcase else ''
    password += rand.choice(numbers) if incl_numbers else ''
    password += rand.choice(symbols) if incl_symbols else ''
    if length > min_length:
        all_characters:str = lower + upper + numbers + symbols
        password += rand.choices(all_characters, k=length-min_length)
    rand.shuffle(password)
    return ''.join(password)



def user_interaction() -> None:
    length:int = 20
    mixedcase:int = 1
    numbers:int = 1
    symbols:int = 1
    print('Program will continue generating passwords until a non-integer is entered.\n')
    while True:
        length = input('Enter length: ')
        mixedcase = input('Include uppercase? (0/1): ')
        numbers = input('Include numbers? (0/1): ')
        symbols = input('Include symbols? (0/1): ')
        try:
            length = int(length)
            mixedcase = int(mixedcase)
            numbers = int(numbers)
            symbols = int(symbols)
            print(generate_password(length, mixedcase, numbers, symbols),'\n')
        except:
            break

def test(print_message:bool) -> None:
    password_length = 20
    for i in range(8):
        binary = bin(i)[2:]
        while len(binary) < 3:
            binary = '0' + binary
        incl_c, incl_n, incl_s = binary
        incl_c, incl_n, incl_s = int(incl_c), int(incl_n), int(incl_s)
        password = generate_password(password_length, incl_c, incl_n, incl_s)
        output_message = f'{password} has ' if incl_c or incl_n or incl_s else f'{password} is weak. '
        output_message += 'mixedcase, ' if incl_c else ''
        output_message += 'numbers, ' if incl_n else ''
        output_message += 'symbols, ' if incl_s else ''
        if print_message:
            print(output_message[:-2]+'.')
    if print_message:
        print('Test ran without crashing Python!')
    '''
    Notes when debugging:
    Learned £ and ¬ are not ascii characters
    Learned True + True = 2
    Learned list + string is valid: [] + 'abc' --> ['a','b','c']
    Random.choice(seq) is invalid: must instantiate an instance of the object first
    random_inst.choice('') is invalid: cannot randomise choice on empty seq
    '''

def main() -> None:
    test(False)
    user_interaction()

if __name__ == '__main__':
    main()
