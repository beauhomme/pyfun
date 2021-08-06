input = 'fish apple BANANA Mango pear avacado pepper'


def sort_words(input):

    words = input.split(' ')

    def lowconv(e):
        return e.lower()

    words.sort(key=lowconv)

    print(words)

sort_words(input)