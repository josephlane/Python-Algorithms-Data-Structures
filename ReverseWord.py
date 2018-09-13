
def rev_word(text):
    
    text = text.strip()
    res = []
    word = ""
    st = ""

    for i in range(len(text)):
        if len(text[i].strip()) > 0 or i == len(text):
            word += text[i]
        else:
            res.append(word)
            word = ""
    if word:
        res.append(word)

    while res:
        st += res.pop()
        if len(res) > 0:
            st += " "

    return st

print rev_word("Hello I Would Like To Go Home")

    
