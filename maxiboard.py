import random
from maxiscoring import *
#imports all the scoring functions and the random module 
#takes as in input filled or unfilled categories from main and returns them in a board.It checks if they are filled and and returns the scored filled in if they are.
def displayscoreboard(scoredcategories):
    categories=[ "ones", "twos", "threes", "fours", "fives", "sixes",
        "one pair", "two pairs", "three of a kind", "four of a kind",
        "five of a kind","small straight", "large straight","full straight","villa","tower","full house", "chance", "yatzy"]
    lines=['SCOREBOARD']
    for category in categories:
       if category in scoredcategories:
          score=scoredcategories[category]
          lines.append(f'{category}:{score}')
       else:
          lines.append(f'{category}:     ')
    lines.append('')
    output='\n'.join(lines)
    return output
#takes as an input player choice and  the dice values and replaces spaces for better matching
#calls a specific scoring function based on the matching of the choices with the categories  inputs a number to the scorenumber function for calculating ones to sixes depending on the chosen category
def scorecalculation(choice, cast):
    choice = choice.replace(" ", "")  # Remove spaces for consistent matching

    if choice == 'ones':
        return scorenumber(cast, 1)
    elif choice == 'twos':
        return scorenumber(cast, 2)
    elif choice == 'threes':
        return scorenumber(cast, 3)
    elif choice == 'fours':
        return scorenumber(cast, 4)
    elif choice == 'fives':
        return scorenumber(cast, 5)
    elif choice == 'sixes':
        return scorenumber(cast, 6)
    elif choice == 'onepair':
        return onepair(cast)
    elif choice == 'twopairs':
        return twopair(cast)
    elif choice == 'threeofakind':
        return threekind(cast)
    elif choice == 'fourofakind':
        return fourkind(cast)
    elif choice=='fiveofakind':
        return fiveofakind(cast)
    elif choice == 'smallstraight':
        return smallstraight(cast)
    elif choice == 'largestraight':
        return largestraight(cast)
    elif choice=='fullstraight':
        return fullstraight(cast)
    elif choice == 'fullhouse':
        return fullhouse(cast)
    elif choice=='villa':
        return villa(cast)
    elif choice=='tower':
        return tower(cast)
    elif choice == 'chance':
        return sum(cast)
    elif choice == 'yatzy':
        return yatzycheck(cast)
    else:
        return None  #returns none if the category isnt matched 
#takes as an input filled and unfilled categories initializes a list of valid categories 
def categorychoice(filledcategories, cast):
    categories = [
        "ones", "twos", "threes", "fours", "fives", "sixes",
        "one pair", "two pairs", "three of a kind", "four of a kind",
        "five of a kind", "small straight", "large straight", "full straight",
        "villa", "tower", "full house", "chance", "yatzy"
    ]
    #checks if the category is valid if not it prompts the player to try again
    category = input('Enter a category: ').strip().lower()
     
    if category in filledcategories:
        return 'This category is filled, choose a different one', filledcategories  # Return a tuple
    if category not in categories:
        return 'Invalid category, try again', filledcategories  # Return a tuple
    #includes error handling for proper input 
    try:
        score = scorecalculation(category, cast)
        filledcategories[category] = int(score) #converts into an integer 
        return f'You scored {score} points in the {category}', filledcategories  #returns newly scored categories and the scored message if they were scored and chosen succesfully 
    except (ValueError, TypeError):
        return 'Type error or value error, try again', filledcategories #returns the unchanged categories and an error message
