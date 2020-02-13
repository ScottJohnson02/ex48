from ex48 import convert


def scan(input):
    lexicon = {'direction': ['north', 'south', 'east',
                             'west', 'down', 'up', 'left', 'right', 'back'],
               'verb': ['go', 'stop', 'kill', 'eat'],
               'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
               'noun': ['door', 'bear', 'princess', 'cabinet'],
               'number': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               'swear': ['ass', 'fuck', 'shit', 'fucking']}
    translate = ()
    commands = []
    sentence = input.split()
    for word in sentence:
        original = word
        test = 0
        number = False
        # checks if the word can be converted to a int
        if convert.convert_number(word) != word:
            translate = ('number', int(word))
            commands.append(translate)
            number = True  # the input is a number
        else:
            word = word.lower()

        for type in lexicon:
            # checks every type of word in the lexicon
            x = lexicon.get(type)

            if word in x:
                # checks if word was found in that word type
                translate = (type, original)
                commands.append(translate)
            else:
                test += 1  # checks what loop the test is on
            if test == 6 and number == False:
                translate = ('error', original)
                commands.append(translate)  # adds the translation to the list
    return commands


# data = alphabet.split() #split string into a list
#
# for temp in data:
#     print temp
