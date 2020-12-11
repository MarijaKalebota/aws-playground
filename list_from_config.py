import os
import configparser

parser_numbers = configparser.ConfigParser()
parser_numbers.read('./numbers.cfg')

for number in parser_numbers.sections():
    print(os.environ.get("{}_PASSWORD".format(number.upper())))