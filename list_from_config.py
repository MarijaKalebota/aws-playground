from dotenv import load_dotenv
load_dotenv()

import os
import configparser

parser_numbers = configparser.ConfigParser()
parser_numbers.read('./numbers.cfg')

for number in parser_numbers.sections():
    print(os.environ.get("{}_NAME".format(number.upper())))