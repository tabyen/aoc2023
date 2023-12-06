import sys




def get_value(val_list, value):
    for each in val_list:
        if each[1] > value:
            continue
        elif each[1] + each[2] < value:
            continue
        elif each[1] + each[2] > value:
            value = each[0] + (value - each[1])
    print(value)
    return value

def main(filename):
    order_of_ops = [
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location"
            ]

    data = {}
    seeds = []
    line_num = 0
    with open(filename, "r") as infile:
        for each in infile.readlines():
            line = each.strip()
            if line_num == 0:
                seeds = [int(x) for x in line.replace("seeds: ", "").split()]
                print(seeds)
                line_num += 1
            else:
                if line == "":
                    curr_map = ""
                    continue
                if not curr_map:
                    curr_map = line.replace(" map:", "")
                    data[curr_map] = []
                    continue
                data[curr_map].append(tuple([int(x) for x in line.split()]))
    print(data)
    locations = []
    for seed in seeds:
        working = seed
        for op in order_of_ops:
            working = get_value(data[op], working)
        locations.append(working)
                
    print(locations)


if __name__ == "__main__":
    main(sys.argv[1])
