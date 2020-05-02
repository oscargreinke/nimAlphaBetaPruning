import time
moveList = []

def testTiming(state):
     start = time.time()
     value = minimaxValue(state)
     end = time.time()
     print("Time taken:", end-start)
     return value

def minimaxValue(state): # State ([state of piles], whose turn (1/2))
    global moveList
    moveList = []
    if(state[1] == 1):
        val = maxValue(state, None, None)
    else:
        val = minValue(state, None, None)
    moveList.reverse()
    moveList = [state] + moveList
    print(moveList)
    return val
    
def flipTurns(state):
    turn = state[1]
    if turn == 1: #MAX's turn
        turn += 1  #Switch to MIN's turn
        return (state[0], turn)
    elif turn == 2: #MIN's turn
        turn -= 1 #Switch to MAX's turn
        return (state[0], turn)
    else:
        print("Error: Invalid turn number")
        return -1

def isTerminal(state):
    if state[0] == []:
        return True
    else:
        for element in state[0]:
            if element == 0:
                pass
            elif element < 0:
                element = 0
            else:
                return False
        return True

def nextStates(state):
    states = []
    for index, st in enumerate(state[0]):
        if st >= 1:
            tempState = state[0][:]
            del(tempState[index])
            states.append(tempState[:index] + [st-1]+ tempState[index:])
        if st >= 2:
            tempState = state[0][:]
            del(tempState[index])
            states.append(tempState[:index] + [st-2]+ tempState[index:])
        if st >= 3:
            tempState = state[0][:]
            del(tempState[index])
            states.append(tempState[:index] + [st-3]+ tempState[index:])
    return states

def maxValue(state, alpha, beta):
    global moveList
    if isTerminal(state):
        if state[1] == 1:
             return 1
        else:
             return -1
    else:
        utility = (None, -999999999)
        states = nextStates(state)
        for pile in states:
            pile = (pile, state[1]) # make pile into state
            flipTurns(pile)
            pileVal = minValue(pile, alpha, beta) # Get util value of pile
            newUtil = (pile, pileVal) #Compile new utility
            
            if newUtil[1] > utility[1]: # Start pruning
                utility = newUtil
            if beta is None or newUtil[1] >= beta:
                if not isTerminal(utility[0]) and utility[0] not in moveList:
                    moveList.append(utility[0])
                return utility[1]
            if alpha is None or newUtil[1] > alpha: # End pruning
                alpha = newUtil[1]
                
        if not isTerminal(utility[0]) and utility[0] not in moveList:
            moveList.append(utility[0])
        return utility[1]

def minValue(state, alpha, beta):
    global moveList
    if isTerminal(state):
        if state[1] == 1:
            return -1
        else:
            return 1
    else:
        utility = (None, 999999999)
        states = nextStates(state)
        
        for pile in states:
            pile = (pile, state[1]) # make pile into state
            flipTurns(pile)
            pileVal = maxValue(pile, alpha, beta) # Get util value of pile
            newUtil = (pile, pileVal) #Compile new utility
            
            if newUtil[1] < utility[1]: # Start pruning
                utility = newUtil
            if alpha is None or newUtil[1] <= alpha:
                if not isTerminal(utility[0]) and utility[0] not in moveList:
                    moveList.append(utility[0])
                return utility[1]
            if beta is None or newUtil[1] < beta: # End pruning
                alpha = newUtil[1]
                
        if not isTerminal(utility[0]) and utility[0] not in moveList:
            moveList.append(utility[0])
        return utility[1]






    
