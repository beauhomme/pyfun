import re


def palindrome(word):
    # word = ''.join(re.findall(r'[a-z]+', word.lower()))
    wordlist = []
    for i in word:
        wordlist.append(i)

    print(wordlist)
    revlist= wordlist[::-1]
    print(revlist)

    revword = ''.join(revlist)

    if word == revword:
        print(word + ' is a Palindrome')
    else:
        print(word + ' is NOT a Palindrome')

    print(revword)

# palindrome('klingon')
# print(revlist[0:])# print(revrev)
# print(len(revlist))
# print(revlist)
# print(wordlist

word = 'maDAM'
# 
word = ''.join(re.findall(r'[a-z]+', word.lower()))
wex = word[::-1]
print(word)
print(wex)
print(word==wex)