#using built in python sorting
def isAnagram1(word1, word2):
    return sorted(list(word1))== sorted(list(word2))

#manual
def isAnagram2(word1, word2):
    counter = {}
    word1 = list(word1)
    word2 = list(word2)

    if word1 and word2:
        
        for word in word1:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
                
        for word in word2:
            if word in counter:
                counter[word] -= 1
    else:
        raise Exception('One or more words are empty')

    for i in counter.values():
        if  i != 0:
            return False
    
    return True


word1 = "cinema"
word2 = "iceman"

print isAnagram1(word1, word2)
print isAnagram2(word1, word2)
