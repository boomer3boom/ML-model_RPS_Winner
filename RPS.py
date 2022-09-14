# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[], player_history = []):
  #A dictionary with what the best counter is for each move
  counter = { 'R': 'P', 'P': 'S', 'S': 'R' }
  #A list of available moves
  moves = ['R', 'P', 'S']

  #Write a model that keeps track of the frequency to a state.
  #the first parameters of the dictionary is the state, and is read by
  #'RP', opponent plays rock, and player plays paper
  #The dictionary of each state is the frequency the opponent plays a
  #'R', 'P', 'S' on the next round given the current state
  model = {
    'RR':{'R': 0, 'P': 0, 'S': 0},
    'RP':{'R': 0, 'P': 0, 'S': 0},
    'RS':{'R': 0, 'P': 0, 'S': 0},
    'PP':{'R': 0, 'P': 0, 'S': 0},
    'PR':{'R': 0, 'P': 0, 'S': 0},
    'PS':{'R': 0, 'P': 0, 'S': 0},
    'SS':{'R': 0, 'P': 0, 'S': 0},
    'SR':{'R': 0, 'P': 0, 'S': 0},
    'SP':{'R': 0, 'P': 0, 'S': 0}
  }

  if prev_play == '':
    guess = moves[random.randint(0,2)]
    player_history.append(guess)
    return guess

  #Keep track of the opponent's history
  if prev_play != '':
    opponent_history.append(prev_play)
  #If there are no previous move, then randomly select a move

  #How long do we want to keep track of the opponent's history
  memory=-1*min(30,len(opponent_history))
  
  for i, move in enumerate(opponent_history[memory:-1]):
    #move is a opponent's previous and player_history is our move
    #so state gives us a combination of a possible value from the model
    state = move + player_history[memory + i]

    #memory is between -1 to -30. Take memory is -30.
    #first iteration, i = 1. So memory + 0 + 1 = -29.
    #second iteration, i = 2, so memory + 1 +1 = -28.
    #realise how this is the next move after our state
    opponent_next_move = opponent_history[memory + i + 1]
    
    #Increment the number of time the opponent played a
    #'R', 'P', or 'S' after the given state.
    model[state][opponent_next_move] += 1

  #So our previous state is what the opponent player last round, and
  #what we did last round
  current_state = prev_play + player_history[-1]

  #Predict what opponent will play based on frequency of current state
  #key gets all the frequency from the dictionary in our current state.
  prediction = max(model[current_state], key=model[current_state].get)

  our_move = counter[prediction]
  player_history.append(our_move)
  return our_move