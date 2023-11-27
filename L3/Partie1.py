#Soit l’alphabet T={a, b, c}, écrire un programme paramétré qui permet de :
#1) Générer le mot miroir d’un mot quelconque de T*.
# Ce mot sera donné en entrée à votre programme.
#2) Générer la puissance n d’un mot quelconque de T*. T^n
# Le mot et la valeur de n seront donnés en entrée à votre programme.

verification = True
empty_word = False
word = input("Donnez le mot: ")
if (word ==""):
    empty_word = True
length = int(len(word))
i = 0
while (i < length) and (verification):
    if word[i] == 'a' or word[i] == 'b' or word[i] == 'c':
        verification = True
    else:
        verification = False
    i += 1

if (verification or empty_word or word =="ɛ"):
    if (empty_word):
        print("Le mot vide appartient")
    else:    
        print("Le mot ", word," appartient")
else :
    print("Le mot ", word, " n'appartient pas à l'alphabet T")

i = length-1
wordMirror =  wordPower = ""
while i >= 0 :
    wordMirror = wordMirror + word[i]
    i -= 1


if (verification):
    n = input("Donnez la puissance: ")
    n = int(n)

    s = 0
    while s < n:
        wordPower = wordPower + word
        s += 1
    if (word ==""):
        print("Le word miroir du word vide est : ɛ")
    else:    
        print("Le word miroir de ", word, "est : ",wordMirror)

    if (empty_word):
        print("Le word puissance du word vide est: ɛ")
    else:
        print("Le word puissance de ", word," est: ",wordPower)