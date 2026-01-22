import sys
import json
import time

LETTERS = {
  "a": 13,
  "b": 12,
  "c": 11,
  "d": 10,
  "e": 9,
  "f": 8,
  "g": 7,
  "h": 6,
  "i": 5,
  "j": 4,
  "k": 3,
  "l": 2,
  "m": 1,
  "n": 0,
  "o": -1,
  "p": -2,
  "q": -3,
  "r": -4,
  "s": -5,
  "t": -6,
  "u": -7,
  "v": -8,
  "w": -9,
  "x": -10,
  "y": -11,
  "z": -12
}

WORDFILE = "words_dictionary.json"
CACHEFILE = "cache.json"
CACHE = {}

def rebuild_cache():
    # rebuild cache
    global CACHE
    for word in data:
        CACHE[word] = calculate_string(word)
    print("Rebuilt Cache!")
    with open(CACHEFILE, 'w') as f:
        f.write(json.dumps(CACHE, indent=4))

def calculate_string(string):
    # calculate string
    total = 0
    if string in CACHE:
        return CACHE[string]
    for char in string:
        if char not in LETTERS:
            continue
        total += LETTERS[char]
    #print("Calculated!")
    return total

def get_possibilities():
    # get possibilities
    time.sleep(1)
    print("Gotten!")

print("Word Adder")
print("==========")
print("Starting...")
time.sleep(1)
print("Loading file...")

try:
    with open(WORDFILE, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f'Error: The file {WORDFILE} was not found.')
    sys.exit(1)
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file. Check for invalid JSON content.")
    sys.exit(1)

try:
    with open(CACHEFILE, 'r') as file:
        CACHE = json.load(file)
except FileNotFoundError:
    print(f'Error: The file {CACHEFILE} was not found.')
    sys.exit(1)
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file. Check for invalid JSON content.")
    sys.exit(1)

print("Files loaded")
print()
print("----------")
print("Options:")
print("1: Rebuild Cache")
print("2: Calculate String")
print("3: Get Possibilities")
try:
    option = int(input("Pick one: "))
except ValueError:
    print("Error: Not a number.")
    sys.exit(1)

if option == 1:
    rebuild_cache()
elif option == 2:
    word = input("Enter string: ")
    print(calculate_string(word))
elif option == 3:
    get_possibilities()
else:
    print("Error: Not an option.")
    sys.exit(1)