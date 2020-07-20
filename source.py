from tkinter import Tk
from tkinter import E
from tkinter import ttk
from tkinter import StringVar

OPERATORS = ['*', '/', '-', '+']
SPECIAL = ['C', 'AC', 'P/M']
BODMAS = ['/', '*', '+', '-']
STORAGE = [None]
CACHE = None

root = Tk()
root.title("PyCalc")
root.resizable(False, False)

DISPLAY = StringVar()
DISPLAY.set(' ')

def cout(char):
    ''' Responisble for displaying result and inputing in STORAGE '''
    global DISPLAY
    global STORAGE
    global OPERATORS
    global CACHE

    if char in OPERATORS:
        if STORAGE[-1] == None:
            if char in OPERATORS[:2]:
                ''' Case when first input is '/' or '*' '''
                STORAGE += ['1']+list(char)
            else:
                ''' Case when first input is '+' or '-' '''
                STORAGE += ['0']+list(char)
        elif STORAGE[-1] in OPERATORS:
            ''' Switching to latest operator, example: '3+-' evalutes to '3-' '''
            STORAGE[-1] = char
        else:
            STORAGE += list(char)
    else:
        if char in SPECIAL:
            ''' Check if input is for 'Clear' or 'Plus/Minus' or 'All Clear' '''
            if char == 'C':
                STORAGE = STORAGE[:-1]
            if char == 'P/M':
                if STORAGE[-1] not in OPERATORS:
                    if float(STORAGE[-1]) >= 0.0:
                        ''' If number is positive change to negative '''
                        STORAGE[-1] = str(-float(STORAGE[-1]))
                    else:
                        ''' If numner is negative change to positive '''
                        STORAGE[-1] = str(abs(float(STORAGE[-1])))
            else:
                STORAGE = [None]
        else:
            if STORAGE[-1] == None:
                ''' First element input case '''
                STORAGE.append(char)
            else:
                ''' Subsequent input case '''
                if STORAGE[-1] in OPERATORS:
                    ''' Subsequent operator input case '''
                    STORAGE += list(char)
                else:
                    ''' Subsequent appending of continuing digits '''
                    STORAGE[-1] += char
    print('STORAGE:', STORAGE)
    TO_BE_DISPLAYED = ''
    for i in STORAGE[1:]:
        ''' Excluding first element 'None' '''
        if i in OPERATORS:
            ''' Spacing around OPERATORS '''
            TO_BE_DISPLAYED += (' '+i+' ')
        else:
            TO_BE_DISPLAYED += i

    DISPLAY.set(TO_BE_DISPLAYED)

def partial_calculate(OPERATOR_POS, PARTIAL_LEFT, PARIAL_RIGHT):
    ''' Evalutes expression one block at a time '''
    global LEFT, RIGHT

    LEFT = float(STORAGE[PARTIAL_LEFT])
    OPERATOR = STORAGE[OPERATOR_POS]
    RIGHT = float(STORAGE[PARIAL_RIGHT])
    
    if OPERATOR == '/':
        return LEFT/RIGHT
    elif OPERATOR == '*':
        return LEFT*RIGHT
    elif OPERATOR == '+':
        return LEFT+RIGHT
    else:
        return LEFT-RIGHT

def calculate():
    ''' Redirects expression to partial_calculate one block at a time '''
    global STORAGE
    global DISPLAY
    global BODMAS
    
    for i in BODMAS:
        if i in STORAGE:
            ITTER = STORAGE.count(i)
            for j in range(ITTER):
                OPERATOR_POS = STORAGE.index(i)
                PARTIAL_LEFT = OPERATOR_POS - 1
                PARTIAL_RIGHT = OPERATOR_POS + 1
                SUB_RESULT = partial_calculate(OPERATOR_POS, PARTIAL_LEFT, PARTIAL_RIGHT)
                STORAGE[OPERATOR_POS] = str(SUB_RESULT); STORAGE.pop(PARTIAL_LEFT); STORAGE.pop(PARTIAL_RIGHT-1)
    DISPLAY.set('Ans: '+STORAGE[1])

content = ttk.Frame(master=root, padding=(3, 3, 3, 3))
mainframe = ttk.Frame(content, relief = 'sunken')

# result display
display = ttk.Frame(mainframe, relief='sunken').grid(row=0, column=0, columnspan=4)

val_display = ttk.Label(display, textvariable=DISPLAY).grid(row=0, column=0, columnspan=4, sticky=E)

# operations
keypad = ttk.Frame(mainframe).grid()

mul = ttk.Button(keypad, text='*', command=lambda: cout('*')).grid(row=1, column=0)
div = ttk.Button(keypad, text='/', command=lambda: cout('/')).grid(row=1, column=1)
clear = ttk.Button(keypad, text='C', command=lambda: cout('C')).grid(row=1, column=2)
allClear = ttk.Button(keypad, text='AC', command=lambda: cout('AC')).grid(row=1, column=3)
sub = ttk.Button(keypad, text='-', command=lambda: cout('-')).grid(row=2, column=3)
add = ttk.Button(keypad, text='+', command=lambda: cout('+')).grid(row=3, column=3)
equal = ttk.Button(keypad, text='=', command=calculate).grid(row=4, column=3)

# keypad values
nine = ttk.Button(keypad, text='9', command=lambda: cout('9')).grid(row=2, column=0)
eight = ttk.Button(keypad, text='8', command=lambda: cout('8')).grid(row=2, column=1)
seven = ttk.Button(keypad, text='7', command=lambda: cout('7')).grid(row=2, column=2)
six = ttk.Button(keypad, text='6', command=lambda: cout('6')).grid(row=3, column=0)
five = ttk.Button(keypad, text='5', command=lambda: cout('5')).grid(row=3, column=1)
four = ttk.Button(keypad, text='4', command=lambda: cout('4')).grid(row=3, column=2)
three = ttk.Button(keypad, text='3', command=lambda: cout('3')).grid(row=4, column=0)
two = ttk.Button(keypad, text='2', command=lambda: cout('2')).grid(row=4, column=1)
one = ttk.Button(keypad, text='1', command=lambda: cout('1')).grid(row=4, column=2)
dot = ttk.Button(keypad, text='.', command=lambda: cout('.')).grid(row=5, column=0)
zero = ttk.Button(keypad, text='0', command=lambda: cout('0')).grid(row=5, column=1)
plusminus = ttk.Button(keypad, text='+/-', command=lambda: cout('P/M')).grid(row=5, column=2)
copy = ttk.Button(keypad, text='Copy', command=lambda: cout('Copy')).grid(row=5, column=3)

# num-pad key bindings
root.bind("*", lambda e: cout('*'))
root.bind("/", lambda e: cout('/'))
root.bind("C", lambda e: cout('C'))
root.bind("c", lambda e: cout('C'))
root.bind("Q", lambda e: cout('AC'))
root.bind("q", lambda e: cout('AC'))
root.bind("-", lambda e: cout('-'))
root.bind("+", lambda e: cout('+'))
root.bind("=", lambda e: calculate())
root.bind("<Return>", calculate)

root.bind("9", lambda e: cout('9'))
root.bind("8", lambda e: cout('8'))
root.bind("7", lambda e: cout('7'))
root.bind("6", lambda e: cout('6'))
root.bind("5", lambda e: cout('5'))
root.bind("4", lambda e: cout('4'))
root.bind("3", lambda e: cout('3'))
root.bind("2", lambda e: cout('2'))
root.bind("1", lambda e: cout('1'))
root.bind(".", lambda e: cout('.'))
root.bind("0", lambda e: cout('0'))

root.mainloop()