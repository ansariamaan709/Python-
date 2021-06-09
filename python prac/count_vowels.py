word = input('')
num_vowels=0
vowels='aeiou'
for letter in word:

    if letter in vowels:
        num_vowels += 1
print(num_vowels)
