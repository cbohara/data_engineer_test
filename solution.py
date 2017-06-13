#!/usr/bin/env python3

import sys
import codecs


def main():
    """Fix utf-16 broken tsv file so each row contains the same number of fields and output as utf-8."""
    with codecs.open('data.tsv', 'rU', encoding='utf_16_le') as input_utf_16_file:
        with open('utf8.tsv', 'w', encoding='utf_8') as output_utf_8_file:
            for line in input_utf_16_file:
                try:
                    output_utf_8_file.write(line.encode('utf_16_le').decode('utf-8'))
                except UnicodeDecodeError:
                    output_utf_8_file.write(line.encode('utf_16_le').decode('latin-1'))


    with open('utf8.tsv', 'r', encoding='utf_8') as input_broken_file:
        with open('fixed.tsv', 'w', encoding='utf_8') as output_fixed_file:
            data = input_broken_file.readlines()
            five_tabs = [row for row in data if len(row.split('\t')) == 5]
            for row in five_tabs:
                output_fixed_file.write(row)


if __name__ == '__main__':
    sys.exit(main())
