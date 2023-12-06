import math
import sys

def main(filename):
    data = {}
    with open(filename, "r") as infile:
        for line in infile.readlines():
            temp = line.split(":")
            data[temp[0]] = [int(x) for x in temp[1].split()]
    #print(data)
    races = []
    for i, value in enumerate(data["Time"]):
            time = data["Time"][i]
            dist = data["Distance"][i]
            counter = 0
            for t in range(time + 1):
                if (time - t) * t > dist:
                    print(t)
                    counter += 1
            races.append(counter)
                #print
    print(math.prod(races))
if __name__ == "__main__":
    main(sys.argv[1])
