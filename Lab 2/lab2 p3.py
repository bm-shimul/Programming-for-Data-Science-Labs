text = input ("Enter  a word or Sentence: ")

charecter = 0
vowels = 0
spaces = 0

for charecter in text :
    charecter = charecter+1

    if charecter.lower() in "aeiou":
        vowels = vowels + 1 

        if charecter == "":
            spaces = spaces +1 

    
print ("Total Charecter :", charecter)
print ("Total vowels :", vowels)
print ("Total spaces :", spaces )