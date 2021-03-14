from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar

try:
    from pyperclip import copy as to_clipboard
except ModuleNotFoundError:
    print("Install pyperclip library to use Copy function")
    pass

from .storage import Storage
from .core_logic import Calculate


class GUI(Tk):

    __operators: list = ['/', '*', '+', '-']

    def __init__(self):
        super().__init__()
        # Main window properties
        self.title("Pymanujan (v2.0)")
        self.resizable(False, False)
        self.styler = ttk.Style()
        self._old_layout = ['*', '/', 'C', 'AC',
                            '9', '8', '7', '-',
                            '6', '5', '4', '+',
                            '3', '2', '1', '+/-',
                            '.', '0', 'Copy', '=']
        self._layout = ['AC', 'C', '+/-', '/',
                        '7', '8', '9', '*',
                        '4', '5', '6', '-',
                        '1', '2', '3', '+',
                        '0', '.', 'copy', '=']
        self._adv_layout = ['(', ')', '^', 'C',
                            '*', 'sin', 'cos', 'tan',
                            '/', 'asin', 'acos', 'atan',
                            '+', 'x!', 'log', 'ln',
                            '-', '\u03C0', 'e', '=']

        # Inheriting from Storage for program `logic`
        self.logic = Storage()

        # Creating root widgets and variable containers
        self.content = ttk.Notebook(master=self,
                                    padding=(0, 0, 0, 0),
                                    style='Outliner.TFrame')
        self.mainframe = ttk.Frame(self.content,
                                   relief='flat',
                                   padding=(0, 0, 0, 0))
        self.mainframe2 = ttk.Frame(self.content)
        self.content.add(self.mainframe, text='            Basic           ')
        self.content.add(self.mainframe2, text='         Advanced          ')
        self.content.grid()
        self.label_text = StringVar()

    def default_style_settings(self):
        """GUI uses this style as default. New styles can be added after this
        method with the following name convention: <theme_name>_style_setting.
        This method could get deprecated in future versions; styles and themes
        could be set using a YAML file.
        """

        self.styler.configure("TFrame",
                              foreground='snow',
                              background='grey17')
        self.styler.configure("TLabel",
                              padding=(0, 10, 0, 10),
                              foreground='snow',
                              background='grey17',
                              font='Times 25')
        self.styler.configure("TButton",
                              font='Times 16 italic bold',
                              relief='flat',
                              width='4',
                              padding=(10, 10, 10, 10),
                              foreground='grey21',
                              background='snow3')
        self.styler.configure("Numerals.TButton",
                              font='Times 16',
                              relief='flat',
                              foreground='snow2',
                              background='grey21')
        self.styler.configure("EqualButton.TButton",
                              relief='flat',
                              foreground='snow2',
                              background='SpringGreen3')
        self.styler.configure("Outliner.TFrame",
                              background='snow2')

    def create_basic_display(self):
        """This method creates the layout and widgets for BASIC tab"""
        display_frame = ttk.Frame(self.mainframe, relief='flat')
        display_frame['borderwidth'] = 10
        display_label = ttk.Label(display_frame,
                                  textvariable=self.label_text)

        display_frame.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        display_label.grid(row=0, column=0, columnspan=4)

    def create_basic_buttons(self):
        """Buttons and their wiring for BASIC tab is contained here"""
        keypad = ttk.Frame(self.mainframe)
        button_objects = {
                button: ttk.Button(
                        master=keypad,
                        text=button,
                        command=lambda button=button: self._button_invoke(
                                button
                                )
                        )
                for button in self._layout
                }
        button_objects['AC']['command'] = lambda: self._button_invoke('A')
        button_objects['+/-']['command'] = lambda: self._button_invoke('i')
        button_objects['=']['style'] = 'EqualButton.TButton'

        for button_char in self._layout:
            if button_char.isnumeric():
                button_objects[button_char]['style'] = "Numerals.TButton"
            elif button_char == '.':
                button_objects[button_char]['style'] = "Numerals.TButton"
            elif button_char == 'copy':
                button_objects[button_char]['style'] = "Numerals.TButton"

        keypad.grid()
        row, column = 0, 0
        for button in button_objects.values():
            button.grid(row=(row//4)+1, column=column % 4)
            row += 1
            column += 1

    def create_advanced_display(self):
        """This method creates the layout and widgets for ADVANCED tab"""
        display_frame = ttk.Frame(self.mainframe2, relief='flat')
        display_frame['borderwidth'] = 10
        display_label = ttk.Label(display_frame,
                                  textvariable=self.label_text)

        display_frame.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        display_label.grid(row=0, column=0, columnspan=4)

    def create_advanced_buttons(self):
        """Buttons and their wiring for ADVANCED tab is contained here"""
        keypad = ttk.Frame(self.mainframe2)
        button_objects = {
                button: ttk.Button(
                        master=keypad,
                        text=button,
                        command=lambda button=button: self._button_invoke(
                                button)
                        )
                for button in self._adv_layout
                }
        button_objects['=']['style'] = 'EqualButton.TButton'

        keypad.grid()
        row, column = 0, 0
        for button in button_objects.values():
            button.grid(row=(row//4)+1, column=column % 4)
            row += 1
            column += 1

    def _button_invoke(self, bt: str) -> None:
        """Backend logic when buttons are invoked.

        The command for most buttons are same as its button['character'] except
        for a few, namely `=`, `Copy` and `x!`. Storage instance `logic` is
        called to input/evaluate the inputs. Refer `storage.py` docs for more
        info.

        Arguments
        ---------
        bt : str
            character corresponding to the invoked button
        """
        to_display = self.logic.show_storage()
        if bt == '=':
            get_storage = self.logic.show_storage_as_list()
            to_display = 'Ans: '+self._calculate_answer(get_storage)
        elif bt == 'Copy':
            self._copy_to_clipboard(self.logic.show_storage_as_list())
        elif bt == 'x!':
            self.logic.into_storage('!')
            to_display = self.logic.show_storage()
        else:
            self.logic.into_storage(bt)
            to_display = self.logic.show_storage()
        self._adjust_and_set_TLabel_font(to_display)

    def keyboard_event_binding(self):
        self.bind("<Key>", self._callback)

    def _callback(self, e):
        key_map = {'c': 'Copy',
                   'a': 'A',
                   'i': 'i',
                   '!': 'x!',
                   '\r': '=',
                   '\x08': 'C',
                   'b': 'C',
                   '!': 'x!'}
        if e.char.lower() in self._layout:
            self._button_invoke(e.char.lower())
        elif e.char.lower() in self._adv_layout:
            self._button_invoke(e.char.lower())
        elif e.char.lower() in key_map:
            self._button_invoke(key_map[e.char.lower()])
        elif e.char.lower() == 'q':
            self.destroy()

    def _calculate_answer(self, inputs_as_list):
        calculate_instance = Calculate(inputs_as_list)
        return calculate_instance.calculate()

    def _copy_to_clipboard(self, inputs_as_list):
        """Copies content of display label to clipboard."""
        to_clipboard("".join(inputs_as_list))

    def _adjust_and_set_TLabel_font(self, to_display):
        """Dynamic font size setting for display label widget."""
        if(len(to_display) >= 14):
            font_size = int(14/len(to_display) * 25)
        else:
            font_size = 25
        FONT = 'Times '+str(font_size)
        self.styler.configure("TLabel", font=FONT)
        self.label_text.set(to_display)
