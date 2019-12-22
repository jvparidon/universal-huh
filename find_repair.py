import os

def find_repair(lang):
    with open(f'../data/OpenSubtitles/raw/{lang}/{lang}.txt', 'r') as subsfile, open(f'{lang}_huh.txt', 'w') as huhfile:
    #with open('test.txt', 'r') as subsfile, open('test_huh.txt', 'w') as huhfile:
        line1back = ''
        line2back = ''
        for line in subsfile:
            if line.strip('\n').strip('\t').strip(' ') != '':
                if line == line2back:
                    print(line2back.replace('\n', '') + '\t' + line1back.replace('\n', '') + '\t' + line.replace('\n', ''))
                    #huhfile.write(line1back.replace('\n', '') + '\t' + line)
                    huhfile.write(line1back)
                line2back = line1back
                line1back = line

find_repair('en')
