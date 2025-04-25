# Importing in-build/installed modules
import customtkinter as ctk
from PIL import Image

# Importing user defined modules
import COMPUTE
import PREDICT

# Creating a ctk window
win = ctk.CTk(fg_color="black")
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.title("Poker")
win.geometry(f"{w}x{h}+0+0")

# Returns the path for an image file
def path(imagename):
    return fr"./IMAGES/{imagename}"

# Returns the path for a card image based on the card value
def cardpath(c):
    
    '''
    NAMING METHOD:
       (1) Most cards -->  "{card_no*} of {first letter of suit}.png"
       (*) Face cards are given a number --> {Jack: 11, Queen: 12, King: 13, Ace: 14*}
       (*) Ace can take both values 1 and 14, for naming it's taken as 14 for convinience
       (2) Back of a card -->  -1
       (3) FOLDED card (back) --> -2
    '''
    
    if c is None:
        return None
    if c == -1:
        return r"CARDS\BACK.png"
    if c == -2:
        return r"CARDS\FOLDED.png"
    return f"CARDS\{c[1]} of {c[0]}.png"

def bgimage(imagename, Size=(w, h)):
    
    '''
    Displays a new background image on the window.
    
    Parameters:
    - imagename (str): The name of the image file.
    - Size (tuple, optional): The size of the image. Defaults to window size.
    
    Returns:
    ctk.CTkLabel: The label displaying the background image.
    '''
    
    bg_image = ctk.CTkImage(light_image=Image.open(path(imagename)), size=Size)
    label = ctk.CTkLabel(win, image=bg_image, text="", bg_color="black")
    label.place(x=0, y=0, relwidth=1, relheight=1)
    return label

def imagebutton(Imagename, Size, Rx=.5, Ry=.5, Command=None, fg_c="black", hover_c="white"):
    
    '''
    Places a button with an image and text(optonal) at a given position.
    
    Parameters:
    - Imagename (str): The name of the image file for the button.
    - Size (tuple): The size of the button.
    - Rx (float, optional): The relative x-coordinate of the button. Defaults to 0.5.
    - Ry (float, optional): The relative y-coordinate of the button. Defaults to 0.5.
    - Command (function, optional): The function to be called when the button is clicked.
    - fg_c (str, optional): The foreground color of the button. Defaults to "black".
    - hover_c (str, optional): The hover color of the button. Defaults to "white".
    
    Returns:
    ctk.CTkButton: The created image button.
    '''
    
    img = ctk.CTkImage(Image.open(path(Imagename)), size=Size)
    button = ctk.CTkButton(win, text="", image=img, fg_color=fg_c, bg_color=fg_c, hover_color=hover_c, command=Command, corner_radius=0)
    button.place(relx=Rx, rely=Ry, anchor="center")
    return button

# Places a label with an image and optional text at a given position
def imagelabel(Imagename, Size, Text="", Font=("kongtext", 20), Rx=.5, Ry=.5, fg_c="black", Anchor="center"):
    
    '''
    Places a label with an image and optional text at a given position.
    
    Parameters:
    - Imagename (str): The name of the image file for the label.
    - Size (tuple): The size of the label.
    - Text (str, optional): The text to be displayed on the label. Defaults to an empty string.
    - Font (tuple, optional): The font for the text. Defaults to ("kongtext", 20).
    - Rx (float, optional): The relative x-coordinate of the label. Defaults to 0.5.
    - Ry (float, optional): The relative y-coordinate of the label. Defaults to 0.5.
    - fg_c (str, optional): The foreground color of the label. Defaults to "black".
    - Anchor (str, optional): The anchor position of the label. Defaults to "center".
    
    Returns:
    ctk.CTkLabel: The created image label.
    '''
    
    if Imagename is None:
        return
    image = ctk.CTkImage(light_image=Image.open(path(Imagename)), size=Size)
    label = ctk.CTkLabel(win, image=image, text=Text, font=Font, fg_color=fg_c, corner_radius=0, anchor=Anchor)
    label.place(relx=Rx, rely=Ry, anchor=Anchor)
    return label

# Places a button with given text at a given position
def textbutton(Text, Command, Font=("kongtext", 30), fg_c="black", hover_c="white", text_c="grey", width=40, height=40, Rx=0, Ry=0, Anchor="center"):
    
    '''
    Places a button with given text at a given position.
    
    Parameters:
    - Text (str): The text to be displayed on the button.
    - Command (function): The function to be called when the button is clicked.
    - Font (tuple, optional): The font for the text. Defaults to ("kongtext", 30).
    - fg_c (str, optional): The foreground color of the button. Defaults to "black".
    - hover_c (str, optional): The hover color of the button. Defaults to "white".
    - text_c (str, optional): The color of the text. Defaults to "grey".
    - width (int, optional): The width of the button. Defaults to 40.
    - height (int, optional): The height of the button. Defaults to 40.
    - Rx (float, optional): The relative x-coordinate of the button. Defaults to 0.5.
    - Ry (float, optional): The relative y-coordinate of the button. Defaults to 0.5.
    - Anchor (str, optional): The anchor position of the button. Defaults to "center".
    
    Returns:
    ctk.CTkButton: The created text button.
    '''
    
    button = ctk.CTkButton(win, width, height, text=Text, font=Font,
                           text_color=text_c, fg_color=fg_c, hover_color=hover_c,
                           corner_radius=0, command=Command)
    button.place(relx=Rx, rely=Ry, anchor=Anchor)
    return button

def back_button(prev, font=("kongtext", 30)): return textbutton("<", prev, Font=font, Rx=0, Ry=0, Anchor="nw")
def next_button(next): textbutton(">", Command=next, Rx=1, Ry=0, Anchor="ne")
def full_back_button(): textbutton("<<", Command=home, Rx=1, Ry=0, Anchor="ne")

def textlabel(Text='', wd=0, ht=28, Font=('kongtext', 20), Rx=0, Ry=0, fg_c='black', Anchor='center'):
    
    '''
    Places a label with given text at a given position.

    Parameters:
    - Text (str, optional): The text to be displayed on the label. Defaults to an empty string.
    - wd (int, optional): The width of the label. Defaults to 0.
    - ht (int, optional): The height of the label. Defaults to 28.
    - Font (tuple, optional): The font for the text. Defaults to ('kongtext', 20).
    - Rx (float, optional): The relative x-coordinate of the label. Defaults to 0.5.
    - Ry (float, optional): The relative y-coordinate of the label. Defaults to 0.5.
    - fg_c (str, optional): The foreground color of the label. Defaults to 'black'.
    - Anchor (str, optional): The anchor position of the label. Defaults to 'center'.

    Returns:
    ctk.CTkLabel: The created label.
    '''
    
    label = ctk.CTkLabel(win, text=Text, width=wd, height=ht, font=Font, fg_color=fg_c, corner_radius=0, anchor=Anchor)
    label.place(relx=Rx, rely=Ry, anchor=Anchor)
    return label

# Creates a page with background, back, and optional next/full-back buttons
def page(bg, prev, next=None, full_back=False):
    
    '''
    Creates a page with a background and places back and next/full-back (optional) buttons.

    Parameters:
    - bg (str): The name of the background image file.
    - prev (function): The function to be called when the back button is clicked.
    - next (function, optional): The function to be called when the next button is clicked. Defaults to None.
    - full_back (bool, optional): If True, a full back button is added. Defaults to False.
    '''
    
    bgimage(bg)
    back_button(prev)
    if next is not None: next_button(next)
    if full_back: full_back_button()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Initiates the start screen with an image label and transitions to the home screen after a delay.
def start():    
    win.overrideredirect(True)
    l = imagelabel('START.PNG', Size=(w, h), Rx=.5, Ry=.5)
    l.after(2500, home)
    
    
# Displays the home screen with background image and buttons to play, learn, cheat, and exit.
def home():
    bgimage('HOME_SCREEN.PNG')
    
    imagebutton('PLAY.PNG', (300, 100), Rx=.6, Ry=.16, Command=lambda: loading(0))
    imagebutton('LEARN.PNG', (300, 100), Rx=.6, Ry=.38, Command=learn)
    imagebutton('CHEAT.PNG', (300, 100), Rx=.6, Ry=.60, Command=lambda: loading(1))
    imagebutton('EXIT.PNG', (300, 100), Rx=.6, Ry=.82, Command=win.quit, hover_c='red')

def loading(n):
    
    '''
    Displays a loading screen with a specific image based on the parameter 'n' and transitions to the next screen.
    
    Parameters:
    - n (int): Indicates the type of loading screen.
    '''
    
    loading_screens = ('LOADING_C.PNG', 'LOADING_J.PNG')
    l = bgimage(loading_screens[n])
    if n == 0: 
        l.after(2000, lambda: game(0))
    if n == 1: 
        l.after(2000, cheat)

# Initiates the learning section, starting with the 'How To Play' page.
def learn():
    def how_to(): 
        page('HOW_TO.PNG', prev=home, next=hands_rank_1)
    def hands_rank_1(): 
        page('HANDS_RANK_1.PNG', prev=how_to, next=hands_rank_2)
    def hands_rank_2(): 
        page('HANDS_RANK_2.PNG', prev=hands_rank_1, next=hands_rank_3)
    def hands_rank_3(): 
        page('HANDS_RANK_3.PNG', prev=hands_rank_2, next=bettings)
    def bettings(): 
        page('BETTINGS.PNG', prev=hands_rank_3, next=round_types_1)
    def round_types_1(): 
        page('ROUND_TYPES_1.PNG', prev=bettings, next=round_types_2)
    def round_types_2(): 
        page('ROUND_TYPES_2.PNG', prev=round_types_1, full_back=True)
        
    how_to()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#    

# Activated cheats: [1v1 odds, total odds, show rank, show community cards]
activated = [False] * 4

# Displays the cheat screen allowing users to activate specific cheats
def cheat():
    bgimage('CHEAT_BLACK.png')

    # Places buttons with given foreground and text colors
    def buttons(cfg, ctc, qfg, qtc):
        back_button(home, font=('kongtext', 42))
        textbutton('c', cheat_main, ('kongtext', 42), fg_c=cfg, text_c=ctc, Rx=0, Ry=0.1, Anchor='nw')
        textbutton('?', cheat_about, ('kongtext', 42), fg_c=qfg, text_c=qtc, Rx=0, Ry=0.2, Anchor='nw')

    def cheat_about():
        # Displays information about cheats
        bgimage('CHEAT_ABOUT.png')
        buttons('black', 'grey', 'blue', 'white')

    def cheat_main():
        # Displays the main cheat screen with activated cheat buttons
        bgimage('CHEAT_MAIN.png')
        buttons('blue', 'white', 'black', 'grey')

        for i in range(len(activated)):
            on(i) if activated[i] else off(i)

        textbutton(' OFF ', Font=('kongtext', 40), Command=err, Rx=.7, Ry=4*.195+.102, fg_c='black', text_c='red', width=50, height=30)

    def on(n):
        # Activates the cheat at index 'n'
        textbutton(' ON ', Font=('kongtext', 40), Command=lambda: off(n), Rx=.7, Ry=n*.197+.102, fg_c='black', text_c='green')
        activated[n] = True

    def off(n):
        # Deactivates the cheat at index 'n'
        textbutton(' OFF ', Font=('kongtext', 40), Command=lambda: on(n), Rx=.7, Ry=n*.197+.102, fg_c='black', text_c='red', width=50, height=30)
        activated[n] = False

    def err():
        # Displays an error message and returns to the start screen
        errlabel = bgimage('ERR_G.png')
        errlabel.after(7000, lambda: start())

    cheat_main()

# Displays information based on activated cheats
def cheat_box(hand):
    global display_pile
    
    # Check if any cheats are activated
    if True not in activated:
        return
    
    displayed_cards = [i for i in display_pile if type(i) is tuple]

    msg = ''

    # Display 1v1 odds if activated
    if activated[0]:
        p1v1 = PREDICT.probability_1v1(hand, displayed_cards)
        wp, tp, lp = map(lambda x: str(int(100*x)).ljust(3), p1v1)
        lp = str(100-int(wp)-int(tp)).ljust(3)
        msg += f'\n 1V1  : W {wp} T {tp} L {lp}\n'

    # Display total odds if activated
    if activated[1]:
        ptot = PREDICT.probability_1vn(hand, displayed_cards, 3-len(folded))
        wp, tp, lp = map(lambda x: str(int(100*x)).ljust(3), ptot)
        lp = str(100-int(wp)-int(tp)).ljust(3)
        msg += f'\n TOT  : W {wp} T {tp} L {lp}\n'

    # Display hand rank if activated
    if activated[2]:
        r, p = COMPUTE.rank_of_best_hand(hand+displayed_cards)
        msg = f'\nRANK : {poker_hands[r-1]}\n' + msg

    # Display that the show community cards cheats is actiavted
    if activated[3]:
        msg = '\nSHOW CC : ACTIVATED\n' + msg

    # Display the information using an image label
    imagelabel('BLACK_BG.png', Size=(370, 210), Text=msg, Font=('kongtext', 14), Rx=.85, Ry=.15)


        
# Displays a slider to raise the bet and executes it if confirmed
def raise_bet(round_no, balances):
    global min_bet
    mn, mx = min_bet, balances[0]
    
    # Check if minimum bet is greater than the maximum balance
    if mn > mx:
        msg = f"Minimum bet is\n{min_bet}"
        imagelabel("BLACK_BG.PNG", Text=msg, Size=(370, 210), Rx=.85, Ry=.76)
        return
        
    # Initialize the amount label with the minimum bet
    amount_label = ctk.CTkLabel(win, corner_radius=0, text=str(min_bet))
    amount_label.place(relx=.87, rely=.67)
    imagelabel("BLACK_BOX.PNG", Size=(370, 210), Rx=.85, Ry=.76)
    
    # Function to update the displayed amount based on slider value
    def slider_disp(Text):
        nonlocal amount_label
        amount_label.destroy()
        amount_label = ctk.CTkLabel(win, corner_radius=0, text=Text, font=("Kongtext", 20), fg_color="transparent")
        amount_label.place(relx=.87, rely=.67)
        return amount_label
    
    val = mn
    # Event handler for the slider
    def slider_event(value):
        nonlocal val 
        slider_disp(int(value/100)*100)
        if int(value) == mx: val = mx
        else: val = int(value/100)*100
        
    slider = ctk.CTkSlider(master=win, from_=mn, to=mx, orientation="vertical", command=slider_event)
    slider.place(relx=0.8, rely=0.76, anchor="center")
    slider.set(mn)
    
    # Confirm button to execute the bet
    def confirm():
        global min_bet
        min_bet = val
        slider.destroy()
        tbutton.destroy()
        amount_label.destroy()
        game(round_no+1, state=2)
        
    tbutton = textbutton("CONFIRM", Font=("kongtext", 20), Command=confirm, Rx=.9, Ry=.82)

# Convenience function that returns the text to be displayed at the end of a game
def endroundmsg(w, r, p, perwin):
    msg = ""
    fontsize = 20
    
    # Check if the player won
    if w == [0]:
        msg += f"You won\n\nYou got {perwin} $"
         
    else:
        ws = ""
        for i in w: ws += players[i]+",\n" if i!=0 else ""
        fontsize = 20 * (len(w)+4)/7
        
        # Check if the game ended in a tie
        if 0 in w:
            msg += f"You tied with {ws[:-2]}\n\nYou got {perwin} $"
        else:
            msg += f"You {('lost', 'folded')[0 in folded]}\n{('Winner is ' if len(w)==1 else 'Winners are ')}{ws[:-2]}"

    msg += f"\n\nRANK: {poker_hands[r-1]}"
    return msg, fontsize

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# declairing global variables
realhands = None 
realpile = None
display_pile = None
display_hands = None
bets = None
balances = None
folded = None
player_folded = False
raised_by = [False, 0]
min_bet = 100
poker_hands = COMPUTE.poker_hands
players = ["You"] + COMPUTE.get_random_from(3, COMPUTE.names)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Display the game screen for the given round
def play(round_no, first=False, showdown=False):
    global realhands, realpile, display_pile, display_hands, bets, balances, raised_by
    
    # Initialization for the first round
    if first:
        # Set up the background and table image
        bgimage("PLAY_BG.PNG")
        imagelabel("TABLE.png", (600, 230), Ry=.47)
        
    # Activate cheat box if needed
    if activated[-1]:
        display_pile = realpile
    cheat_box(realhands[0])
    
    t = 0.072
    for i in range(5):
        a = .356 + t * i
        if display_pile[i] is not None:
            # Display cards on the table
            imagelabel(cardpath(display_pile[i]), Size=(250 * .4, 363 * .4), fg_c="#005E38", Rx=a, Ry=.47)
            
    # STATES (MOVES)  -->   {0: FOLD, 1: CALL, 2: RAISE, 3: CHECK}
    
    global raised_by
    if raised_by[1] == 0:
        raised_by[0] = False
    
    # Function to handle game state transitions
    def game_call(state):
        if bets[0] + balances[0] < 100 and round_no < 3:
            # Player is out of money
            exitlabel = ctk.CTkLabel(win, w, h, corner_radius=0, text="YOU ARE OUT OF MONEY\n\n...", font=("kongtext", 40), text_color="#870101")
            exitlabel.place(relx=.5, rely=.5, anchor="center")
            exitlabel.after(1000, home)
            return
        if sum(bets[1:]) + sum(balances[1:]) == 0:
            # Player won the game
            exitlabel = ctk.CTkLabel(win, w, h, corner_radius=0, text=f"YOU WON THE GAME\n\nWON {balances[0]}$", font=("kongtext", 40), text_color="white")
            exitlabel.place(relx=.5, rely=.5, anchor="center")
            exitlabel.after(1000, home)
            return
        if showdown:
            if state == 0:
                game(0, new=False)
            return
        if state == 2:
            raise_bet(round_no, balances)
        else:
            game(round_no + 1, state)
    
    # Display buttons based on player actions
    if player_folded:
        # Display buttons for a folded player
        imagebutton("BLACK.png", (1100, 60), fg_c="black", hover_c="white", Rx=.5, Ry=.94, Command=lambda: game_call(0))
        imagebutton("NEXT.png", (180, 45), fg_c="black", hover_c="black", Rx=.5, Ry=.94, Command=lambda: game_call(0))
    else:
        # Display buttons for an active player
        
        imagebutton("FOLD.png", (180, 60), fg_c="black", hover_c="blue", Rx=.2, Ry=.94, Command=lambda: game_call(0))
        if first:
            imagebutton("BET.png", (180, 60), fg_c="black", hover_c="green", Rx=.5, Ry=.94, Command=lambda: game_call(1))
        elif raised_by[0]:
            imagebutton("CALL.png", (180, 60), fg_c="black", hover_c="green", Rx=.5, Ry=.94, Command=lambda: game_call(1))
        else:
            imagebutton("CHECK.png", (180, 60), fg_c="black", hover_c="green", Rx=.5, Ry=.94, Command=lambda: game_call(3))
        imagebutton("RAISE.png", (180, 60), fg_c="black", hover_c="red", Rx=.8, Ry=.94, Command=lambda: game_call(2))
        
    if showdown:
        display_pile = realpile
        display_hands = realhands
    
    X = (.5, .15, .5, .85)
    Y = (.79, .46, .14, .46)
    for i in range(4):
        if display_hands[i] is None:
            continue
        if i != 0:
            textlabel(players[i], wd=250 * .85, Rx=X[i], Ry=Y[i] - 363 * .27 / 864)
        # Display opponent cards
        imagelabel(cardpath(display_hands[i][0]), Size=(250 * .4, 363 * .4), fg_c="#193528", Rx=X[i] - t/2, Ry=Y[i])
        imagelabel(cardpath(display_hands[i][1]), Size=(250 * .4, 363 * .4), fg_c="#193528", Rx=X[i] + t/2, Ry=Y[i])
        
    # Display bet and balance information
    def numstr(n):
        ns = str(n).center(5)
        if n >= 100000:
            ns = f"{round(n/100000, 2)} L"
        return f"  {ns}"
    d = .105
    
    X2 = (.448, .098, .448, .798)
    Y2 = (.66, .59, .27, .59)
    for i in range(4):
        if bets[i] is not None:
            # Display bet information
            imagelabel("BET_BOX.PNG", (190 * .8, 55 * .8), Text=numstr(bets[i]), Rx=X2[i], Ry=Y2[i])
        if balances[i] is not None:
            # Display balance information
            imagelabel("BALANCE_BOX.PNG", (190 * .8, 55 * .8), Text=numstr(balances[i]), Rx=X2[i] + d, Ry=Y2[i])
    
    # Display leave button
    def leave():
        tlabel = ctk.CTkLabel(win, w, h, corner_radius=0, text=f"YOU LEFT WITH\n\n{balances[0]}$", font=("kongtext", 40))
        tlabel.place(relx=0.5, rely=0.5, anchor="center")
        tlabel.after(1000, home)
        
    textbutton("LEAVE", Rx=0, Ry=0, Anchor="nw", Command=leave)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Execute player and opponent moves and call play() accordingly
def game(round_no, state=1, new=True):
    global realhands, realpile, display_pile, display_hands, bets, balances, min_bet, folded, player_folded
    
    # Initialization for the first round
    if round_no == 0:
        deck = [(s, n) for s in 'SCDH' for n in range(2, 15)]
        folded = []
        realhands = [COMPUTE.get_random_from(2, deck) for _ in range(4)]
        realpile = COMPUTE.get_random_from(5, deck)
        display_pile = [-1] * 5
        display_hands = [realhands[0]] + [(-1, -1)] * 3
        bets = [0] * 4
        # Initialize balances if new round
        if balances is None or new:
            balances = [10000] * 4
        player_folded = False
        play(round_no, first=True)
        return
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def showdown():
        global min_bet, bets
        
        # Calculate the winning hands, ranks, and players
        considered_cards = [hand + realpile for hand in realhands]
        w, r, p = COMPUTE.compare_hands(considered_cards, folded)
        
        # Calculate the amount each player wins
        perwin = int(sum(bets) / len(w))
        
        for i in w:
            balances[i] += perwin
        
        # Generate the end-of-round message
        msg, fontsize = endroundmsg(w, r, p, perwin)
        
        # Display all cards
        play(round_no=5, showdown=True)
        
        # Reset bets to zero for the next round
        bets = (0,) * 4
        
        def display():
            # Display the result message
            imagelabel("BLACK_BG.PNG", Text=msg, Font=("kongtext", fontsize), Size=(370, 210), Rx=.85, Ry=.76)
            
            if not player_folded:
                # Display buttons for the next round
                imagebutton("BLACK.png", (1100, 60), fg_c="black", hover_c="grey", Rx=.5, Ry=.94, Command=lambda: game(0, new=False))
                imagebutton("NEXT.png", (180, 45), fg_c="black", hover_c="black", Rx=.5, Ry=.94, Command=lambda: game(0, new=False))
        
        # Display the result after a short delay
        l = textlabel(Rx=1, Ry=0)
        sleep = 1500
        l.after(sleep, display)
        min_bet = 100

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    '''
    Round states and move states:
        ROUND STATES    -->   {0: F_BET/CALL_R, 1: F_CHECK_R}
        STATES (MOVES)  -->   {0: FOLD, 1: CALL, 2: RAISE, 3: CHECK}
    '''
    
    # Initialize variables for the current round
    msg = ""
    display_hands = [realhands[0]] + [(None, None)] * 3

    # Check if the player has folded
    if state == 0:
        player_folded = True
        folded.append(0)
        
    # Iterate through players to determine their moves
    for i in range(4):
        global raised_by
        
        if i in folded:
            continue
        
        # Reset the raise tracking if the current player raised in the previous move
        if raised_by[1] == i:
            raised_by[0] = False
        
        # Determine the round state based on the current state, round number, and raise status
        round_state = int(state in (0, 3) and round_no != 1 and not raised_by[0])
        
        # Initialize variables for predicting the move of AI players
        new_state = 3
        
        # AI players make predictions for their moves
        if i != 0:
            j = (i - 1) + i % 3
            displayed_pile = [i for i in display_pile if type(i) is tuple]
            n = 3 - len(folded)
            no_fold = i == 2
            new_state, amount = PREDICT.get_move(realhands[i], displayed_pile, round_state, min_bet, balances[i], round_no * (j**2) / 11, n, no_fold)
        
        # Handle the case where the AI player folds
        if new_state == 0:
            folded.append(i)
            msg += f"\n{players[i]} folded\n"
            display_hands[i] = (-2, -2)
            continue
        
        # Update the state for AI players
        if i != 0:
            state = new_state
        
        # Handle betting or checking based on the determined state
        if state in (1, 2):
            # Check if the player has enough balance to meet the minimum bet
            if balances[i] < min_bet:
                msg = f"Minimum bet is\n{min_bet}"
                imagelabel("BLACK_BG.PNG", Text=msg, Size=(370, 210), Rx=.85, Ry=.76)
                game(round_no, state=3)
                return
            
            # Handle raising scenario
            if state == 2:
                raised_by[0] = True
                raised_by[1] = i
                if i!=0: min_bet = amount
            
            # Update the message with the player's bet
            msg += f"\n{players[i]} bet {min_bet}$\n"
            
            # Update bets and balances accordingly
            bets[i] += min_bet
            balances[i] -= min_bet
            
        elif state == 3:
            # Update the message for players who checked
            msg += f"\n{players[i]} checked\n"

    # Update the display_pile based on the realpile for the current round
    display_pile = realpile[:round_no + 2] + [None] * (3 - round_no)

    # Call the play() function to continue the game
    play(round_no)

    # Display the message for the current round
    imagelabel("BLACK_BG.PNG", Text=msg, Size=(370, 210), Rx=.85, Ry=.76, Font=("kongtext", 15))

    # Check if it's the last round or if all other players have folded to initiate showdown
    if round_no == 4 or len(folded) == 3:
        showdown()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

start()

win.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
