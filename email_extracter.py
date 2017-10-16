#!/usr/bin/env python
# coding:utf-8

import re
import sys

if len(sys.argv) < 3:
    print('Usage: python email_extracter.py [input_file] [output_file]')
    sys.exit()

regex = re.compile(r'[\w\.-]+@[\w\.-]+')

# The input file
filename = sys.argv[1]

# The output file.
output_file = sys.argv[2]

with open(filename, 'r') as emailfile:
    email_list = emailfile.read().lower()

# Here re.findall() returns a list of all the found email strings
emails = re.findall(regex, email_list)

# Write the emails into the file, one per line
with open(output_file, 'w') as output_file:
    for email in emails:
        output_file.write(email + '\n')
