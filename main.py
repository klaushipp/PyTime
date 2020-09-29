import os
import time
import math
import curses

def clear_screen():
    '''
    Should seperate between win and Linux
    '''
    os.system('cls')

def print_banner():
    print("\t ")

    print("\t ___     _____ _           ")
    print("\t| _ \_  |_   _(_)_ __  ___ ")
    print("\t|  _/ || || | | | '  \/ -_)")
    print("\t|_|  \_, ||_| |_|_|_|_\___|")
    print("\t     |__/                  ")

def draw_menu(menu_list, selection):
    clear_screen()
    print_banner()
    for idx,item in enumerate(menu_list):
        if idx == selection:
            prefix = "> "
        else:
            prefix = "  "
        print(prefix + item)

def home_menu():
    menu_list = ["Home", "Timer", "Exit"]
    menu_selection = 0

    # Refresh per second
    refresh_rate = 5

    while 1:
        draw_menu(menu_list, menu_selection)

        time.sleep(1/refresh_rate)
        if msvcrt.kbhit():
            nav = msvcrt.getch()

            if nav == b'j':
                menu_selection = menu_selection + 1
            elif nav == b'k':
                menu_selection = menu_selection - 1

            if menu_selection < 0:
                menu_selection = 0
            elif menu_selection > len(menu_list) -1:
                menu_selection = len(menu_list) - 1

            if nav == b'\r':
                if menu_selection == 1:
                    timer_menu()
                elif menu_selection == 2:
                    clear_screen()
                    break 

def timer_menu():
    menu_list = ["Start", "Stop", "Exit"]
    menu_selection = 0

    # Refresh per second
    refresh_rate = 5
    
    timer_start_sec = 12 * 60
    current_timer = timer_start_sec
    diff_time_str = "0"
    timer_on = False
    start_time = time.perf_counter()

    while 1:
        draw_menu(menu_list, menu_selection)
        print(diff_time_str)
        time.sleep(1/refresh_rate)
        if msvcrt.kbhit():
            nav = msvcrt.getch()

            
            #print(nav)

            if nav == b'j':
                menu_selection = menu_selection + 1
            elif nav == b'k':
                menu_selection = menu_selection - 1

            if menu_selection < 0:
                menu_selection = 0
            elif menu_selection > len(menu_list) -1:
                menu_selection = len(menu_list) - 1

            if nav == b'\r':
                if menu_selection == 0:
                    timer_on = True
                    start_time = time.perf_counter()
                    current_timer = timer_start_sec
                elif menu_selection == 1:
                    timer_on = False
                    current_timer = timer_start_sec
                elif menu_selection == 2:
                    clear_screen()
                    break
        
        if timer_on:
            current_timer = time.perf_counter()
            diff_time = current_timer - start_time
            timer_sec = timer_start_sec - diff_time
            diff_time_str = "%d:%02d" % (math.floor(timer_sec/60), timer_sec%60)            

def close_app():
    clear_screen()

def main():
    os.system('cls')

    home_menu()


if __name__ == "__main__":
    main()