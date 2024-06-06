### chap16/emdash-fixed.py
import sys

# Terminal colors
C_RESET = '\033[0m'
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
"""INSTRUCTIONS:
Let's look at each sentence in this paragraph, and
you tell me if you want me to surround a phrase with
em dashes rather that the existing commas.""")

    # Iterate through each candidate sentence in text.
    # A sentence is a candidate only if it has three
    # or more phrases in it.
    sentences = paragraph.split('.')
    sentences = sentences[:-1]  # last item isn't a sentence
    for i, s in enumerate(sentences):
        # Split the sentence into numbered phrases
        phrases = s.split(',')
        if len(phrases) == 1 or len(phrases) == 2:
            # Nothing to do
            continue

        print()

        # Print the phrases and ask the user
        for j, p in enumerate(phrases):
            if j != 0 and j != len(phrases) - 1:
                print(f'{C_BLUE}{j+1}: {p}{C_RESET}')
            else:
                print(f'{j+1}: {p}')
        
        ans = int(input(f'\nWhich {C_BLUE}blue{C_RESET} phrase, \
if any, do you want to set off with em dashes? '))
        if ans == 0:
            continue     # Leave the sentence alone
        elif ans == 1 or ans == len(phrases):
            print("That phrase wasn't blue...skipping on.")
            continue
        else:
            a = ans - 1  # Turn ans into an index

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
        # the leading spaces in it and the new_suffix.
        new_s = s_prefix + '--' + phrases[a].strip() + '--' + s_suffix.strip()

        # Put the updated sentence back into the sentences list
        sentences[i] = new_s

    # Add back the periods and print out the new paragraph
    for i in range(len(sentences)):
        sentences[i] += '.'
    print('\nNew paragraph:')
    print(''.join(sentences))

if __name__ == '__main__':
    main()
