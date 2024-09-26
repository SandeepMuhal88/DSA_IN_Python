# Q5. how to update word in string ?

def checkString(str,word,update):
    l1=str.split()
    if word in l1:
        index=l1.index(word)
        l1[index]=update
        print(str(l1))
        l1 = " ".join(l1)
    else:
        print("Word not found")

str="My name sandeep"
word="My"
update="I"
checkString(str,word,update)