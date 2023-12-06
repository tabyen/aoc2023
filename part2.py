import sys




def get_value(val_list, value):
    #print(f"Value In: {value}")
    for each in val_list:
        if each[1] <= value:
            if value < each[1] + each[2]:
                value = each[0] + (value - each[1])
                break
    #print(f"Value out: {value}")
    return value

def get_back(val_list, value):
    #print(f"Value In: {value}")
    for each in val_list:
        if each[0] <= value and value < each[0] + each[2]:
            value = each[1] + (value - each[0])
            break
    #print(f"Value out: {value}")
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
    
    backward_ops = [
            "humidity-to-location",
            "temperature-to-humidity",
            "light-to-temperature",
            "water-to-light",
            "fertilizer-to-water",
            "soil-to-fertilizer",
            "seed-to-soil"
    ]

    data = {}
    seeds = []
    line_num = 0
    with open(filename, "r") as infile:
        for each in infile.readlines():
            line = each.strip()
            if line_num == 0:
                seeds = [int(x) for x in line.replace("seeds: ", "").split()]
                #sys.exit()
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
    #print(data)
    #locations = []
    ranges = []
    lowest = None
    while len(seeds)> 0:
        end = seeds.pop()
        start = seeds.pop()
        ranges.append((start, end))
    """
    counter = 0
    for item in ranges:
        for i in range(item[0], item[0] + item[1]):
            counter += 1
            if counter%1000000 == 0:
                print(counter)
            working = i
            for op in order_of_ops:
                working = get_value(data[op], working)
            #print(working)
            if lowest is None:
                lowest = working
            elif working < lowest:
                lowest = working
    """
    counter = 0
    for i in range(50000000, 0+198620952):
        counter += 1
        if counter % 1000 == 0:
            print(f"{counter:,d}")
        working = i
        for op in backward_ops:
            working = get_back(data[op], working)
        for each in ranges:
            if each[0] <= working < (each[0] + each[1]):
                print(i)
                sys.exit()
    
    #print(lowest)


if __name__ == "__main__":
    main(sys.argv[1])
