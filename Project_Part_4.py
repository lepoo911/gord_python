class Entry:
    def __init__(self, input_word, input_synonyms):
        self.word = input_word
        self.synonyms = input_synonyms


e1 = Entry("dog", ["doggie", "puppy"])
e2 = Entry("cat", ["kitty"])
e2 = Entry("happy", ["gleeful"])
Thesaurus = [e1, e2]

doc1 = ['this', 'is', 'a', 'happy', 'document']
doc2 = ['this', 'gleeful', 'another', 'gleeful']
Corpus = [doc1, doc2]


def search(keyword):
    retVal = []
    allwords = [keyword]
    for entry in Thesaurus:
        if keyword == entry.word:
            for syn in entry.synonyms:
                allwords.append(syn)

    for search_word in allwords:
        count = 0
        for doc in Corpus:
            for word in doc:
                if search_word == word:
                    count = count + 1
        retVal.append((search_word, count))

    return retVal


input = 'happy'
output = search(input)  # invoke the method using a test input
print(output)  # prints the output of the function
# do not remove this line!
