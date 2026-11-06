#JOHN BRIAN DELA CRUZ
#BAET 2102
#VOWEL COUNTER

sentence = input("Sentence: ")

vowels = 0

for character in sentence:
    if character.lower() in "aeiou":
        vowels = vowels + 1

print("Vowels:", vowels)