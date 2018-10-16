# The Following Script aggregates the files located in /nlu into chatbot_nlu_def.md

import glob
import os

def create_nlu_file():
    # Name and location of the final file?
    output_filename = './backend/chatbot_nlu_def.md'

    with open(output_filename, 'w') as outfile:
        print("writing data to " + output_filename)
        write_md("intents", outfile)
        write_md("synonyms", outfile)
        write_md("regex", outfile)

def write_md(name, outfile):
    files = glob.glob('./backend/nlu/' + name + '/*.md')
    for fname in files:
        print("writing intent " + fname)
        with open(fname) as infile:
            outfile.write("\n\n");
            outfile.write(infile.read());

if __name__ == '__main__':
    create_nlu_file()
