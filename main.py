from gui import GUI


def main() -> None:
    gui_instance = GUI()
    gui_instance.default_style_settings()
    gui_instance.create_simple_display()
    gui_instance.create_simple_buttons()
    gui_instance.keyboard_event_binding()
    gui_instance.mainloop()


if __name__ == '__main__':
    main()
