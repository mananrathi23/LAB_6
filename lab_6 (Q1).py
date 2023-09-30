n = str(input("enter: "))
a = "aeiouAEIOU"
count_vowels = 0 
count_consonents = 0
count_words = 1
for i in n :
    if i in a :
        count_vowels+=1
    elif i != " "  :
        count_consonents+=1
    else:
        count_words+=1 
print("vowels: ", count_vowels)
print("consonents: ", count_consonents)
print("words: ", count_words)