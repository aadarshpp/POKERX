def rank_of_best_hand(cards: list[tuple]) -> tuple[int]:
    '''
    Finds the best hand, return rank and points of the hand.
    (*)--> rank: int, points: int (?)                
    (?)--> Rankings:
            1. ROYAL FLUSH
            2. STRAIGHT FLUSH
            3. FOUR OF A KIND
            4. FULL HOUSE
            5. FLUSH
            6. STRAIGHT
            7. THREE OF A KIND
            8. TEO PAIR
            9. PAIR
           10. HIGH CARD
    (?)--> Points:
            After ranking the hand (those cards have highest priority), 
            the rest of the cards are ordered according to their card value (number/face)
            then using get_points() function the points of the hand is calculated.
    '''
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    N = [c[1] for c in cards]
    S = [c[0] for c in cards]
    
    suit_dict = {}
    for i in range(len(S)):
        s = S[i]
        n = N[i] 
        if s not in suit_dict:
            suit_dict[s] = set()
        suit_dict[s].add(n)
        
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def has_royal_flush():
        return set(range(10, 15)) in suit_dict.values()
    
    def has_flush():
        for i in suit_dict.values():
            if len(i)>=5:
                return True 
        return False
    
    def is_straight(L):
        if len(set(L)) < 5 : return False
        return set(L) == set(range(min(L), max(L)+1))
    
    def has_straight(L):
        M = L.copy()
        L = sorted(set(L))
        for i in L:
            M.remove(i)
        n = len(L)
        for s, e in ((0, n), (1, n), (0, -1), (1, -1), (2, n), (0, -2)):
            C = rsort(L[s:e])[:5]
            if is_straight(C):
                return True, C + rsort(list(set(L).difference(C))+list(M))
        if 14 in L:
            L = [i if i!=14 else 1 for i in L]
            return has_straight(L)
        return False, None
    
    def has_straight_flush():
        for L in suit_dict.values():
            Straight, C = has_straight(L)
            if Straight:
                return True, C
        return False, None
    
    # Checks if the hand is:  Royal Flush, Straight Flush, Flush, Straight or High Card
    def check_1() -> tuple:
        if has_royal_flush():
            return 1, 0
        
        StraightFlush, L = has_straight_flush()
        if StraightFlush:
            return 2, get_points(L)
        
        if has_flush():
            return 5, get_points(rsort(N))
        
        Straight, L = has_straight(N)
        if Straight:
            return 6, get_points(L)
        
        return 10, get_points(rsort(N))
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    count = get_counts(N)
    reverse_count = reverse_dict(count)

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def is_four_of_a_kind():
        if 4 in reverse_count:
            return True, reverse_count[4]*4 + rsort([i for i in N if count[i]!=4])
        return False, None
    
    def is_full_house():
        #3 3 1, 3 2 1 1, 3 2 2
        
        if 3 not in reverse_count:
            return False, None
        
        L_3 = reverse_count[3]
        if len(L_3)==2:
            a, b = rsort(L_3)
            return True, [a]*3 + [b]*3 + reverse_count.setdefault(1, [])
        
        if 2 not in reverse_count:
            return False, None
        
        L_2 = reverse_count[2]
        if len(L_2)==1:
            return True, L_3*3 + L_2*2 + reverse_count.setdefault(1, [])
        
        a, b = rsort(L_2)
        return True, L_3 + [a]*2 + [b]*2
    
    def is_three_of_a_kind():
        if 3 in reverse_count:
            L = reverse_count[3]*3 + rsort([i for i in N if count[i]!=3])
            return True, L
        return False, None
    
    def count_pairs():
        if 2 not in reverse_count:
            return 0
        return len(reverse_count[2])
        
    # Check if the hand is : Four of a Kind, Full House, Three of a Kind, Two Pair, Pair or High Card
    def check_2() -> tuple:
        Fours, L = is_four_of_a_kind()
        if Fours:
            return 3, get_points(L)
        
        FullHouse, L = is_full_house()
        if FullHouse:
            return 4, get_points(L)
        
        Threes, L = is_three_of_a_kind()
        if Threes:
            return 7, get_points(L)
        
        PairCount = count_pairs()
        if PairCount==3:
            a, b, c = rsort(reverse_count[2])
            P =  [a]*2 + [b]*2 + rsort([c]*2 + reverse_count.setdefault(1, []))
            return 8, get_points(P)
        
        if PairCount==2:
            a, b = rsort(reverse_count[2])
            P = [a]*2 + [b]*2 + rsort(reverse_count.setdefault(1, []))  
            return 8, get_points(P)
        
        if PairCount==1:
            a = reverse_count[2][0]
            P = [a]*2 + rsort(reverse_count.setdefault(1, []))
            return 9, get_points(P)
        
        return 10, get_points(rsort(N))
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    r1, p1 = check_1()
    
    if r1<3:
        return r1, p1 
    
    r2, p2 = check_2()
    
    if r1<r2:
        return r1, p1 
    
    return r2, p2

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def compare_hands(Hands, folded=tuple()) -> tuple:
    
    '''
    Compares hands and determines the winner(s) among the unfolded hands.
    
    Parameters:
        - Hands: A list containing hands (each hand represented as a list of cards).
        - folded: A tuple containing indices of folded hands.
    
    Returns:
        - A tuple containing the winning indices, rank, and points of the best hand(s).
    '''
    
    W = []
    mx = -14 ** 8
    R, P = 0, 0
    
    for i in range(len(Hands)):
        if i in folded: continue
        r, p = rank_of_best_hand(Hands[i])
        v = -r * 14 ** 7 + p 
        if v > mx:
            mx = v 
            W = [i]
            R, P = r, p 
        elif v == mx:
            W.append(i)
    
    return W, R, P

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def get_points(N):
    
    '''
    Calculates points for a given hand by converting each card values to a base-14 number
        (?) N = [7, 7, 5, 5, 10, 3, 1] --> (7766T31) in base 14*
        (*) - 14 digits are: 1, 2, 3, 4, 5, 6, 7, 8, 9, T, J, K, Q, A
    '''
    
    points = 0
    for i in range(len(N)):
        points += (N[-i-1]-1) * 14**i 
    return points

# Counts the occurrences of each card value in a hand and returns a dictionary
def get_counts(N):    
    count_dict = {}
    for i in N:
        if i not in count_dict:
            count_dict[i] = 0 
        count_dict[i] += 1
    return count_dict

def reverse_dict(d):
    # Reverses a dictionary, grouping keys by their values.
    # {2:2, 10:1, 9:1} --> {2:[2], 1:[10, 9]}
    
    reverse_d = dict()
    for (k, v) in d.items():
        if v not in reverse_d:
            reverse_d[v] = []
        reverse_d[v] += [k]
    return reverse_d

def rsort(L):
    return sorted(L, reverse=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

from random import randrange

# Draws a specified number of unique random cards from a list
def get_random_from(n, L):
    cards = []
    for _ in range(n):
        card_indx = randrange(len(L))
        card = L.pop(card_indx)
        cards.append(card)
    return cards
    
def convert(x):
    A = "123456789TJQKA"   
    d = x%14
    x = x//14
    if x==0:
        return A[d]
    return convert(x) + A[d]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

poker_hands = ("ROYAL\n    FLUSH", "STRAIGHT\n   FLUSH", "FOUR OF\n    A KIND", "FULL HOUSE",
               "FLUSH", "STRAIGHT", "THREE OF\n    A KIND", "TWO PAIR", "PAIR", "HIGH CARD")

names = ["Michael", "Scott", "David", "Dwight", "Pam", "Jim", "Erik", "Joey", "Barney", "Robin", "Dom", "Nas"]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#