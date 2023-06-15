import random

def modify_word(word):
    if len(word) > 3:
        new_word = word[1:] + word[0] + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
    else:
        new_word = word[::-1]  
    
    return new_word

st=input("enter msg which u want to decode\n ")
words=st.split(" ")


for word in words:
    modified_word = modify_word(word)
    print(f"{word} -> {modified_word}")
