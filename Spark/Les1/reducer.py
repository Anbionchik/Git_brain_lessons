
import sys

def reduce():
    prev_key = None
    counter = 0
    for line in sys.stdin:
        vals = line.strip().split("\t")
        if prev_key is None or prev_key == vals[0]:
            prev_key = vals[0]
            counter += 1
            continue
        sys.stdout.write("{}\t{}\n".format(prev_key, counter))
        prev_key = vals[0]
        counter = 1
    if prev_key is not None:
        sys.stdout.write("{}\t{}\n".format(prev_key, counter))
            
            
if __name__ == "__main__":
    mapper()
