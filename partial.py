import sys
from collections import Counter

def get_data(filename):
    data = []
    with open(filename, "r") as infile:
        for line in infile.readlines():
            data.append(line.strip().split())
    return data

def score_card(

def main(filename):
    data = get_data(filename)
    


if __name__ == "__main__":
    main(sys.argv[1])
