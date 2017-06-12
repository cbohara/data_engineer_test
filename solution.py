import codecs

with codecs.open('data.tsv', 'rU', encoding='utf_16_le') as input_file:
    with open('fixed.tsv', 'w') as fixed_file:
        for line in input_file:
            try:
                fixed_file.write(line.encode('utf_16_le').decode('utf-8'))
            except UnicodeDecodeError:
                fixed_file.write(line.encode('utf_16_le').decode('latin-1'))
