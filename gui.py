from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from storage import Storage


class GUI(Tk):

    def __init__(self):
        ''' View initializer '''
        super().__init__()
        # Main window properties
        self.title("PyCalc v0.1-beta")
        self.resizable(False, False)
        styler = ttk.Style()
        styler.configure("TLabel",
                         font='Times 20')
        styler.configure("TButton",
                         relief='flat',
                         width='5',
                         padding='10',
                         background='bisque')
        styler.configure("GreenButton.TButton",
                         relief='falt',
                         background='SeaGreen2',
                         foreground='green4')
        styler.configure("Snow.TFrame",
                         background='snow2')
        # Inheriting from Storage for program logic
        self.logic = Storage()
        # Set General layout
        self.content = ttk.Frame(master=self,
                                 padding=(3, 3, 3, 3),
                                 style='Snow.TFrame')
        self.mainframe = ttk.Frame(self.content,
                                   relief='flat')
        self.content.grid()
        self.mainframe.grid()
        self.label_text = StringVar()
        # Create display
        self._create_display()

    def _create_display(self):
        ''' Create the display '''
        display_frame = ttk.Frame(self.mainframe, relief='flat')
        display_frame['borderwidth'] = 10
        display_label = ttk.Label(display_frame,
                                  textvariable=self.label_text)
        # grid above widgets
        display_frame.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        display_label.grid(row=0, column=0, columnspan=4)
        # Create buttons
        self._create_buttons(self.mainframe)

    def _create_buttons(self, mainframe):
        ''' Create buttons under keypad '''
        keypad = ttk.Frame(mainframe)
        # row 1
        mul = ttk.Button(keypad, text='*',
                         command=lambda: self._button_invoke('*'))
        div = ttk.Button(keypad, text='/',
                         command=lambda: self._button_invoke('/'))
        clear = ttk.Button(keypad, text='C',
                           command=lambda: self._button_invoke('C'))
        allClear = ttk.Button(keypad, text='AC',
                              command=lambda: self._button_invoke('AC'))
        # row 2
        nine = ttk.Button(keypad, text='9',
                          command=lambda: self._button_invoke('9'))
        eight = ttk.Button(keypad, text='8',
                           command=lambda: self._button_invoke('8'))
        seven = ttk.Button(keypad, text='7',
                           command=lambda: self._button_invoke('7'))
        sub = ttk.Button(keypad, text='-',
                         command=lambda: self._button_invoke('-'))
        # row 3
        six = ttk.Button(keypad, text='6',
                         command=lambda: self._button_invoke('6'))
        five = ttk.Button(keypad, text='5',
                          command=lambda: self._button_invoke('5'))
        four = ttk.Button(keypad, text='4',
                          command=lambda: self._button_invoke('4'))
        add = ttk.Button(keypad, text='+',
                         command=lambda: self._button_invoke('+'))
        # row 4
        three = ttk.Button(keypad, text='3',
                           command=lambda: self._button_invoke('3'))
        two = ttk.Button(keypad, text='2',
                         command=lambda: self._button_invoke('2'))
        one = ttk.Button(keypad, text='1',
                         command=lambda: self._button_invoke('1'))
        plusMinus = ttk.Button(keypad, text='+/-',
                               command=lambda: self._button_invoke('i'))
        # row 5
        dot = ttk.Button(keypad, text='.',
                         command=lambda: self._button_invoke('.'))
        zero = ttk.Button(keypad, text='0',
                          command=lambda: self._button_invoke('0'))
        copy = ttk.Button(keypad, text='Copy',
                          command=lambda: self._button_invoke('c'))
        equal = ttk.Button(keypad, text='=',
                           style='GreenButton.TButton',
                           command=lambda: self._button_invoke('='))
        buttons = {mul: (1, 0),
                   div: (1, 1),
                   clear: (1, 2),
                   allClear: (1, 3),
                   nine: (2, 0),
                   eight: (2, 1),
                   seven: (2, 2),
                   sub: (2, 3),
                   six: (3, 0),
                   five: (3, 1),
                   four: (3, 2),
                   add: (3, 3),
                   three: (4, 0),
                   two: (4, 1),
                   one: (4, 2),
                   plusMinus: (4, 3),
                   dot: (5, 0),
                   zero: (5, 1),
                   copy: (5, 2),
                   equal: (5, 3),
                   }
        keypad.grid()
        for bt, pos in buttons.items():
            bt.grid(row=pos[0], column=pos[1])

    def _button_invoke(self, bt):

        if bt is '=':
            ''' If button pressed is '=' '''
            to_display = 'Ans: '+self.logic.show_answer()
            if(len(to_display)>17):
                ttk.Style().configure("TLabel",font='Times '+str(20*17//len(to_display)))
            else:
                ttk.Style().configure("TLabel",font='Times 20')
            self.label_text.set(to_display)
        elif bt is 'Copy':
            self.logic.copy_to_clipboard()
        else:
            self.logic.into_storage(bt)
            to_display = self.logic.show_storage()
            if(len(to_display)>17):
                ttk.Style().configure("TLabel",font='Times '+str(20*17//len(to_display)))
            else:
                ttk.Style().configure("TLabel",
                         font='Times 20')
            self.label_text.set(to_display)
                
