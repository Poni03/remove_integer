import os
import re

def remove_numbers(text):
    return re.sub(r'[0-9-]', '', text)

def merge_files(output_file, input_files):
    with open(output_file, 'w') as f:
        for filename in input_files:
            #print(filename)
            with open(os.path.join('zak/', filename), 'r') as f_in:
                text = f_in.read()
                text = remove_numbers(text)
                f.write(text)

if __name__ == '__main__':
    input_files = os.listdir('zak')
    #print(input_files)
    output_file = 'output.txt'
    merge_files(output_file, input_files)
