#!/usr/bin/python3
"""
   5-text_indentation module

   provides one function text_indentation

   sample:
>>> text_indentation("Lorem ipsum dolor sit consectetur. adipiscing elit")
Lorem ipsum dolor sit consectetur adipiscing elit.
<BLANKLINE>
adipiscing elit
"""


def text_indentation(text):
    """
       prints a text with 2 new lines after
       each of these characters: ., ? and :

      Args:
          text(str): the string to print
    """

    if type(text) is not str:
        raise TypeError('text must be a string')
    string = ''
    i = 0
    while i < len(text):
        if text[i] in ['.', ':', '?']:
            print(text[i], end='')
            if text[i + 1] == ' ':
                i += 2
            print("\n" * 2, end='')
        print(text[i], end='')
        i += 1


if __name__ == '__main__':

    text_indentation("""Lorem ipsum dolor hud""")
