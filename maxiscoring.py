import random
#imports random module 
def diceroll(reroll): #defines diceroll function takes in a list if the list is empty creates the dice roll for the game if not it checks which values are to be rerolled basedon the placement holder 9 in cooperation with main
    rolls=[]
    if not reroll:
      for i in range(6):
       roll=random.randint(1,6)
       rolls.append(roll)
    elif reroll:
       for i in range(len(reroll)):
          if reroll[i]==9:
             reroll[i]=random.randint(1,6)
       rolls=reroll
    return rolls

def totalscore(dice): 
    return sum(dice)

def fiveofakind(dice): #checks for a five of a kind by using the count function so see the number of elements with a specified value then retruns the sum 
    for die in dice:
        if dice.count(die)>=5:
          return die*5
    return 0


def yatzycheck(dice): #checks for a yatzy  by using the count function so see the number of elements with a specified value then returns 1o0 points  
    score=0
    if dice.count(dice[0])==6:
        score=100
    return score

def scorenumber(dice,number): #scores the ones-sixes categories by using the count function to check number of elements with a specified value then returns the multiplication and takes in a number as an input
    count=dice.count(number)
    score=count*number
    return score
def scorepair(dice):
    pairs=[]
    for die in set(dice):
        if dice.count(die)>=2:
            pairs.append(die)
    score=0
    highestpair=0
    if len(pairs)>0:
        highestpair=max(pairs)
    else:
        highestpair=0
    score=highestpair*2
    return score

def onepair(dice):  #checks for one pair by using the count function so see the number of elements with a specified value then retruns the sum.Also iterates through the dice values in a descending order to always return the largest one pair
    for die in range(6,0,-1):
        if dice.count(die)>=2:
            score=die*2
            return score
    return 0
def twopair(dice): #checks for two pairs by appending thems to a list using the count function so see the number of elements with a specified value then retruns the sum.Also iterates through the dice values in a descending order to always return the largest pairs
    pairs=[]
    for die in range(6,0,-1):
        if dice.count(die)>=2:
            pairs.append(die)
    if len(pairs)>=2:
        score=(pairs[0]*2)+(pairs[1]*2)
        return score
    return 0

def threekind(dice):  #checks for three kind by using the count function so see the number of elements with a specified value then retruns the sum.Also iterates through the dice values in a descending order to always return the largest three kind
    for die in range(6,0,-1):
        if dice.count(die)>=3:
            score=die*3
            return score
    return 0

def fourkind(dice):  #checks for a four of a kind by using the count function so see the number of elements with a specified value then retruns the sum 
    for die in dice:
        if dice.count(die)>=4:
            score=die*4
            return score
    return 0
def smallstraight(dice): #checks for a small straight by seeing if the sorted and unique dice values match the small straight numbers
    sorteddice=sorted(set(dice))
    if sorteddice==[1,2,3,4,5] or sorteddice==[1,2,3,4,5,6]:
        return 15
    return 0

def largestraight(dice): #checks for a large  straight by seeing if the sorted and unique dice values match the small straight numbers
    sorteddice=sorted(set(dice))
    if sorteddice==[2,3,4,5,6] or sorteddice==[1,2,3,4,5,6]:
        return 20
    return 0
def fullstraight(dice): #checks for a full  straight by seeing if the sorted and unique dice values match the small straight numbers
    sorteddice=sorted(set(dice))
    if sorteddice==[1,2,3,4,5,6]:
        return 21
    return 0

def fullhouse(dice): #checks for full house by utilizing a dictionary to keep count of how many times a dice value appears.Then checks if the frequencies match the full house combination and returns sum 
    counts={}
    for die in dice:
        if die in counts:
            counts[die]+=1
        else:
            counts[die]=1
    pair=0
    triple=0
    fullhousesum=0
    for die in sorted(counts,reverse=True):
        if counts[die]>=3 and triple==0:
            triple=die
            fullhousesum+=die*3
            counts[die]-=3
    for die in sorted(counts,reverse=True):
        if counts[die]>=2 and pair==0:
            pair=die
            fullhousesum+=die*2
    
    if triple and pair:
        return sum(dice)
    return 0   
    
def villa(dice): #checks for villa by utilizing a dictionary to keep count of how many times a dice value appears.Then checks if the frequencies match the villa combination and returns sum
    counts = {}
    for die in dice:
        if die in counts:
            counts[die]+=1
        else:
            counts[die]=1
    threeofkind=0
    for count in counts.values():
        if count >= 3:
            threeofkind += count // 3
    if threeofkind >= 2:
        return sum(dice)
    return 0

def tower(dice): #checks for tower by utilizing a dictionary to keep count of how many times a dice value appears.Then checks if the frequencies match the tower combination and returns sum
    counts={}
    for die in dice:
        if die in counts:
            counts[die]+=1
        else:
            counts[die]=1
    countfour=0
    counttwo=0
    for die in counts:
        if counts[die]>=4:
            countfour+=1
        elif counts[die]==2:
            counttwo+=1
    if countfour>=1 and counttwo>=1:
        return sum(dice)
    return 0
        
def bonuscheck(scoredcategories): #checks if the upper section categories are more than 73 points then returns the 50 point bonus.It does this by defining a list that matche the upper section categories of of all categories and summing them in score
    uppersection = ['ones','twos','threes','fours','fives','sixes']
    upperscore = 0
    for category in uppersection:
        if category in scoredcategories:
            upperscore += scoredcategories[category]
        if upperscore >= 73:
            return 50
    return 0
    
#change global variable names to avoid conflicts with function names
highest_score = 0
highscorename = ''

def highscore(totalscore, playername): #takes as an iput the players total score and playername checks if total score is the highest score  in cooperation with main
    global highest_score, highscorename  #updates variable name
    if totalscore > highest_score:       #uses updated variable here
        highest_score = totalscore       
        highscorename = playername
    return highest_score, highscorename

def highscoreinstall(): #error handling for valueerror and file errors, reads the file and returns the highscore name in the file as well as the highscore converted into an integer 
    try: 
        with open('highscore.txt','r') as file:
            score = file.read().strip().split(':')
            if len(score) == 2:
                highscorename = score[0]
                highscore = int(score[1])
                return highscorename, highscore
            else:
                return '',0  # Fallback if the file doesn’t contain two elements
    except (ValueError, FileNotFoundError):  # Handle both missing file and value errors
        return '',0  #retrun values if theres an error 

def uploadhighscore(highscorename, highscore):
    with open('highscore.txt', 'w') as file:
        file.write(f'{highscorename},{str(highscore)}')


def uploadhighscore2(highscorename, highscore): #sorts the highscores in the file in desceding order using a sorting algorithm then writes the new highscore based on the order ,if theres a file error it creates a new file with the current highscore
    try:
        with open('highscore.txt','r') as file:
            lines = file.readlines()
        highscores = []
        for line in lines:
            if line.strip():
                name,score = line.strip().split(':')
                highscores.append((name,int(score)))
        highscores.append((highscorename,highscore))
        for i in range(len(highscores)):
            for j in range(i+1,len(highscores)):
                if highscores[j][1] > highscores[i][1]:
                    highscores[i],highscores[j] = highscores[j],highscores[i]
        with open('highscore.txt','w') as file:
            for name,score in highscores:
                file.write(f'{name}:{score}\n')
    except FileNotFoundError:
        with open('highscore.txt','w') as file:
            file.write(f'{highscorename}:{highscore}\n')
