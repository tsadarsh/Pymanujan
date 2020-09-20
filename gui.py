from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from storage import Storage


class GUI(Tk):

    def __init__(self):
        ''' View initializer '''
        super().__init__()
        # Main window properties
        self.title("PyCalc (v1.0)")
        self.resizable(False, False)
        self.styler = ttk.Style()
        self._layout = {'*': '*', '/': '/', 'C': 'C', 'AC': 'AC',
                        '9': '9', '8': '8', '7': '7', '-': '-',
                        '6': '6', '5': '5', '4': '4', '+': '+',
                        '3': '3', '2': '2', '1': '1', '+/-': 'i',
                        '.': '.', '0': '0', 'Copy': 'c', '=': '='}

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

    def style_settings(self):
        self.styler.configure("TLabel",
                         font='Times 20')
        self.styler.configure("TButton",
                         relief='flat',
                         width='5',
                         padding='10',
                         background='bisque')
        self.styler.configure("GreenButton.TButton",
                         relief='falt',
                         background='SeaGreen2',
                         foreground='green4')
        self.styler.configure("Snow.TFrame",
                         background='snow2')
    def create_display(self):
        ''' Create the display '''
        display_frame = ttk.Frame(self.mainframe, relief='flat')
        display_frame['borderwidth'] = 10
        display_label = ttk.Label(display_frame,
                                  textvariable=self.label_text)
        # grid above widgets
        display_frame.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        display_label.grid(row=0, column=0, columnspan=4)

    def create_buttons(self):
        ''' Create buttons under keypad '''
        keypad = ttk.Frame(self.mainframe)
        button_objects = {button: ttk.Button(keypad, text=button,
            command=lambda button=self._layout[button]: self._button_invoke(button))
            for button in self._layout}
        button_objects['=']['style'] = 'GreenButton.TButton'

        keypad.grid()
        row, column = 0, 0
        for button in button_objects.values():
            button.grid(row=(row//4)+1, column=column % 4)
            row += 1
            column += 1

    def _button_invoke(self, bt):

        if bt is '=':
            ''' If button pressed is '=' '''
            to_display = 'Ans: '+self.logic.show_answer()
            if(len(to_display) > 17):
                ttk.Style().configure("TLabel", font='Times '+str(20*17//len(to_display)))
            else:
                ttk.Style().configure("TLabel", font='Times 20')
            self.label_text.set(to_display)
        elif bt is 'c':
            self.logic.copy_to_clipboard()
        else:
            self.logic.into_storage(bt)
            to_display = self.logic.show_storage()
            if(len(to_display) > 17):
                ttk.Style().configure("TLabel", font='Times '+str(20*17//len(to_display)))
            else:
                ttk.Style().configure("TLabel", font='Times 20')
            self.label_text.set(to_display)

    def keyboard_event_binding(self):
        self.bind("<Key>", self._callback)

    def _callback(self, e):
        if e.char.lower() in self._layout.values():
            self._button_invoke(e.char)
        elif e.char == '\r':
            self._button_invoke('=')
        elif e.char.lower() in ('\x08', 'b'):
            self._button_invoke('C')
        elif e.char.lower() == 'q':
            self.destroy()
