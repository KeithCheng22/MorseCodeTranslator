morse_code = {'a': '.-',
              'b': '-...',
              'c': '-.-.',
              'd': '-.. ',
              'e': '.',
              'f': '..-. ',
              'g': '--.',
              'h': '....',
              'i': '..',
              'j': '.--- ',
              'k': '-.-',
              'l': '.-..',
              'm': '--',
              'n': '-.',
              'o': '---',
              'p': '.--.',
              'q': "--.-",
              'r': '.-.',
              's': '...',
              't': '-',
              'u': '..-',
              'v': ' ...-',
              'w': '.--',
              'x': '-..-',
              'y': '-.--',
              'z': '--..',
              ' ': ' ',
              '0': '-----',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.',
              ',':',',
              "'":"'",
              '.':'.',
              '!':'!'}


class Converter:
    def encode(self, user_input):
        list_vers = list(user_input)
        encoder = [morse_code[char] for char in list_vers]
        morse_word = ' '.join(encoder)
        return morse_word

    def decode(self, user_input):
        key_list = list(morse_code.keys())
        val_list = list(morse_code.values())
        sliced = user_input.split(' ')
        for _ in sliced:
            if '' in sliced:
                sliced[sliced.index('')] = ' '
        decoder = [val_list.index(char) for char in sliced]
        decoded = [key_list[char] for char in decoder]
        actual_word = ' '.join(decoded)
        return actual_word


