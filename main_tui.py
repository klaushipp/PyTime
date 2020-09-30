# encoding: utf-8
# pylint: disable=maybe-no-member

import curses
import time
import npyscreen

def print_banner():
    window = curses.newwin(6, 30, 0, 0)

    pytime_ascii_str = (" ___     _____ _           \n"
                        "| _ \_  |_   _(_)_ __  ___ \n"
                        "|  _/ || || | | | '  \/ -_)\n"
                        "|_|  \_, ||_| |_|_|_|_\___|\n"
                        "     |__/                  \n"
                        )

    window.addstr(pytime_ascii_str)
    window.refresh()
    return window

class MenuList(npyscreen.BoxTitle):
    def __init__(self, *args, **keywords):
        super(MenuList, self).__init__(*args, **keywords)

    def when_value_edited(self):
        self.parent.parentApp.queue_event(npyscreen.Event("event_menu_select"))

class SideMenu(npyscreen.Form):
    def create(self):
        self.Text1 = self.add(npyscreen.TitleText, name = "Name")
        self.Date = self.add(npyscreen.TitleDateCombo, name = "Date blabla")

class MainForm(npyscreen.FormBaseNew):
    def afterEditing(self):
        self.parentApp.setNextForm(None)
        
    def create(self):
        y,x = self.useable_space()
        self.menu_list = self.add(MenuList, 
                                  name = "Menu",
                                  values = ["Time", "Timer", "Exit"],
                                  max_width = x //4)
        # self.button_Time = self.add(npyscreen.Menu, name = "Time")
        # self.button_Timer = self.add(npyscreen.Button, name = "Timer")
        # self.button_Exit = self.add(npyscreen.Button, name = "Exit")

    def event_menu_select(self, event):
        pass


class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.TransparentThemeLightText)
        self.addForm("MAIN", MainForm)


if __name__ == "__main__":
    App = TestApp()
    App.run()
