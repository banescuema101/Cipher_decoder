import sys

#Function for display the text -> red if the letters have changed, black otherwise
def colored_text(text, cipher_map):
  red_color = '\033[1;31m'
  termination = '\033[0m'
  colored_text = ""
  for char in text:
    # If the char has been replaced, will be highlighted in red
    #  (if i found it through the dictionary values)
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
      decoded_text += cipher_map[char]  
      # In the new text i will replace the old char(the key)
      #  with the afferent values in the dictionary
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