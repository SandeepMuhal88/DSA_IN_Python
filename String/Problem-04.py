# Q4. write a program to Check word in string.


def CheckString(string, word):
    l1 = string.split()
    if word in l1:
        print(f"Found {word}")
    else:
        print(f"Not Found {word}")

string = "my name is Sandeep MUhal Current I prepare For I am firt job in google"
word = "years"
CheckString(string, word)
word="job"
CheckString(string, word)
word="google"
CheckString(string, word)