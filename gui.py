from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar

from pyperclip import copy as to_clipboard

from storage import Storage
from core_logic import Calculate


class GUI(Tk):

    __operators: list = ['/', '*', '+', '-']

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
                                 style='Outliner.TFrame')
        self.mainframe = ttk.Frame(self.content,
                                   relief='flat')
        self.content.grid()
        self.mainframe.grid()
        self.label_text = StringVar()

    def default_style_settings(self):
        self.styler.configure("TLabel",
                              font='Times 20')
        self.styler.configure("TButton",
                              relief='flat',
                              width='5',
                              padding='10',
                              background='bisque')
        self.styler.configure("EqualButton.TButton",
                              relief='falt',
                              background='SeaGreen2',
                              foreground='green4')
        self.styler.configure("Outliner.TFrame",
                              background='snow2')

    def create_simple_display(self):
        ''' Create the display '''
        display_frame = ttk.Frame(self.mainframe, relief='flat')
        display_frame['borderwidth'] = 10
        display_label = ttk.Label(display_frame,
                                  textvariable=self.label_text)
        # grid above widgets
        display_frame.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        display_label.grid(row=0, column=0, columnspan=4)

    def create_simple_buttons(self):
        ''' Create buttons under keypad '''
        keypad = ttk.Frame(self.mainframe)
        button_objects = {button: ttk.Button(keypad, text=button,
            command=lambda button=self._layout[button]: self._button_invoke(button))
            for button in self._layout}
        button_objects['=']['style'] = 'EqualButton.TButton'

        keypad.grid()
        row, column = 0, 0
        for button in button_objects.values():
            button.grid(row=(row//4)+1, column=column % 4)
            row += 1
            column += 1

    def _button_invoke(self, bt):
        if bt is '=':
            ''' If button pressed is '=' '''
            to_display = 'Ans: '+self._get_answer(self.logic.show_storage_as_list(),
                                                  self.__operators)
            if(len(to_display) > 17):
                ttk.Style().configure("TLabel", font='Times '+str(20*17//len(to_display)))
            else:
                ttk.Style().configure("TLabel", font='Times 20')
            self.label_text.set(to_display)
        elif bt is 'c':
            self._copy_to_clipboard(self.logic.show_storage_as_list())
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

    def _get_answer(self, inputs_as_list, operators):
        calculate_instance = Calculate(inputs_as_list, operators)
        return calculate_instance.calculate()

    def _copy_to_clipboard(self, inputs_as_list):
        to_clipboard("".join(inputs_as_list))
