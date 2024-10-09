### chap16/emdash.py
"""Limiting assumption: This script works with paragraphs
in which all sentences end with periods, and no period
characters are used for any other purpose."""
import sys

# Terminal colors
C_RESET = '\033[0m'
C_RED = '\033[31m'
C_BLUE = '\033[34m'

def main():
    # Check usage
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 emdash.py paragraph.txt')
    
    # Grab the paragraph and convert any newlines into spaces
    with open(sys.argv[1]) as fin:
        paragraph = fin.read()
    paragraph = paragraph.replace('\n',' ')

    # Print out instructions
    print( \
"""**INSTRUCTIONS**
As you look at each sentence in this paragraph, tell me
via a phrase index if you want to surround that phrase
with em dashes rather than the existing commas.""")

    # Iterate through each candidate sentence in text.
    # A sentence is a candidate only if it has three
    # or more phrases in it.
    sentences = paragraph.split('.')
    sentences = sentences[:-1]  # last item isn't a sentence
    for i, s in enumerate(sentences):
        # Split the sentence into phrases
        phrases = s.split(',')
        if len(phrases) == 1 or len(phrases) == 2:
            # Nothing to do
            continue

        print()   # blank line in output

        # Number and print the phrases
        for j, p in enumerate(phrases):
            if j != 0 and j != len(phrases) - 1:
                print(f'{C_BLUE}{j+1}: {p}{C_RESET}')
            else:
                print(f'{j+1}: {p}')
        
        # Grab a phrase index from the user, if any
        a = get_phrase_index(phrases)
        if a == 0:
            continue     # Leave the sentence alone

        # Add back the comma on the unaffected phrases while
        # building the sentence prefix and suffix.
        s_prefix = ''
        s_suffix = ''
        for j in range(0, a):
            if j != a - 1:
                s_prefix += phrases[j] + ','
            else:
                s_prefix += phrases[j]
        for j in range(a + 1, len(phrases)):
            if j != len(phrases) - 1:
                s_suffix += phrases[j] + ','
            else:
                s_suffix += phrases[j]

        # Add the em dashes to the affected phrase and remove
        # the leading spaces in it and the s_suffix.
        new_s = s_prefix + '--' + phrases[a].split() + '--' + s_suffix.split()

        # Put the edited sentence back into the sentences list
        sentences[i] = new_s

    # Add back the periods and print out the new paragraph
    for i in range(len(sentences)):
        sentences[i] += '.'
    print('\nNew paragraph:')
    print(''.join(sentences))

def get_phrase_index(phrases):
    prompt = f'\nWhich {C_BLUE}blue{C_RESET} phrase do you want to set off with em dashes? Enter 0 for none: '

    # Keep asking until we get a good answer. `0` says do nothing
    # to the sentence. Remember that the user sees a count, not an
    # index: `1` and `len(phrases)` are the first and last phrases. 
    while True:
        try:
            ans = int(input(prompt))
            if ans == 0:
                return ans     # Leave the sentence alone
            elif ans == 1 or ans == len(phrases):
                print("That phrase wasn't blue...skipping on.")
                return 0       # Leave the sentence alone
            elif ans < 1 or ans > len(phrases):
                print(f"{C_RED}Index out of bounds:{C_RESET} Please enter a blue number or 0.")
            else:
                phrase_index = ans - 1  # Turn ans into an index
                return phrase_index
        except ValueError:
            print(f"{C_RED}Not a number:{C_RESET} Please enter a blue number or 0.")

if __name__ == '__main__':
    main()
