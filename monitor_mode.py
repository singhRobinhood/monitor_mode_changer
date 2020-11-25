#!/usr/bin/env python3

import subprocess
import re

def iwconfig_result(interface):
    result = subprocess.check_output(["iwconfig", interface]).decode('utf-8')
    in_which_mode = re.search(r"Mode:.*", result)
    if in_which_mode:
        print(in_which_mode.group(0))

def mode_changer(interface):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["airmon-ng", "check", "kill"])
    subprocess.run(["airmon-ng", "start", interface], stdout=subprocess.PIPE)

def mode_changer2():
    subprocess.run(["airmon-ng", "stop", "wlan0mon"], stdout=subprocess.PIPE)

def results():
    iwconfig_result = subprocess.check_output(["iwconfig"]).decode('utf-8')
    in_which_mode = re.search(r"Mode:.*", iwconfig_result)
    if in_which_mode:
        print(in_which_mode.group(0))

def choice():
    print("enter 1 for manage_mode ")
    print("enter 2 for monitor_mode ")
    choice = int(input("enter your choice >> "))
    if (choice == 1):
        try:
            print("_______________________________________________ \n")
            interface = input("Interface name >> ")
            iwconfig_result(interface)
            print("_______________________________________________ \n")
            mode_changer2()
            print("_______________________________________________ \n")
            results()
            print("_______________________________________________ \n")
        except:
            mode_changer2()
            results()
    else:
        try:
            print("________________________________________________ \n")
            interface = input("Interface name >> ")
            iwconfig_result(interface)
            print("________________________________________________ \n")
            mode_changer(interface)
            print("_______________________________________________ \n")
            results()
            print("_______________________________________________ \n")
        except:
            print("you're already in monitor mode")

choice()

