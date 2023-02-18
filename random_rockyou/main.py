# This program takes an input file from the user and randomly selects a line from the file to print to the screen.
# File source: https://www.w3resource.com/python-exercises/file/python-io-exercise-15.php https://stackoverflow.com/questions/10114146/string-processing-error-unicodedecodeerror-utf8-codec-cant-decode
import random


def random_line(fname):
    lines = open(fname, encoding='latin-1').read().splitlines()
    return random.choice(lines)


print(random_line('rockyou.txt'))
