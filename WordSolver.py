import copy


def validate_word(word, letters):
    letters_copy = letters[:]
    # word = 'sulk'

    # print(word)
    for c in word:
        if not c in letters_copy:
            # print(c)
            return False
        letters_copy.remove(c)
    # print(word)
    return True


file = '/usr/share/dict/words'
while True:
    inputted = input('enter 8 letters:')
    print("{s} letters entered".format(s=len(inputted)))
    if len(inputted) == 8:
        letters = []
        letters.extend(inputted)
        break

matches = []

for word in open(file):
    word = word.lower().strip()
    # print(word)
    if validate_word(word, letters):
        # print(word)
        matches.append(word)
print("{s} matches".format(s=len(matches)))
matches.sort(key=len)
for match in matches:
    print(match)
