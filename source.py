from tkinter import Tk
from tkinter import N, S, E, W
from tkinter import ttk
from tkinter import StringVar

OPERATORS = ['*', '/', '-', '+']
SPECIAL = ['C', 'AC']
BODMAS = ['/', '*', '+', '-']
LEFT, RIGHT = 1, 1
CALCULATOR = {'/':LEFT/RIGHT,
              '*':LEFT*RIGHT,
              '+':LEFT+RIGHT,
              '-':LEFT-RIGHT}

def isonlydecimal(char):
    for i in char:
        if i.isdigit() or i == '.':
            continue
        else:
            return False
    return True

def isnotdecimal(char):
    return not isonlydecimal(char)

''' GUI '''
root = Tk()

DISPLAY = StringVar()
DISPLAY.set(' ')
STORAGE = ' '

def cout(char):
    global DISPLAY
    global STORAGE

    if char in OPERATORS and STORAGE[-1] in OPERATORS:
        ''' Switching to latest operator, example: '3+-' evalutes to '3-' '''
        STORAGE = STORAGE[:-1]+char
    else:
        if char in SPECIAL:
            ''' Check if input is for 'Clear' or 'All Clear' '''
            if char == 'C':
                STORAGE = STORAGE[:-1]
            else:
                STORAGE = ' '
        else:
            STORAGE += char

    TO_BE_DISPLAYED = ''
    for i in STORAGE:
        if i in OPERATORS:
            ''' Spacing around OPERATORS '''
            TO_BE_DISPLAYED += (' '+i+' ')
        else:
            TO_BE_DISPLAYED += i

    DISPLAY.set(TO_BE_DISPLAYED)

def partial_calculate(STORAGE, OPERATOR_POS, PARTIAL_LEFT, PARIAL_RIGHT):
    global LEFT, RIGHT
    global CALCULATOR
    print("STORAGE:", STORAGE)
    print('LEFT:', STORAGE[PARTIAL_LEFT : OPERATOR_POS])
    print('RIGHT:', STORAGE[OPERATOR_POS+1 : PARIAL_RIGHT+1])
    LEFT = float(STORAGE[PARTIAL_LEFT : OPERATOR_POS])
    RIGHT = float(STORAGE[OPERATOR_POS+1 : PARIAL_RIGHT+1])
    OPERATOR = STORAGE[OPERATOR_POS]
    
    return CALCULATOR.get(OPERATOR)
    

def calculate():
    global STORAGE
    global DISPLAY
    global BODMAS

    STORAGE = STORAGE.lstrip()
    
    if isonlydecimal(STORAGE):
        ''' Displaying final result '''
        DISPLAY.set('Ans: '+STORAGE)
    if STORAGE[0] in OPERATORS:
        ''' Trivial ambiguity, '-10+23' results to '0-10+23' '''
        STORAGE = '0'+STORAGE
        
    for i in BODMAS:
        if i in STORAGE:
            OPERATOR_POS = STORAGE.find(i)
            for i in range(OPERATOR_POS, 0, -1):
                if isnotdecimal(STORAGE[i]):
                    PARTIAL_LEFT = i+1
            for i in range(OPERATOR_POS, len(STORAGE)):
                if isnotdecimal(STORAGE[i]):
                    PARTIAL_RIGHT = i-1
    SUB_RESULT = partial_calculate(STORAGE, OPERATOR_POS, PARTIAL_LEFT, PARTIAL_RIGHT)
    STORAGE = STORAGE[:PARTIAL_LEFT] + SUB_RESULT + STORAGE[PARTIAL_RIGHT+1:]
    DISPLAY.set('Ans: '+STORAGE)
    calculate()

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
plusminus = ttk.Button(keypad, text='+/-', command=lambda: cout('pm')).grid(row=5, column=2)
copy = ttk.Button(keypad, text='Copy', command=lambda: cout('Copy')).grid(row=5, column=3)

root.mainloop()
