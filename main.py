from gui import GUI


def main() -> None:
    gui_instance = GUI()
    gui_instance.create_display()
    gui_instance.create_buttons()
    gui_instance.keyboard_event_binding()
    gui_instance.mainloop()


if __name__ == '__main__':
    main()
