import requests

# Link to the script
url = 'https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script'
# Use requests to download the script and convert it to test
r = requests.get(url, allow_redirects=True)
whole = r.content.decode('ascii')

# Split the string on the places that I want
SCRIPT1 = whole[:30005]
SCRIPT2 = whole[30005:]

# Add the flag for the middle of the script
FLAG = 'sp00ky{th4ts_4l0t_0f_subs}\n'

# Create the output string
output = ""

# Create the lookup table for the emojis
EMOJILOOKUP = {
    ' ': '🌌',
    'a': '🏭',
    'b': '🔥',
    'c': '👻',
    'd': '👽',
    'e': '🍉',
    'f': '🍎',
    'g': '✨',
    'h': '🎂',
    'i': '🏊',
    'j': '👍',
    'k': '👎',
    'l': '🌈',
    'm': '🍕',
    'n': '👌',
    'o': '👾',
    'p': '🤖',
    'q': '👺',
    'r': '👹',
    's': '👿',
    't': '🤡',
    'u': '🇪',
    'v': '👶',
    'w': '👦',
    'x': '👧',
    'y': '👨',
    'z': '👩',

    'A': '🇦',
    'B': '😱',
    'C': '🦃',
    'D': '📀',
    'E': '🧸',
    'F': '🍩',
    'G': '🍪',
    'H': '🍁',
    'I': '🇲',
    'J': '🥘',
    'K': '🛸',
    'L': '🇮',
    'M': '🇳',
    'N': '💾',
    'O': '🇸',
    'P': '🥞',
    'Q': '🥢',
    'R': '🥟',
    'S': '🎁',
    'T': '🏁',
    'U': '💳',
    'V': '🎄',
    'W': '🐕',
    'X': '☕',
    'Y': '🔑',
    
    "'": '🍖',
    ',': '👋',
    '.': '🛑',
    '\n': '🔞',
    '!' : '👀',
    '?': '💸',
    '-': '🌕',
    ':': '🌑',
    '"': '🌚',
    '{': '🌝',
    '}': '🌞',
    '_': '🌛',
    
    '0': '🥜',
    '1': '📹',
    '2': '📺',
    '3': '🍴',
    '4': '🧊',
    '5': '🍆',
    '6': '🌮',
    '7': '🍑',
    '8': '💻',
    '9': '📱',
}

# Loop through each character in each string and add the emoji to the output
for i in SCRIPT1:
    output = output + EMOJILOOKUP[i]
    
for i in FLAG:
    output = output + EMOJILOOKUP[i]
    
for i in SCRIPT2:
    output = output + EMOJILOOKUP[i]

# Print the output
print(output)
