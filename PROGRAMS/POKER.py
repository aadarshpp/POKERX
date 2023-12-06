# Importing in-build/installed modules
import customtkinter as ctk
from PIL import Image

# Importing user defined modules
import COMPUTE
import PREDICT

# creating a ctk window
win = ctk.CTk(fg_color="black")
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.title("Poker")
win.geometry(f"{w}x{h}+0+0")
win.overrideredirect(True) 

# convinience funtions
def path(imagename): return f"C:\code\Python\POKER\IMAGES\{imagename}"
def cardpath(c): 
    if c is None: return None
    if c==-1: return r"CARDS\BACK.png"
    if c==-2: return r"CARDS\FOLDED.png"
    return f"CARDS\{c[1]} of {c[0]}.png"

# display a new background image
def bgimage(imagename, Size=(w, h)):
    bg_image = ctk.CTkImage(light_image=Image.open(path(imagename)), size=Size)
    label =  ctk.CTkLabel(win, image=bg_image, text="", bg_color="black")
    label.place(x=0, y=0, relwidth=1, relheight=1)
    return label

# place an image button at a given position
def imagebutton(Imagename, Size, Rx=.5, Ry=.5, Command=None,fg_c="black",  hover_c="white"):
    img = ctk.CTkImage(Image.open(path(Imagename)), size=Size)
    button = ctk.CTkButton(win, text="", image=img,fg_color=fg_c, bg_color=fg_c, hover_color=hover_c, command=Command, corner_radius=0)
    button.place(relx=Rx, rely=Ry, anchor="center")

# place a label having an image and text(optional) at a given position
def imagelabel(Imagename, Size, Text="", Font=("kongtext", 20), Rx=.5, Ry=.5, fg_c="black", Anchor="center"):
    if Imagename is None: return
    image = ctk.CTkImage(light_image=Image.open(path(Imagename)), size=Size)
    label =  ctk.CTkLabel(win, image=image, text=Text, font=Font, fg_color=fg_c, corner_radius=0, anchor=Anchor)
    label.place(relx=Rx, rely=Ry, anchor=Anchor)
    return label

# place a button with given text at a given position
def textbutton(Text, Command, Font=("kongtext", 30), fg_c="black", hover_c="white", text_c="grey", width=40, height=40, Rx=.5, Ry=.5, Anchor="center"):
    button = ctk.CTkButton(win, width, height, text=Text, font=Font,
                           text_color=text_c, fg_color=fg_c, hover_color=hover_c,
                           corner_radius=0, command=Command)
    button.place(relx=Rx, rely=Ry, anchor=Anchor)
    return button

def back_button(prev, font=("kongtext", 30)): return textbutton("<", prev, Font=font, Rx=0, Ry=0, Anchor="nw")
def next_button(next): textbutton(">", Command=next, Rx=1, Ry=0, Anchor="ne")
def full_back_button(): textbutton("<<", Command=home, Rx=1, Ry=0, Anchor="ne")

# places a label with given text at a given position
def textlabel( Text="", wd=0, ht=28, Font=("kongtext", 20), Rx=.5, Ry=.5, fg_c="black", Anchor="center"):
    label =  ctk.CTkLabel(win, text=Text,width=wd, height=ht, font=Font, fg_color=fg_c, corner_radius=0, anchor=Anchor)
    label.place(relx=Rx, rely=Ry, anchor=Anchor)
    return label

# creates a page with background with back and next/fullback buttons
def page(bg, prev, next=None, full_back=False):
    bgimage(bg)
    back_button(prev)
    if next is not None: next_button(next)
    if full_back : full_back_button()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def start():
    l = imagelabel("START.PNG", Size=(w, h), Rx=.5, Ry=.5)
    l.after(4000, home)

def home():
    bgimage("HOME_SCREEN.PNG")
    
    imagebutton("PLAY.PNG", (300, 100), Rx=.6, Ry=.16, Command=lambda: loading(0))
    imagebutton("LEARN.PNG", (300, 100), Rx=.6, Ry=.38, Command=learn)
    imagebutton("CHEAT.PNG", (300, 100), Rx=.6, Ry=.60, Command=lambda: loading(1))
    imagebutton("EXIT.PNG", (300, 100), Rx=.6, Ry=.82, Command=win.quit, hover_c="red")

def loading(n):
    loading_screens = ("LOADING_C.PNG", "LOADING_J.PNG")
    l = bgimage(loading_screens[n])
    if n==0: l.after(2000, lambda: game(0))
    if n==1: l.after(2000, cheat)
    
def learn():
    def how_to(): 
        page("HOW_TO.PNG", prev=home, next=hands_rank_1)
    def hands_rank_1(): page("HANDS_RANK_1.PNG", prev=how_to, next=hands_rank_2)
    def hands_rank_2(): page("HANDS_RANK_2.PNG", prev=hands_rank_1, next=hands_rank_3)
    def hands_rank_3(): page("HANDS_RANK_3.PNG", prev=hands_rank_2, next=bettings)
    def bettings(): page("BETTINGS.PNG", prev=hands_rank_3, next=round_types_1)
    def round_types_1(): page("ROUND_TYPES_1.PNG", prev=bettings, next=round_types_2)
    def round_types_2(): page("ROUND_TYPES_2.PNG", prev=round_types_1, full_back=True)
        
    how_to()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#    

# actiavated = [1v1 odds, tot odds, show rank, show community cards]
activated = [False] * 4

def cheat():
    bgimage("CHEAT_BLACK.png")
    
    # places buttons with given foreground and text colours
    def buttons(cfg, ctc, qfg, qtc):
        back_button(home, font=("kongtext", 42))
        textbutton("c", cheat_main, ("kongtext", 42), fg_c=cfg, text_c=ctc, Rx=0, Ry=0.1, Anchor="nw")
        textbutton("?", cheat_about, ("kongtext", 42), fg_c=qfg, text_c=qtc, Rx=0, Ry=0.2, Anchor="nw")
    
    def cheat_about():
        bgimage("CHEAT_ABOUT.png")
        buttons("black", "grey", "blue", "white")
    
    def cheat_main():
        bgimage("CHEAT_MAIN.png")
        buttons("blue", "white", "black", "grey")
        
        for i in range(len(activated)): 
            on(i) if activated[i] else off(i)
            
        textbutton(" OFF ", Font=("kongtext", 40), Command=err, Rx=.7, Ry=4*.195+.102, fg_c="black", text_c="red", width=50, height=30)
               
    def on(n):
        textbutton(" ON ", Font=("kongtext", 40), Command=lambda:off(n), Rx=.7, Ry= n*.197+.102, fg_c="black", text_c="green")
        activated[n] = True
        
    def off(n):
        textbutton(" OFF ", Font=("kongtext", 40), Command=lambda:on(n), Rx=.7, Ry=n*.197+.102, fg_c="black", text_c="red", width=50, height=30)
        activated[n]=False
    
    def err():
        errlabel = bgimage("ERR_G.png")
        errlabel.after(7000, start)
    
    cheat_main()

# displays information according to cheats activated
def cheat_box(hand):
    global display_pile
    if True not in activated: return 
    displayed_cards = [i for i in display_pile if type(i) is tuple]
    
    msg = ""
    
    if activated[0]:
        p1v1 = PREDICT.probability_1v1(hand, displayed_cards)
        ptot = PREDICT.probability_1vn(hand, displayed_cards, 3-len(folded))
        wp, tp, lp = map(lambda x:str(int(100*x)).ljust(3), p1v1)
        lp = str(100-int(wp)-int(tp)).ljust(3)
        msg += f"\n 1V1  : W {wp} T {tp} L {lp}\n"
        
    if activated[1]:
        ptot = PREDICT.probability_1vn(hand, displayed_cards, 3-len(folded))
        wp, tp, lp = map(lambda x:str(int(100*x)).ljust(3), ptot)
        lp = str(100-int(wp)-int(tp)).ljust(3)
        msg += f"\n TOT  : W {wp} T {tp} L {lp}\n"
        
    if activated[2]:
        r, p = COMPUTE.rank_of_best_hand(hand+displayed_cards)
        msg = f"\nRANK : {poker_hands[r-1]}\n" + msg
        
    if activated[3]:
        msg = "\nSHOW CC : ACTIVATED\n" + msg
    
    imagelabel("BLACK_BG.png", Size=(370, 210), Text=msg, Font=('kongtext', 14), Rx=.85, Ry=.15)
        
# displays slider to raise the bet and excecutes it if confirmed
def raise_bet(round_no, balances):
    global min_bet
    mn, mx = min_bet, balances[0]
    
    if mn>mx:
        msg = f"Minimum bet is\n{min_bet}"
        imagelabel("BLACK_BG.PNG", Text=msg,Size=(370, 210), Rx=.85, Ry=.76)
        return
        
    amount_label = ctk.CTkLabel(win, corner_radius=0, text=str(min_bet))
    amount_label.place(relx=.87, rely=.67)
    imagelabel("BLACK_BOX.PNG",Size=(370, 210), Rx=.85, Ry=.76)
    def textlabel(Text):
        nonlocal amount_label
        amount_label.destroy()
        amount_label = ctk.CTkLabel(win, corner_radius=0, text=Text, font=("Kongtext", 20), fg_color="transparent")
        amount_label.place(relx=.87, rely=.67)
        return amount_label
    
    val = mn
    def slider_event(value):
        nonlocal val 
        textlabel(int(value/100)*100)
        if int(value)==mx: val = mx
        else: val = int(value/100)*100
        
    slider = ctk.CTkSlider(master=win, from_=mn, to=mx, orientation="vertical", command=slider_event)
    slider.place(relx=0.8, rely=0.76, anchor="center")
    slider.set(mn)
    
    def confirm():
        global min_bet
        min_bet = val
        slider.destroy()
        tbutton.destroy()
        amount_label.destroy()
        
        game(round_no+1, state=2)
        
    tbutton = textbutton("CONFIRM", Font=("kongtext", 20), Command=confirm, Rx=.9, Ry=.82)


# convinience function that returns the text to be displayed at the end of a game
def endroundmsg(w, r, p, perwin):
    msg = ""
    fontsize = 20
    
    if w == [0]:
         msg += f"You won\n\nYou got {perwin} $"
         
    else:
        ws = ""
        for i in w: ws += players[i]+",\n"
        fontsize = 20 * (len(w)+4)/5
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

# diplays the game screen for the given round
def play(round_no, first=False, showdown=False):
    global realhands, realpile, display_pile, display_hands, bets, balances, raised_by
    
    if first:
        bgimage("PLAY_BG.PNG")
        imagelabel("TABLE.png", (600, 230), Ry=.47)
        
    if activated[-1]: display_pile = realpile
    cheat_box(realhands[0])
    
    t = 0.072
    for i in range(5):
        a = .356 + t*i
        if display_pile[i] is not None:
            imagelabel(cardpath(display_pile[i]), Size=(250*.4, 363*.4), fg_c="#005E38", Rx=a, Ry=.47)
    
    def game_call(state):
        global raised_by
        if raised_by[1]==0: raised_by[0] = False
        if bets[0]+balances[0]<100 and round_no < 3:
            exitlabel = ctk.CTkLabel(win, w, h, corner_radius=0, text="YOU ARE OUT OF MONEY\n\n...", font=("kongtext", 40), text_color="#870101")
            exitlabel.place(relx=.5, rely=.5, anchor="center")
            exitlabel.after(1000, home)
            return
        if sum(bets[1:])+sum(balances[1:])==0:
            exitlabel = ctk.CTkLabel(win, w, h, corner_radius=0, text=f"YOU WON THE GAME\n\nWON {balances[0]}$", font=("kongtext", 40), text_color="white")
            exitlabel.place(relx=.5, rely=.5, anchor="center")
            exitlabel.after(1000, home)
            return
        if showdown:
            if state==0: game(0, new=False)
            return
        if state==2:
            raise_bet(round_no, balances)
        else:
            game(round_no+1, state)
    
    if player_folded:
        imagebutton("BLACK.png", (1100, 60), fg_c="black", hover_c="white", Rx=.5, Ry=.94, Command=lambda: game_call(0))
        imagebutton("NEXT.png", (180, 45), fg_c="black", hover_c="black", Rx=.5, Ry=.94, Command=lambda: game_call(0))
    else:
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
    Y = (.79,.46, .14, .46)
    for i in range(4):
        if display_hands[i] is None: continue
        if i!=0: textlabel(players[i], wd=250*.85, Rx=X[i], Ry=Y[i]-363*.27/864)
        imagelabel(cardpath(display_hands[i][0]),  Size=(250*.4, 363*.4), fg_c="#193528", Rx=X[i]-t/2, Ry=Y[i])
        imagelabel(cardpath(display_hands[i][1]),  Size=(250*.4, 363*.4), fg_c="#193528", Rx=X[i]+t/2, Ry=Y[i])
        
    def numstr(n): 
        ns = str(n).center(5)
        if n>=100000:
            ns = f"{round(n/100000, 2)} L"
        return f"  {ns}"
    d = .105
    
    X2 = (.448,  .098, .448, .798)
    Y2 = (.66,.59, .27, .59)
    for i in range(4):
        if bets[i] is not None:
            imagelabel("BET_BOX.PNG", (190*.8, 55*.8), Text=numstr(bets[i]), Rx=X2[i], Ry=Y2[i])
        if balances[i] is not None:
            imagelabel("BALANCE_BOX.PNG", (190*.8, 55*.8), Text=numstr(balances[i]), Rx=X2[i]+d, Ry=Y2[i])
    
    def leave():
        tlabel = ctk.CTkLabel(win, w, h, corner_radius=0, text=f"YOU LEFT WITH\n\n{balances[0]}$", font=("kongtext", 40))
        tlabel.place(relx=0.5, rely=0.5, anchor="center")
        tlabel.after(1000, home)
        
    textbutton("LEAVE", Rx=0, Ry=0, Anchor="nw", Command=leave)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# executes player and opponent moves and calls play() accordingly
def game(round_no, state=1, new=True):
    global realhands, realpile, display_pile, display_hands, bets, balances, min_bet, folded, player_folded, raised_by
    
    if round_no==0:
        deck = [(s, n) for s in 'SCDH' for n in range(2, 15)]
        folded = []
        realhands = [COMPUTE.get_random_from(2, deck) for _ in range(4)]
        realpile = COMPUTE.get_random_from(5, deck)
        display_pile = [-1]*5
        display_hands = [realhands[0]] + [(-1,-1)]*3
        bets = [0]*4
        if balances is None or new : balances = [10000]*4
        player_folded = False
        play(round_no, first=True)
        return 
    
    def showdown():
        global min_bet, bets
        considered_cards = [hand + realpile for hand in realhands]
        w, r, p = COMPUTE.compare_hands(considered_cards, folded)
        perwin = int(sum(bets)/len(w))
        for i in w: balances[i] += perwin
        
        msg, fontsize = endroundmsg(w, r, p, perwin)
        play(round_no = 5, showdown=True)
        bets = (0,)*4
        
        def display():
            imagelabel("BLACK_BG.PNG", Text=msg, Font=("kongtext", fontsize), Size=(370, 210), Rx=.85, Ry=.76)
            if not player_folded:
                imagebutton("BLACK.png", (1100, 60), fg_c="black", hover_c="grey", Rx=.5, Ry=.94, Command=lambda: game(0, new=False))
                imagebutton("NEXT.png", (180, 45), fg_c="black", hover_c="black", Rx=.5, Ry=.94, Command=lambda: game(0, new=False))
            
        l = textlabel(Rx=1, Ry=0)
        sleep = 1500
        l.after(sleep, display)
        min_bet = 100
        
    msg = ""
    display_hands = [realhands[0]] + [(None, None)] * 3
    
    # ROUND STATES    -->   {0: F_BET/CALL_R, 1: F_CHECK_R}
    # STATES (MOVES)  -->   {0: FOLD, 1: CALL, 2: RAISE, 3: CHECK}
    
    if state == 0:
        player_folded = True
        folded.append(0)
        
    for i in range(4):
        
        if i in folded: continue
        if raised_by[1] == i: raised_by[0] = False
        
        round_state = int(state in (0, 3) and round_no != 1 and not raised_by[0])
        new_state  = 3
        
        if i != 0:
            j = (i-1) + i%3
            displayed_pile =  [i for i in display_pile if type(i) is tuple]            
            n = 3-len(folded)
            no_fold = i==2
            new_state, amount  = PREDICT.get_move(realhands[i], displayed_pile, round_state, min_bet, balances[i], round_no*(j**2)/11, n, no_fold)
            
        if new_state == 0:
            folded.append(i)
            msg += f"\n{players[i]} folded\n"
            display_hands[i] = (-2, -2)
            continue
        
        if i!=0: 
            state = new_state
        
        if state in (1,2):
            
            if balances[i]<min_bet:
                msg = f"Minimum bet is\n{min_bet}"
                imagelabel("BLACK_BG.PNG", Text=msg,Size=(370, 210), Rx=.85, Ry=.76)
                game(round_no, state=3)
                return
            
            if state == 2:
                raised_by[0] = True
                raised_by[1] = i
                
            if i != 0: min_bet = amount
            
            msg += f"\n{players[i]} bet {min_bet}$\n"
            bets[i] += min_bet
            balances[i] -= min_bet
            
        elif state == 3 :
            msg += f"\n{players[i]} checked\n"
    
    display_pile = realpile[:round_no+2] + [None]*(3-round_no)
            
    play(round_no)
    imagelabel("BLACK_BG.PNG", Text=msg,Size=(370, 210), Rx=.85, Ry=.76, Font=("kongtext", 15))
    
    if round_no==4 or len(folded)==3:
        showdown()
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

start()

win.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#