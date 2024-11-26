from maxiposibility import *
from maxiboard import *
from maxiscoring import *
#imports all functions from all pyfiles
def menu(): #this function is used as a main and partly a menu function that takes choices as inputs and calls the rest of the functions
#initializes lists and dictionaries that are to be used 
    filledcategories = {}
    totalscore = {}
    playerscore = {}
    playernames = []
    filledcategories_all = {}
    bonusawarded = {}
#MAKE SURE TO ANSWER THE QUESTIONS ABOUT REROLLING BEFORE TYPING THE CATEGORY WE GUIDE THE USER TO THIS BUT IT MAY BE MISSED WHEN TRYING TO TYPE FAST #there were some issues with small straight and full straight below 
    #they worked but we changed them now for flexibility to include a case 
    #error handling input for player count while asking for number of players as input
    while True:
        try:
            nplayers = int(input('Enter the number of players: '))
            if nplayers <= 0:
                print("Please enter a positive number of players.")
                continue
            break  #exits loop if valid inputs
        except ValueError:
            print("Invalid input. Please enter a number.")

    #error handling for name input for the players while appending the player names to a list

    for member in range(nplayers):
        while True:
            player = input(f'Enter a name for player {member + 1}: ').strip()
            if not player:
                print("Player name cannot be empty. Please enter a valid name.")
            elif player in playernames:
                print(f"Name '{player}' is already taken. Please choose a different name.")
            else:
                playernames.append(player)  #only adds players name once inside the validation loop
                break  

        playerscore[player] = {}
        totalscore[player] = 0
        filledcategories_all[player] = {}
        bonusawarded[player]=False

    #initialization of player score for specific player and total score as well for each category 
    global highscorename,highscorevalue
    highscorename,highscorevalue = highscoreinstall()
    #error handling for installed highscore from previous game if non highscore values are returned
    if highscorename == '':
        print('no available highscore')
    else:
        print(f'the current highscore is {highscorename}:{highscorevalue}')
#MAKE SURE TO ANSWER THE QUESTIONS ABOUT REROLLS FIRST BEFORE ENTERING A CATEGORY WHEN PLAYING THE GAME WE GUIDE THE USER TO THE INPUT FOR THIS BUT JUST AS A REMINDER
    gamefinished = 0
    try: #error handling for unexpected errors 
        while gamefinished == 0:
            gamefinished = 1  #initializes game is finished unless proven otherwise
            for player in playernames:
                if len(filledcategories_all[player]) < 19:  #checks if each player has categories left to fill
                    gamefinished = 0  #initializes gamefinished to 0 if at least one player has categories left
                    print(f'{player}\'s TURN')
                    cast0 = diceroll([]) #calls diceroll function
                    throws = 0
                    print(f'\n|{player.capitalize()}|') #prints players name then displays the board using the display function after categories have been filled and prints players current total score
                    print(displayscoreboard(filledcategories_all[player]))
                    print(f'Your current total score is: {totalscore[player]}')
                    if not bonusawarded[player]:
                        bonus = bonuscheck(playerscore[player])
                        totalscore[player] += bonus
                        print(f'\nYour current bonus for having >73 uppersection points:{bonus}')
                        bonusawarded[player]=True
                    else:
                        print(f'\nYour current bonus for having >73 uppersection points:{bonus}')
                    
                    while throws < 2: #checks for two rerolls by the rules of the game
                        print(f'Current roll: {cast0}')
                        selection = input("Which dice do you want to reroll? (Enter positions separated by spaces, or 'n' for no rerolls): ")
                        if selection.lower() == 'n':
                            print('No rerolls selected')
                            posibilities(cast0)
                            break  #goes to category choice if 'n' is selected

                        try: #error handling for invalid input 
                            replaceindices = list(map(int, selection.split())) #splts user input to indices converts the input into integers using the map function and creates a list for the new replaced indices 
                            if all(1 <= i <= len(cast0) for i in replaceindices): #checks if each number i is within the valid range of dice positions includes error handling for proper input
                                for i in replaceindices:
                                    cast0[i - 1] = 9  #placement holder for dicevalues that are to be rerolled
                            else:
                                print('Invalid dice positions. Try again.')
                                continue  
                        except ValueError:
                            print('Invalid input. Please enter numbers separated by spaces, or enter "n" to skip.')
                            continue

                        #performs the reroll
                        cast0 = diceroll(cast0)
                        throws += 1
                        print(f'Your new roll: {cast0}')
                        posibilities(cast0)

                        if throws < 2:
                            # error handling for reroll input
                            while True:
                                reroll_prompt = input("Would you like to reroll again? (y/n): ")
                                if reroll_prompt.lower() == 'y':
                                    break # valid input to reroll again
                                elif reroll_prompt.lower() == 'n':
                                    throws = 2
                                    break
                                else:
                                    print("Invalid input. Please enter 'y' for yes or 'n' for no")

                    print('\nProceeding to category choice...')
                    print(f'\n|{player.capitalize()}|') #prints players name then displays the board using the display function after categories have been filled and prints players current total score
                    print(displayscoreboard(filledcategories_all[player]))
                    print(f'Your current total score is: {totalscore[player]}')
                    if not bonusawarded[player]:
                        bonus = bonuscheck(playerscore[player])
                        totalscore[player] += bonus
                        print(f'\nYour current bonus for having >73 uppersection points:{bonus}')
                        bonusawarded[player]=True
                    else:
                        print(f'\nYour current bonus for having >73 uppersection points:{bonus}')
                    category_chosen = False #initializes category as false and then initializes it as true after it was chosen and scored succesfully 
                    
                    while not category_chosen:  
                        result, updated_categories = categorychoice(filledcategories_all[player], cast0) #tuple for the result and the category
                        print(result)
                        if "scored" in result:  #suceess message for scoring showing that the category was scored correctly
                            for category in updated_categories:
                                if category not in playerscore[player]: #checks if the category is in the newly scored categories as well as wether it has already been scored 
                                    score = updated_categories[category] #retrieves score from updated categories 
                                    playerscore[player][category] = score #updates the player score dictionary 
                                    totalscore[player] += score #adds the newly added score to total score 
                                    print(f'Category: {category}, Score: {score}')
                            category_chosen = True
                            break #breaks then calls the displayboard fucntion and prints 
                        else:
                            print('Either all categories are filled or invalid category. Try again.')
                    print(f'\n|{player.capitalize()}|') #prints players name then displays the board using the display function after categories have been filled and prints players current total score
                    print(displayscoreboard(filledcategories_all[player]))
                    print(f'Your current total score is: {totalscore[player]}')
                    if not bonusawarded[player]:
                        bonus = bonuscheck(playerscore[player])
                        totalscore[player] += bonus
                        print(f'\nYour current bonus for having >73 uppersection points:{bonus}')
                        bonusawarded[player] = True
                    else:
                        print(f'\nYour current bonus for having >73 uppersection points:{bonus}')

    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")



    #iterates through player and scores for the name and calls the bonus check function then adds the bonus to the players total score if the achieved the bonus 
    for player in playernames:
        print(f'{player} received {bonus} points as bonus')
    for player in playernames: # iterates through player names then calls the highscore function to chcek if the players total score is the highest score 
        highscorevalue, highscorename = highscore(totalscore[player], player)
    if highscorename: #if the highscore is identified it calls the highscore upload function
        uploadhighscore2(highscorename, highscorevalue) 
    print('\n FINAL SCORES:') #sorts the total scores for the players in descending order using sorted() function and reverse=true  in adittion it uses lambda function to specify that the sorting should only take place for the score of each player
    sortedscore=sorted(totalscore.items(),key=lambda item: item[1],reverse=True)
    winner,topscore=max(sortedscore) #takes the maximum score and the nme of the winner 
    for player,score in sortedscore:
        print(f'{player}:{score}')
    print(f'\n<||>{winner} wins the game with a total of {topscore} points<||>') #dec΄lares the winner based on the highest score

menu()
