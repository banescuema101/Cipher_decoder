## --> Purposes and behavior: <--

# I write an Python script that will help you break the cipher and decode the original text. The script does the following:
  -> read the ciphertext from a file specified as a command line argument
  
  -> use a dictionary to map each encoded character back to it's original value
  
  -> manually populate this dictionary as you progress in your attempt and reveal new characters
  
  -> whenever you run the script, it prints the text to the screen, with a few minor changes:
      any character that exists as a key in the dictionary is replaced with the found correspondent.
      any replaced character is highlighted in bold red.
# How everything starts?
  The only known information was the fact that " 5 SLEUZGU " represents a calendar date, so I had to find
  the month with the fourth letter as well as the seventh. From here I realized that it is NOVEMBER.
  From here, everything was like a puzzle, gradually I found other connections (from the prepositions: the, and, on etc.)
