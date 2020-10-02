# encoding: utf-8
# pylint: disable=maybe-no-member

import curses
import time
import npyscreen

class MenuList(npyscreen.BoxTitle):
    def when_value_edited(self):
        self.parent.update_edit_content()

    def when_check_value_changed(self):
        self.parent.update_change_content()

    def when_cursor_moved(self):
        self.parent.update_cursor_content()

    def when_check_cursor_moved(self):
        self.parent.update_cursor_content()

class ContentBox(npyscreen.BoxTitle):
    def create(self):
        pass

    def show_something(self, content):
        self.values = content
        self.display()

class MainForm(npyscreen.FormBaseNew):
    def afterEditing(self):
        self.parentApp.setNextForm(None)
        
    def create(self):
        y,x = self.useable_space()

        self.menu_list = self.add(MenuList, 
                                  name = "Menu",
                                  values = ["Time", "Timer", "Exit"],
                                  max_width = x // 4)

        self.content_window = self.add(ContentBox,
                                       name = "Content",
                                       relx = x // 4 + 5,
                                       rely = 2)
                                    
    def update_edit_content(self):
        self.content_window.show_something("edit")

    def update_change_content(self):
        self.content_window.show_something("change")

    def update_cursor_content(self):
        self.content_window.show_something("cursor")

class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.TransparentThemeLightText)
        self.addForm("MAIN", MainForm)


if __name__ == "__main__":
    App = TestApp()
    App.run()
