from collections import Counter #imports counter function from collections 
import random #imports random module 
#the function shows which categories havve potential scoring values for a given dice value 
def posibilities(cast): #posibility dictionary for initialization
    posibility = {
        "ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0,
        "one pair": 0, "two pairs": 0, "three of a kind": 0, "four of a kind": 0, 'five of a kind':0, 'villa':0 , 'tower':0, "small straight": 0, "large straight": 0,'full straight':0, "full house": 0, "chance":0, "yatzy": 0
    }

    #uses counter to count  occurrences of each number
    counts = Counter(cast)

    # Assign values to possibilities based on counts
    for number, count in counts.items():
        if number == 1:
            posibility["ones"] += count
        elif number == 2:
            posibility["twos"] += count * 2
        elif number == 3:
            posibility["threes"] += count * 3
        elif number == 4:
            posibility["fours"] += count * 4
        elif number == 5:
            posibility["fives"] += count * 5
        elif number == 6:
            posibility["sixes"] += count * 6
    
    #cchecks for one pair 
    highest_pair = 0
    for num, count in counts.items():
        if count >= 2:
            pair_value = num * 2
            if pair_value > highest_pair:
                highest_pair = pair_value

    posibility["one pair"] = highest_pair

    #checks for two pairs
    two_pair_values = []
    for num, count in counts.items():
        if count >= 2:
            two_pair_values.append(num)

    if len(two_pair_values) >= 2:
        posibility["two pairs"] = (two_pair_values[0] + two_pair_values[1]) * 2
        
    # Check for the highest "three of a kind"
    highest_three_of_a_kind = 0
    for num, count in counts.items():
        if count >= 3:
            three_of_a_kind_value = num * 3
            if three_of_a_kind_value > highest_three_of_a_kind:
                highest_three_of_a_kind = three_of_a_kind_value
    posibility["three of a kind"] = highest_three_of_a_kind

    #checks for four of a kind 
    for num, count in counts.items():
        if count >= 4:
            posibility["four of a kind"] = num * 4
            break  # Stop after finding the first three of a 

    for num,count in counts.items(): #checks for five of a kind 
        if count >=5:
            posibility['five of a kind'] = num * 5
            break
    if (1 in counts) and (2 in counts) and (3 in counts) and (4 in counts) and (5 in counts): #checks for small straight 
        posibility['small straight'] = 15

    if (2 in counts) and (3 in counts) and (4 in counts) and (5 in counts) and (6 in counts): #checks for large straight 
        posibility['large straight'] = 20

    if (1 in counts) and (2 in counts) and (3 in counts) and (4 in counts) and (5 in counts) and (6 in counts): #checks for full straight 
        posibility['full straight'] = 21
    
    #full house
    two = 0
    three = 0
    for count in counts:
        if counts[count] >= 3:
            if count > three:
                three = count
    for count in counts:
        if counts[num] >= 2 and num != three:
            if count > two:
                two = count
    if two >= 0 and three >= 0:
        posibility['full house'] = sum(cast)

    posibility['chance'] = sum(cast) #checks for chance 


    if len(counts) == 1: #checks for yatzy 
        posibility['yatzy'] = 100

    threekind = [] #checks for villa 
    for num,count in counts.items():
        threekind.extend([num]*(count//3))
    if len(threekind) >= 2:
        posibility['villa'] = sum(cast)

    fourkind = 0
    pair = 0
    for count in counts.values(): #checks for tower
        if count >= 4:
            fourkind = 1
        if count == 2:
            pair = 1
    if fourkind >=1 and pair >=1:
        posibility['tower'] = sum(cast)
    
    for key,value in posibility.items():
        if value != 0:
            print(f'{key}:your value:{value}')

    #prints the potential values directly 
    return posibility #returns the possibility dictionary 
    


    
