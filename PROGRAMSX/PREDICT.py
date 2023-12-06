import COMPUTE

def probability_1v1(hand: list, pile: list):
    
    '''
    Every possible pair of cards that the opponent card (without considering permutation) 
    is simulated and the probability is calculated.
    '''
    
    cards = hand + pile
    deck =[(s, n) for s in "SDCH" for n in range(2, 15)]
    rank, points = COMPUTE.rank_of_best_hand(cards)
    value = -rank*14**7 + points
    
    wins = ties = loses  = 0
    for i in range(52):
        if deck[i] in cards: continue
        for j in range(i+1, 52):
            if deck[j] in cards: continue
            hand_2 = [deck[i], deck[j]]
            rank_2, points_2 = COMPUTE.rank_of_best_hand(hand_2 + pile)
            value_2 = -rank_2*14**7 + points_2
            
            if value>value_2:
                wins += 1
            elif value==value_2:
                ties += 1
            else:
                loses += 1
    total = wins + ties + loses    
    
    return wins/total, ties/total, loses/total

def probability_1v2(hand:list, pile: list):
    
    '''
    Caluculates probabilities against two opponents.
    
    (Result_opp1 Result_opp2 Result_opp3) x permutations --> FinalResult --> probability
    
    (W W) x 1 --> win  --> 1  x  p(w)²
    
    (T T) x 1 --> tie  --> 1  x  p(t)²
    (W T) x 2 --> tie  --> 2  x  p(w)  *  p(t)
    
    (L L) x 1 --> lose --> 1  x  p(l)²
    (T L) x 2 --> lose --> 2  x  p(t)  *  p(l)
    (W L) x 2 --> lose --> 2  x  p(w)  *  p(l)
    
    '''
    
    p_1v1 = probability_1v1(hand, pile)
    w, t, l= p_1v1
    
    win_p = w**2
    tie_p = t**2 + 2*t*w
    lose_p = l**2 + 2*l*t + 2*l*w
    
    return win_p, tie_p, lose_p
     
def probability_1v3(hand: list, pile:list):
    
    '''
    Caluculates probabilities against three opponents.
    
    (Result_opp1 Result_opp2 Result_opp3) x permutations --> FinalResult --> probability
    
    (W W W) x 1 --> win  --> 1  x  p(w)³
    
    (T T T) x 1 --> tie  --> 1  x  p(t)³
    (W T T) x 3 --> tie  --> 3  x  p(w)   *  p(t)²
    (W W T) x 3 --> tie  --> 3  x  p(w)²  *  p(w)
    
    (L L L) x 1 --> lose --> 1  x  p(l)³
    (T L L) x 3 --> lose --> 3  x  p(t)   *  p(l)²
    (T T L) x 3 --> lose --> 3  x  p(t)²  *  p(l)
    (W L L) x 3 --> lose --> 3  x  p(w)   *  p(l)²
    (W W L) x 3 --> lose --> 3  x  p(w)²  *  p(l)
    
    '''
    
    p_1v1 = probability_1v1(hand, pile)
    w, t, l= p_1v1
    
    win_p = w**3
    tie_p = t**3 + 3 * w * t**2 + 3 * w**2 * t
    lose_p = l**3 + 3 * t * l**2 + 3 * t**2 * l + 3 * w * l**2 + 3 * w**2 * l
    
    return win_p, tie_p, lose_p

def probability_1vn(hand: list, pile: list, n=3):
    if n==1: return probability_1v1(hand, pile)
    elif n==2: return probability_1v2(hand, pile)
    else: return probability_1v3(hand, pile)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# ROUND STATES    -->   {0: F_BET/CALL_R, 1: F_CHECK_R}
# STATES (MOVES)  -->   {0: FOLD, 1: CALL, 2: RAISE, 3: CHECK}

def get_move(player_hand, displayed_pile, round_state, min_bet, balance, tolerence, n, no_fold=False):
    
    if balance<min_bet:
        if round_state==0: 
            return 0, 0
        return 3, 0
    
    w, t, l = probability_1vn(player_hand, displayed_pile, n)
    pile_no = len(displayed_pile)
    
    state = 1 if round_state==0 else 3
    bet = min_bet if round_state==0 else 0
    
    if pile_no==0:
        return state, bet
    
    if l < .03 * tolerence:
        return 2, int(max(balance*.5, min_bet+100))
    
    if l < .25 * tolerence:
        r = int(max(min_bet+100, min_bet*(1+w/2)))
        if balance >= r: return 2, r 
        if balance >= min_bet + 100: return 2, min_bet + 100
        return state, bet
    
    if state==3: return state, bet 
    
    if l < (1-min_bet/balance) * tolerence * 2 or no_fold:
        return state, bet

    return 0, 0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
