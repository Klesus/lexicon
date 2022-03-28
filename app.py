import datetime
import functools
import math
from operator import indexOf
import random

def ask_for_type(request: str, explanation: str, tajp):
    """
    Requests user for input and returns a value of given type.
    Keeps re-requesting until user gives acceptable input.

    Parameters:
        request (str): A string given when asking for input the first time
        explanation (str): A string given each time input type wasn't acceptable
        tajp (type): The supposed type requested to the user

    Returns:
        Value of type tajp
    """

    value = None
    while type(value) != tajp:
        try:
            value = tajp(input(request))
        except ValueError:
            print(explanation)
    return value

def say_words(words="Hello World"):
    print(words)

def mention_person():
    fname, ename, age = None, None, None

    print("Uppge en persons förnamn, efternamn och ålder")
    # askfortype() finns men är onödig på strängar
    fname = input("Förnamn: ")
    ename = input("Efternamn: ")
    
    age = ask_for_type("Ålder: ", "Ålder måste vara en positiv siffra.", float)

    print(f"Denna personen heter {fname} {ename} och är {age} år gammal")

def console_color():
    red = "\033[38;2;255;0;0m"
    green = "\033[38;2;0;255;0m"
    blue = "\033[38;2;0;0;255m"
    cyan = "\033[38;2;0;255;255m"
    pink = "\033[38;2;255;128;255m"
    reset = "\033[0m"
    
    print("Välj en färg:")
    print(red + "1) Röd")
    print(green + "2) Grön")
    print(blue + "3) Blå")
    print(cyan + "4) Cyan")
    print(pink + "5) Rosa" + reset)

    choice = input("Välj färg: ")

    match choice:
        case ("1"|"Röd"|"röd"):
            print(red)
        case ("2"|"Grön"|"grön"):
            print(green)    
        case ("3"|"Blå"|"blå"):
            print(blue)
        case ("4"|"Cyan"|"cyan"):
            print(cyan)
        case ("5"|"Rosa"|"rosa"):
            print(pink)
        case _:
            print("Det alternativet finns inte")

def today():
    print(f"Idag är det {datetime.date.today()}")

def biggest():
    """
    Prints the biggest of two number inputs
    """
    print("Ange två tal:")
    a = ask_for_type("A: ", "Talet måste vara en siffra", float)
    b = ask_for_type("B: ", "Talet måste vara en siffra", float)
    
    tmp = max(a, b)
    ans = "A" if tmp == a else "B"
    if a == b:
        ans = "A och B är lika stora"
        print(ans)
    else:
        print(f"{ans} är störst")

def number_guess():
    print("Nu spelar vi en gissningslek")
    print("Hitta det magiska talet mellan 1 - 100")
    goal = random.randint(1, 100)
    guess = None
    n = 0
    while goal != guess:
        n += 1
        
        try:
            guess = int(input(f"Gissning {n}: "))
            
            # refactor ask_for_type to accept optional checks
            if guess > goal:
                print("Din gissning var större än det magiska talet")
            elif guess < goal:
                print("Din gissning var mindre än det magiska talet")

        except ValueError:
            print("Din gissning måste vara ett heltal")
            n -= 1 # räkna inte felinmatningar som försök
    
    print("Du hittade det magiska talet!")
    print(f"Det tog dig {n} gissningar")

def save_text():
    text = input("Skriv en text du vill spara: ")
    with open("text.txt", "w") as f:
        f.write(text)
    print("Din text är sparad i text.txt")

def load_text():
    try:
        with open("text.txt", "r") as f:
            txt = f.read()
            print("Texten i text.txt lyder som följer:")
            print(txt)
    except FileNotFoundError:
        print("Det finns ingen data sparad")

def decimal():
    n = None
    while type(n) != float:
        try:
            n = float(input("Ange ett decimaltal: "))
            if n == int(n):
                raise ValueError # talet har inga decimaler
        except ValueError:
            print("Du måste ange ett tal som har decimaler")
            n = None
    
    if n < 0:
        print("Roten ur ditt tal är påhittat")
    else:
        print(f"Roten ur ditt tal: {math.sqrt(n)}")
    print(f"Ditt tal upphöjt i 2: {n**2}")
    print(f"Ditt tal upphöjt i 10: {n**10}")

def multiplication():
    nums = list(range(1, 11))
    d = {x:[y*x for y in nums] for x in nums}
    # samma som:
    # d = {1: [x for x in nums],
    #      2: [x*2 for x in nums],
    #      3: [x*3 for x in nums],
    #      4: [x*4 for x in nums],
    #      5: [x*5 for x in nums],
    #      6: [x*6 for x in nums],
    #      7: [x*7 for x in nums],
    #      8: [x*8 for x in nums],
    #      9: [x*9 for x in nums],
    #      10: [x*10 for x in nums]}
    
    print("Multiplikationstabellen upp till 10")
    print(f"{'':<5} {1:<3} {2:<3} {3:<3} {4:<3} {5:<3} {6:<3} {7:<3} {8:<3} {9:<3} {10:<3}") # Header
    print(f"{'':->45}")
    for k, v in d.items():
        ones, twos, threes, fours, fives, sixes, sevens, eights, nines, tens = v
        print(f"{k:>3} | {ones:<3} {twos:<3} {threes:<3} {fours:<3} {fives:<3} {sixes:<3} {sevens:<3} {eights:<3} {nines:<3} {tens:<3}")

def my_sort(unsorted):
    sortedArray = []
    while unsorted:
        i = indexOf(unsorted, min(unsorted))
        sortedArray.append(unsorted.pop(i))

    return sortedArray

def arrays(lst_size=10, rnd_range=100):
    unsorted = random.sample(range(1,rnd_range), lst_size)
    print(f"Här är en osorterad lista: {unsorted}")
    sortedArray = my_sort(unsorted)
    print(f"Här är listan sorterad:    {sortedArray}")

def palindrom():
    print("Här kan du kolla om ett ord är ett palindrom (ordet är detsamma bakvänt)")
    ord = input("Ditt ord: ")
    if ord.upper() == ord[::-1].upper():
        print("Ja, ordet är ett palindrom")
    else:
        print("Nej, ordet är inte ett palindrom")
    print(f"{ord} spegelvänt blir {ord[::-1]}")

def given_range():
    """
    Givet ett första och andra heltal, skrivs alla tal däremellan ut utan att inkludera första eller andra talet.
    """
    print("Här kan du ange två heltal och få listat alla heltal däremellan")
    start = ask_for_type("Första talet: ", "Talet måste vara ett heltal", int)
    end = ask_for_type("Andra talet: ", "Talet måste vara ett heltal", int)

    print(f"Talen mellan {start} och {end} lyder som följer...")
    if start >= end:
        print(list(range(start-1, end, -1))) # skriv i sjunkande ordning om första talet är större (eller lika med) det andra
    else:
        print(list(range(start+1, end)))

def odd_even():
    unsorted_evens = []
    unsorted_odds = []
    while not unsorted_evens and not unsorted_odds: # or kräver både udda och jämna tal, and gör det inte
        values = input("Ange ett antal heltal separerade med kommatecken: ")
        separated = values.split(",")
        for val in separated:
            try:
                val = int(val)
                if val % 2:
                    unsorted_odds.append(val)
                else:
                    unsorted_evens.append(val)
            except ValueError:
                print("Serien måste innehålla heltal separerade med kommatecken (,)")
                unsorted_evens = []
                unsorted_odds = []
                break
    
    evens = my_sort(unsorted_evens)
    odds = my_sort(unsorted_odds)
    print("Udda tal i listan:")
    print(odds)
    print("Jämna tal i listan")
    print(evens)

def sum_list():
    lst = []
    while not lst:
        values = input("Ange ett antal heltal separerade med kommatecken: ")
        separated = values.split(",")
        for val in separated:
            try:
                lst.append(int(val))
            except ValueError:
                print("Serien måste innehålla heltal separerade med kommatecken (,)")
                lst = []
                break
    
    print(functools.reduce((lambda x, y: x + y), lst)) # reduce finns i många andra språk så jag använder det här

class Character:
    def __init__(self, name, hp, str):
        self.name = name
        self.hp = random.randint(int(hp*2/3), hp) # enkel formel för att sätta min hp
        self.str = random.randint(int(str/2), str)

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.lck = random.randint(1, 10) # Borde inte bara spelaren ha egenskapen tur?
    
    def __repr__(self):
        return f"Player({self.name}, {self.hp}, {self.str}, {self.lck})"

    def __str__(self):
        return f"Typ: Spelare\nNamn: {self.name}\nHälsa: {self.hp}\nStyrka: {self.str}\nTur: {self.lck}"

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, 500, 30)
    
    def __repr__(self):
        return f"Enemy({self.name}, {self.hp}, {self.str})"

    def __str__(self):
        return f"Typ: Fiende\nNamn: {self.name}\nHälsa: {self.hp}\nStyrka: {self.str}"

player, enemy = None, None

def create_charachters():
    global player, enemy

    if player:
        print("Dessa karaktärer finns redan...")
        print(player)
        print("")
        print(enemy)
        print("")
        print('Vill du ändra dessa karaktärer? Svara då med "ok/ja", i annat fall sparas de')
        tmp = input('Ändra?: ')
        if not (tmp.lower() == "ok" or tmp.lower() == "ja"):
            return

    print("Skapa några spelkaraktärer")
    player = Player(input("Vad ska din karaktär heta?: "))
    enemy = Enemy(input("Vad heter din fiende?: "))
    print(player)
    print("")
    print(enemy)

first_run = True
def main():
    global first_run

    today()
    choice = None
    while True:
        
        if not first_run:
            input("Tryck Enter för att fortsätta...")
        else:
            first_run = False

        print("""
Välj ett av följande alternativ:
1) Skriv "Hello World"
2) Namnge en person
3) Byt färg på texten
4) Dagens datum
5) Störst av två
6) Magiskt nummerspel
7) Spara text
8) Ladda text
9) Nummerinfo
10) Multiplikationstabellen
11) Slumpad lista -> sorterad lista
12) Palindromcheck
13) Nummer emellan
14) Jämna/udda listor
15) Addera listan
16) Spelkaraktärer
Skriv q/Q för att avsluta
        """)

        choice = input("Välj program (med siffra): ")
        if choice.lower() == "q":
            print("\33[0m")
            break

        try:
            choice = int(choice)
            
            match choice:
                case 1:
                    say_words()
                case 2:
                    mention_person()
                case 3:
                    console_color()
                case 4:
                    today()
                case 5:
                    biggest()
                case 6:
                    number_guess()
                case 7:
                    save_text()
                case 8:
                    load_text()
                case 9:
                    decimal()
                case 10:
                    multiplication()
                case 11:
                    arrays()
                case 12:
                    palindrom()
                case 13:
                    given_range()
                case 14:
                    odd_even()
                case 15:
                    sum_list()
                case 16:
                    create_charachters()
                case _:
                    print("Det alternativet finns inte")
        except ValueError:
            print(f"{choice} är inget giltigt alternativ")

if __name__ == "__main__":
    main()