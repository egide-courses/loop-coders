text = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"
p = 0
q = 0

for letter in text:
    if letter.isalpha():
        if letter in vowels:
            p = p + 1
        else:
            q = q + 1

print("Vowels:", p)
print("Consonants:", q)
