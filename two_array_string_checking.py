def string():
    word = ['ab','c']
    word2 = ['ac','b']
    string1 = ''
    string2 = ''
    for i in word:
        string1 += str(i)

    for j in word2:
        string2 += str(j)
    return (string1 == string2)
am = string()
print(am)
