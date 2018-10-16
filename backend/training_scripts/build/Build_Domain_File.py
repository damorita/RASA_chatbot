# The Following Script aggregates the files located in /domain into domain.yml

import glob
import os

def writeSubFile(outfile, subfileName, spacer):
    with open (subfileName) as infile:
        for line in infile.readlines():
            outfile.write(spacer + line)

def intents(outfile):
    outfile.write("\n\n")
    writeSubFile(outfile, "./backend/domain/intents.yml", "")

def entities(outfile):
    writeSubFile(outfile, "./backend/domain/entities.yml", "")

def slots(outfile):
    outfile.write("\n\n")
    writeSubFile(outfile, "./backend/domain/slots.yml", "")

def templates(outfile):
    outfile.write("\n\ntemplates:")
    utterance_files = glob.glob("./backend/domain/utterances/*.yml")
    for fname in utterance_files:
        outfile.write("\n")
        writeSubFile(outfile, fname, "  ")

def actions(outfile):
    outfile.write("\n\n")
    writeSubFile(outfile, "./backend/domain/actions.yml", "")

def build_domain():
    with open("./backend/domain.yml", "w") as outfile:
        entities(outfile)
        intents(outfile)
        actions(outfile)
        slots(outfile)
        templates(outfile)
        
        

if __name__ == '__main__':
    build_domain()


