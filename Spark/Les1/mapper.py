
import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            sys.stdout.write("{}\t{}\n".format(word, 1))
            
if __name__ == "__main__":
    mapper()
