# The Following Script aggregates the files located in /stories into stories.md
import glob
import os

def writeSubFile(outfile, subfileName, spacer):
    with open (subfileName) as infile:
        for line in infile.readlines():
            outfile.write(line)

def gen_stories(outfile):
    outfile.write("\n\n")
    writeSubFile(outfile, "./backend/stories/generated_stories.md", "  ")

def custom_stories(outfile):
    outfile.write("\n\n")
    writeSubFile(outfile, "./backend/stories/custom_stories.md", "  ")

def build_stories():
    with open("./backend/stories.md", "w") as outfile:
        custom_stories(outfile)
        gen_stories(outfile)
        

if __name__ == '__main__':
    build_stories()