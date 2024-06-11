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
    r:Random = Random()
    password:list = [r.choice(lower)]
    password += r.choice(upper) if incl_mixedcase else ''
    password += r.choice(numbers) if incl_numbers else ''
    password += r.choice(symbols) if incl_symbols else ''
    if length > min_length:
        all_characters:str = lower + upper + numbers + symbols
        password += r.choices(all_characters, k=length-min_length)
    r.shuffle(password)
    return ''.join(password)



def test() -> None:
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
        print(output_message[:-2]+'.')
    '''
    Notes when debugging:
    Learned £ and ¬ are not ascii characters
    Learned list + string is valid: [] + 'abc' --> ['a','b','c']
    Random.choice(seq) is invalid: must instantiate an instance of the object first
    random_inst.choice('') is invalid: cannot randomise choice on empty seq
    '''

def main() -> int:
    test()
    print('Test ran without crashing Python!')
    return 0

if __name__ == '__main__':
    main()
