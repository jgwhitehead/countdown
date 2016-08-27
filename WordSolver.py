
def validate_word(word, letters):
    letters_copy = letters[:]
    for c in word:
        if not c in letters_copy:
            return False
        letters_copy.remove(c)
    return True


def get_user_input():
    letters = []
    while True:
        inputted = input('enter 8 or 9 letters:')
        print("{s} letters entered".format(s=len(inputted)))
        if len(inputted) == 8 or len(inputted) == 9:
            letters = []
            letters.extend(inputted)
            break
    return letters


matches = []
file = '/usr/share/dict/words'
letters = get_user_input()
for word in open(file):
    word = word.lower().strip()
    if validate_word(word, letters):
        matches.append(word)
print("{s} matches".format(s=len(matches)))
matches.sort(key=len)
for match in matches:
    print(match)
print("longest word length: {longestLength}".format(longestLength=len(matches[-1])))
