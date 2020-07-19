from tkinter import Tk
from tkinter import N, S, E, W
from tkinter import ttk
from tkinter import StringVar

OPERATORS = ['*', '/', '-', '+']
SPECIAL = ['C', 'AC']
BODMAS = ['/', '*', '+', '-']

def isonlydecimal(char):
    for i in char:
        if i.isdecimal() or i == '.':
            continue
        else:
            return False
    return True

def isnotdecimal(char):
    return False if isonlydecimal(char) else True

''' GUI '''
root = Tk()

DISPLAY = StringVar()
DISPLAY.set(' ')
STORAGE = [None]

def cout(char):
    ''' Responisble for displaying result and inputing in STORAGE '''
    global DISPLAY
    global STORAGE
    global OPERATORS

    if char in OPERATORS:
        if STORAGE[-1] == None:
            if char in OPERATORS[:2]:
                ''' Case when first input is '/' or '*' '''
                STORAGE.append('1')
                STORAGE += list(char)
            else:
                ''' Case when first input is '+' or '-' '''
                STORAGE.append('0')
                STORAGE += list(char)
        elif STORAGE[-1] in OPERATORS:
            ''' Switching to latest operator, example: '3+-' evalutes to '3-' '''
            STORAGE[-1] = char
        else:
            STORAGE += list(char)
    else:
        if char in SPECIAL:
            ''' Check if input is for 'Clear' or 'All Clear' '''
            if char == 'C':
                STORAGE = STORAGE[:-1]
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
    global CALCULATOR

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
plusminus = ttk.Button(keypad, text='+/-', command=lambda: cout('pm')).grid(row=5, column=2)
copy = ttk.Button(keypad, text='Copy', command=lambda: cout('Copy')).grid(row=5, column=3)

root.mainloop()
