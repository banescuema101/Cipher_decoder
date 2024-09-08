import sys
# -------> Purposes and behavior:

# I write an Python script that will help you break the cipher and decode the original text. The script does the following:
#   -> read the ciphertext from a file specified as a command line argument
#   -> use a dictionary to map each encoded character back to it's original value
#   -> manually populate this dictionary as you progress in your attempt and reveal new characters
#   -> whenever you run the script, it prints the text to the screen, with a few minor changes:
#........ any character that exists as a key in the dictionary is replaced with the found correspondent.
#........ any replaced character is highlighted in bold red.


#   The only known information was the fact that " 5 SLEUZGU " represents a calendar date, so I had to find
# the month with the fourth letter as well as the seventh. From here I realized that it is NOVEMBER.
#   From here, everything was like a puzzle, gradually I found other connections
# (from the prepositions: the, and, on etc.)

# Function for display the text -> red if the letters have changed, black otherwise
# functie pentru prelucrarea textului pentru afisat, red daca literele s-au schimbat, altfel, negru

def colored_text(text, cipher_map):
  red_color = '\033[1;31m'
  termination = '\033[0m'
  colored_text = ""
  for char in text:
    # If the char has been replaced, will be highlighted in red (if i found it through the dictionary values)
    if char in cipher_map.values():
      colored_text += f"{red_color}{char}{termination}"
    else:
      colored_text += char
  return colored_text

# Function for decrypting each character of the text, using the dictionary.
def decode_text(text, cipher_map):
  decoded_text = ""
  for char in text:
    if char in cipher_map:
      decoded_text += cipher_map[char]  # In the new text i will replace the old char(the key) with the afferent values in the dictionary
    else:
      decoded_text += char
  return decoded_text

def main():
  if (len(sys.argv) < 2):  # display a message error if there are insuficient arguments
    print("Usage: python3 decode_cipher.py <cipher_file>")
    sys.exit()
  file_name = sys.argv[1]  # i take the parameter of the first position, the file-name
  try:
      file = open(file_name, 'r')
      cipher_text = file.read()
  except FileNotFoundError:
    print("The cipher_text file doesn't exist!")
    sys.exit()
  cipher_map = {
    'S': 'N', 
    'L': 'O',
    'E': 'V',
    'Z': 'M',
    'G': 'B',
    'U': 'E',
    'T': 'R',
    'O': 'T',
    'F': 'H',
    'K': 'F',  
    'I': 'A',
    'Q': 'P',
    'V': 'L',
    'P': 'I',
    'Z': 'M',      
    'W': 'C',
    'J': 'S',
    'B': 'D',
    'X': 'U',
    'Y': 'Y',
    'H': 'G',
    'R': 'W',
    'N': 'K',
    'M': 'J',
    'E': 'V'
  }
  decoded_text = decode_text(cipher_text, cipher_map)
  print(colored_text(decoded_text, cipher_map))
if __name__ == '__main__':
  main()  