from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar

from pyperclip import copy as to_clipboard

from storage import Storage
from core_logic import Calculate


class GUI(Tk):

    __operators: list = ['/', '*', '+', '-']

    def __init__(self):
        super().__init__()
        # Main window properties
        self.title("PyCalc (v2.1-alpha)")
        self.resizable(False, False)
        self.styler = ttk.Style()
        self._layout = ['*', '/', 'C', 'AC',
                        '9', '8', '7', '-',
                        '6', '5', '4', '+',
                        '3', '2', '1', '+/-',
                        '.', '0', 'Copy', '=']
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
                                   relief='flat')
        self.mainframe2 = ttk.Frame(self.content)
        self.content.add(self.mainframe, text='Basic')
        self.content.add(self.mainframe2, text='Advanced')
        self.content.grid()
        self.label_text = StringVar()

    def default_style_settings(self):
        """GUI uses this style as default. New styles can be added after this
        method with the following name convention: <theme_name>_style_setting.
        This method could get deprecated in future versions; styles and themes
        could be set using a YAML file.
        """

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
        self.styler.configure("EqualButton2.TButton",
                              relief='flat',
                              background='firebrick1',
                              foreground='green4')
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
        button_objects['=']['style'] = 'EqualButton2.TButton'

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
        if bt == '=':
            get_storage = self.logic.show_storage_as_list()
            to_display = 'Ans: '+self._calculate_answer(get_storage)
            self._adjust_and_set_TLabel_font(to_display)
        elif bt == 'Copy':
            self._copy_to_clipboard(self.logic.show_storage_as_list())
        elif bt == 'x!':
            self.logic.into_storage('!')
            self._adjust_and_set_TLabel_font(to_display)
        else:
            self.logic.into_storage(bt)
            to_display = self.logic.show_storage()
            self._adjust_and_set_TLabel_font(to_display)

    def keyboard_event_binding(self):
        self.bind("<Key>", self._callback)

    def _callback(self, e):
        if e.char.lower() in self._layout:
            self._button_invoke(e.char)
        elif e.char.lower() == 'c':
            self._button_invoke('Copy')
        elif e.char.lower() == 'a':
            self._button_invoke('A')
        elif e.char.lower() == 'i':
            self._button_invoke('i')
        elif e.char == '\r':
            self._button_invoke('=')
        elif e.char.lower() in ('\x08', 'b'):
            self._button_invoke('C')
        elif e.char.lower() == 'q':
            self.destroy()
        elif e.char == '(':
            self._button_invoke('(')
        elif e.char == ')':
            self._button_invoke(')')

    def _calculate_answer(self, inputs_as_list):
        calculate_instance = Calculate(inputs_as_list)
        return calculate_instance.calculate()

    def _copy_to_clipboard(self, inputs_as_list):
        """Copies content of display label to clipboard."""
        to_clipboard("".join(inputs_as_list))

    def _adjust_and_set_TLabel_font(self, to_display):
        """Dynamic font size setting for display label widget."""
        if(len(to_display) > 17):
            font_size = 20*17//len(to_display)
        else:
            font_size = 20
        FONT = 'Times '+str(font_size)
        self.styler.configure("TLabel", font=FONT)
        self.label_text.set(to_display)
