import sys

def text_to_braille(text):
    braille_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
        'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
        '0': '.OOO..', '.': 'O.O.OO', ',': 'O.....', ';': 'O.O...', ':': 'OO....',
        '?': 'OO.O..', '!': 'O..O..', '(': 'OOO...', ')': 'OOOO..', '-': 'O.OO..', 
        '/': '.OO...', '<': '.OO..O', '>': 'O..OO.', 'capital-follows': '.....O', 
        'number-follows': '.O.OOO', 'decimal-follows': '.O...O', 'space': '......'
    }
    first_number=True
    braille_eq = ''
    for char in text:
        if char.isupper():
            braille_eq += braille_dict['capital-follows']
            braille_eq += braille_dict[char.lower()]
        elif char.isdigit():
            if(first_number):
                braille_eq += braille_dict['number-follows']#just for the first number
            braille_eq += braille_dict[char]
            first_number=False
        elif char == ' ':
            braille_eq += braille_dict['space']
            first_number=True
        else:
            braille_eq += braille_dict[char]
    
    return braille_eq

def braille_to_text(braille):
    braille_dict ={
    'O.....': ['a', '1'], 'O.O...': ['b', '2'], 'OO....': ['c', '3'], 'OO.O..': ['d', '4'], 
    'O..O..': ['e', '5'], 'OOO...': ['f', '6'], 'OOOO..': ['g', '7'], 'O.OO..': ['h', '8'], 
    '.OO...': ['i', '9'], '.OOO..': ['j', '0'], 'O...O.': ['k'], 'O.O.O.': ['l'], 
    'OO..O.': ['m'], 'OO.OO.': ['n'], 'O..OO.': ['o'], 'OOO.O.': ['p'], 
    'OOOOO.': ['q'], 'O.OOO.': ['r'], '.OO.O.': ['s'], '.OOOO.': ['t'], 
    'O...OO': ['u'], 'O.O.OO': ['v'], '.OOO.O': ['w'], 'OO..OO': ['x'], 
    'OO.OOO': ['y'], 'O..OOO': ['z'], '.....O': 'capital-follows', '.O.OOO': 'number-follows'
    , '......': 'space'}   
    default=0 
    text = ''
    i = 0
    while i < len(braille):
        char = braille[i:i+6]
        if(braille_dict[char]=='capital-follows'):#Capital follows
            i+=6
            text+=braille_dict[braille[i:i+6]][default].upper()#add the letter in upper case
        elif(braille_dict[char]=='number-follows'):#Number follows
            i+=6
            default=1
            text+=braille_dict[braille[i:i+6]][default]#add the letter 
        elif(braille_dict[char]=='space'):#space
            default=0
            text+=' '
        else: #NO indicator before it
            text+=braille_dict[char][default]# lowercase character
        i += 6
    return text

def detect_and_translate(input_text):
    if all(char in 'O.' for char in input_text)and len(input_text.replace(' ', '')) % 6 == 0:
        return braille_to_text(input_text)
    else:
        return text_to_braille(input_text)

if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])
    print(detect_and_translate(input_text))
# OOO......O.OOOO.O....O.OOOOO..........OO..OO.....OOO.OOOO..OOO
# OOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
#My output
#.....OO.....O.O...OO...........O.OOOO......O.OOOO.O....O.OOOOO..........OO..OO.....OOO.OOOO..OOO
#Capita|a    |b   |c    |sp    |nm   |1    |                    
# expected
#.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
#Capita|  a |b    |c    |space|  nu |1     |2    |3    |space|