s1 = input()
v = "aeiou"
vowel = 0
consonant = 0
for i in range(len(s1)):
    if s1[i] in v:
        vowel = vowel+1
    else:
        consonant = consonant+1 
print(consonant)
