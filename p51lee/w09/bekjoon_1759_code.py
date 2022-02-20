import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alphabets = sys.stdin.readline().split()
vowels = []
consonants = []

for alphabet in alphabets:
    if alphabet in ["a", "e", "i", "o", "u"]:
        vowels.append(alphabet)
    else:
        consonants.append(alphabet)
num_vowels = len(vowels)
num_consonant = len(consonants)
num_alphabet = len(alphabets)

answers = []
for vowel_selected in range(1, min(l-1, num_vowels+1)):
    vowel_selections = list(combinations(vowels, vowel_selected))
    consonant_selections = list(combinations(consonants, l-vowel_selected))
    for v_selection in vowel_selections:
        for c_selection in consonant_selections:
            temp = list(v_selection) + list(c_selection)
            temp.sort()
            answers.append("".join(temp))
answers.sort()
for ans in answers:
    print(ans)

