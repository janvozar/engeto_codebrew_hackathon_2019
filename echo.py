#example_sentece = ('I do not want to work today')
repeat = int(input('Please enter the number of repetitions: '))
core = input('Please enter your sentence: ')
dare = core.split()
echo = []
space_between_words = ' '

def echolocation(repet, dare, echo):
    for i in dare:
        string_creation = (i + ' ') * repeat
        echo.append(string_creation)
        repeated_words = space_between_words.join(echo)
    print (repeated_words)

echolocation(repeat, dare, echo)