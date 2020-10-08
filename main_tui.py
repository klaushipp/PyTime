# encoding: utf-8
# pylint: disable=maybe-no-member

import curses
import time
import npyscreen

class MenuList(npyscreen.BoxTitle):
    def create(self):
        pass
    def when_value_edited(self):
        self.parent.update_content_box()

    # def when_cursor_moved(self):
    #     val_list = self.get_values()
    #     val_idx = self.get_value()
    #     if val_idx == None:
    #         val_idx = 0
    #     val = val_list[val_idx]
    #     self.parent.update_edit_content(val)

class TimeBox(npyscreen.BoxTitle):
    def create(self):
        self.values = ["TimeBox"]

    def show(self):    
        self.display()

class TimerBox(npyscreen.BoxTitle):
    def create(self):
        self.values = ["TimerBox"]

    def show(self):    
        self.display()

class MainForm(npyscreen.FormBaseNew):
    def afterEditing(self):
        self.parentApp.setNextForm(None)
        
    def create(self):
        y,x = self.useable_space()

        self.menu_items = ["Time", "Timer", "Exit"]

        self.menu_list = self.add(MenuList, 
                                  name = "Menu",
                                  values = self.menu_items,
                                  max_width = x // 4)

        self.time_window = self.add(TimeBox,
                                       name = "Time",
                                       relx = x // 4 + 5,
                                       rely = 2)
                                    
        self.timer_window = self.add(TimerBox,
                                       name = "Timer",
                                       relx = x // 4 + 5,
                                       rely = 2)
        self.update_content_box()

    def update_content_box(self):
        '''
        Update the content of current content box depending on 
        menu_item. Jump into the box to edit stuff here.
        '''
        menu_idx = self.menu_list.get_value()
        if menu_idx == None:
            menu_idx = 0
        menu_item = self.menu_items[menu_idx]
        if menu_item == 'Time': 
            self.time_window.show()
        elif menu_item == 'Timer':
            self.timer_window.show()
        elif menu_item == 'Exit':
            self.parentApp.switchForm(None)


    def update_edit_content(self,val):
        self.content_window.show_something([val])

    def update_cursor_content(self):
        self.content_window.show_something(["cursor"])

class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.TransparentThemeLightText)
        self.addForm("MAIN", MainForm)


if __name__ == "__main__":
    App = TestApp()
    App.run()
