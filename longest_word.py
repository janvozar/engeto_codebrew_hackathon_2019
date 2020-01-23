words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']
longest = ()

def longest_word(words):
    longest = words[0]
    for i in range (0, len(words)-1):
        if len(longest)<len(words[i]):
            longest = words[i]
            print(longest)
    print('(' +longest + ', ' + str(len(longest)) + ')')
longest_word(words)