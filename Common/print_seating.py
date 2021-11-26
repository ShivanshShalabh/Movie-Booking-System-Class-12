from string import ascii_uppercase


def print_seating(raw_str):
    raw_str = raw_str.split("|")
    height = len(raw_str)
    width = 0
    for i in range(len(raw_str)):
        temp_width = len(raw_str[i])-raw_str[i].count("-")
        raw_str[i] = raw_str[i].split("-")
        width = max(temp_width, width)
        
    l = len(str(height))
    print(l*" ", end=" ")
    width_partition = [0]
    for i in raw_str[0]:
        print(
            ascii_uppercase[width_partition[-1]:width_partition[-1]+len(i)], end=" ")
        
        width_partition.append(len(i)+width_partition[-1])
    
    print()

    for i in range(height):
        print(" "*(l-len(str(i+1)))+str(i+1), end=" ")
        print(" ".join(raw_str[i]))
