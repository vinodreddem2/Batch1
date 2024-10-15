
def removeSpecialChar(arr,str):
    # loop through the string and search each char with the values in the list and then replace it.
    for char in str:
        if char in arr:
            str = str.replace(char,"")
    return str


# Driver Code
special_char_arr = ["(",")","[","]",",","."," ","{","}"]

str = " Ma(hes)h} you{are]great,and[knowledgable ."

plain_string = removeSpecialChar(special_char_arr,str)

print(plain_string)

