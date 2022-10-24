import random
wordlist=open("words.txt").readlines()
word=random.choice(wordlist)
wordle=len(word)
wordle-=1
word_comp=("_" *wordle)
def lts():
    return (word_in_list.join(word_comp))

guessed_letters=[]
guessed_words=[]
tries=len(word)
word_in_list = list(word_comp)
word_actual=list(word)
x=1
y=1

while tries!=0:
    if "_" not in word_in_list:
        print("")
        tries=0
        print("nyertel a szo:",word,"volt")
    else:
        print("")
        print (*word_in_list)
        print (tries,"probalkozasod van hatra")
        guess=input("mi a tipped? ")
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("ezt mar tippelted")
            elif guess not in word:
                print("helytelen tipp")
                tries-=1
                guessed_letters.append(guess)
            else:
                print ("helyes tipp")
                guessed_letters.append(guess)
                while guess in word_actual:
                    x=word_actual.index(guess)
                    word_in_list[x]=guess
                    word_actual[x]="/"


        else:
            print("ervenytelen tipp")

print("a jateknak vege a szo",word,"volt")
