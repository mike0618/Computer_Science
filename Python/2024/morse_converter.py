morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    " ": "/",
}


# Create a reverse lookup dictionary for Morse code
reverse_morse = {v: k for k, v in morse.items()}

def encode(text: str) -> str:
    # Initialize an empty string to store the Morse code
    code = ''
    # Loop through each character in the cleaned input text
    for symbol in text.strip():
        # Convert the character to uppercase and find the corresponding Morse code
        morse_sym = morse.get(symbol.upper(), '?')
        # Append the Morse code to the result string with a space separator
        code += morse_sym + ' '
    # Return the final Morse code string, removing any trailing spaces
    return code.strip()

def decode(code: str) -> str:
    # Initialize an empty string to store the decoded text
    text = ''
    # Split the input Morse code into a list of Morse code elements
    code_lst = code.strip().split()
    # Loop through each Morse code element
    for element in code_lst:
        # Use match-case to handle different Morse code elements
        match element:
            # If the element is '/', add a space (indicating word separation)
            case '/':
                text += ' '
            # If the element is '.-.-', add a newline character
            case '.-.-':
                text += '\n'
            # If the element is '?', add a '?' to indicate an unknown character
            case '?':
                text += '?'
            # For all other elements
            case _:
                # Use the reverse lookup dictionary to find the symbol
                text += reverse_morse.get(element, '?')
    # Return the final decoded text, removing any trailing spaces
    return text.strip()

def convert():
    # Print the welcome message
    greet = 'Welcome to the Morse Code Auto-Converter!'
    print(greet)
    # Print the encoded version of the welcome message for demonstration
    print(encode(greet))

    while True:
        # Prompt user for input or exit
        user_input = input('\nEnter your text or Morse code here, or press Enter to exit,\nif you want to enforce converting text to Morse code start your input with *:\n').strip()
        # Exit the loop if the input is empty
        if not user_input:
            break

        # Check if the input starts with '*', or if it has more non-Morse characters
        if user_input.startswith('*') or user_input.count('-') + user_input.count('.') + user_input.count('/') < len(user_input) // 2:
            # Encode the text if it starts with '*' or has more non-Morse characters
            print('\nEncoding Text to Morse Code')
            print('\n### MORSE CODE ###')
            # Remove the '*' and encode the rest
            print(encode(user_input.lstrip('*')))
            print('### END OF THE CODE ###')
        else:
            # Decode the Morse code if it does not match the encoding condition
            print('\nDecoding Morse Code')
            print('\n### YOUR TEXT ###')
            print(decode(user_input))  # Decode the Morse code to text
            print('### END OF THE TEXT ###')

# Execute the convert function if this script is run directly
if __name__ == '__main__':
    convert()
