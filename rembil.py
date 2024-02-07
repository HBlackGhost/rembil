#! /usr/bin/python3
import os
import subprocess
import argparse
from colorama import Fore
from modules import banner , menues
def st_1() :
    os.system('clear')
    banner.banner()
    parser = argparse.ArgumentParser(prog="rembil" ,description=Fore.LIGHTGREEN_EX+"Rembil is a utility designed for managing executable files on linux systems, offering streamlined installation and removal processes. By simplifying file copying, permission setting, and symbolic link creation, it enhances system organization and workflow efficiency. With its intuitive interface, users can seamlessly integrate or uninstall tools, optimizing their computing environment."+Fore.LIGHTYELLOW_EX)
    parser.add_argument('-m', dest='MODE',help='build or remove',choices='br')
    parser.add_argument('-p', dest='PATH', help='The Path Of Tool  To Be Builded [For Build]')
    parser.add_argument('-d',dest='DIRECTORY', help='The Directory Name of Tool To Be Build [For Build]')
    parser.add_argument('-f', dest='FILE' , help='The Tool Name File in The Directory [For Build]')
    parser.add_argument('-c', dest='CALL' , help='The Name Wanted To Call Tool In Terminal [For Build] ')
    parser.add_argument('-RD',dest='REMOVE_DIRECTORY', help='The Directory Name of Tool To Be Remove [For Remove] ')
    parser.add_argument('-RF', dest='REMOVE_FILE' , help='The Tool File Name in The Directory  [For Remove] ')
    parser.add_argument('-RC', dest='REMOVE_CALL' , help='The Call Of Tool Wanted To Remove [For Remove] ')
    args = parser.parse_args()
    if args.MODE == 'b' :
        if os.geteuid() == 0 :
            if os.path.exists(f"{args.PATH}/{args.FILE}") and args.PATH != None and args.DIRECTORY != None and args.FILE != None and args.CALL != None:
                command_1 = f"cp -r { args.PATH } /usr/share/ && chmod +x /usr/share/{args.DIRECTORY}/{ args.FILE} "
                subprocess.run(command_1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                menues.we_working_g()
                command_2 = f"touch /usr/bin/{args.CALL} && echo '#!/bin/bash \ncd /usr/share/{args.DIRECTORY}/  && ./{args.FILE} \"$@\" ' > /usr/bin/{args.CALL} && chmod +x /usr/bin/{args.CALL}"
                subprocess.run(command_2, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                if os.path.exists(f"/usr/bin/{args.CALL}"):
                    print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTBLUE_EX+" Now You Can Use "+Fore.LIGHTRED_EX+f"{args.CALL}"+Fore.LIGHTYELLOW_EX+" Successfully")
                    menues.end()
                    exit()
            else :
                menues.check_3_values()
        else:
            menues.err_root()
    elif args.MODE == 'r':
        if os.geteuid() ==0 :
            if os.path.exists(f"/usr/share/{args.REMOVE_DIRECTORY}/{args.REMOVE_FILE}") and os.path.exists(f"/usr/bin/{args.REMOVE_CALL}") and args.REMOVE_FILE != None and args.REMOVE_DIRECTORY != None and args.REMOVE_CALL != None:
                print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTBLUE_EX+" We Finded"+Fore.LIGHTRED_EX+f" {args.REMOVE_CALL}"+Fore.LIGHTYELLOW_EX+" Successfully")
                command_1 = f"rm -r /usr/share/{args.REMOVE_DIRECTORY} && rm /usr/bin/{args.REMOVE_CALL}"
                subprocess.run(command_1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                menues.we_working_g()
                print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTBLUE_EX+ " We Removed "+Fore.LIGHTRED_EX+f"{args.REMOVE_CALL}"+Fore.LIGHTYELLOW_EX+" Successfully")
                menues.end()
                exit()
            else :
                menues.check_3_values()
        else:
            menues.err_root()
    else :
        return
st_1()
def st_2() :
    if os.geteuid() == 0 :
        try:
            inp_0 = input(f"[!] Enter Your Mode ({Fore.LIGHTGREEN_EX}Build,{Fore.LIGHTRED_EX}Remove{Fore.LIGHTCYAN_EX}) : ")
            if inp_0 in {'B','b','Build','build'} :
                inp_1 = input("Enter Path Of Tool To Be Builded : ")
                inp_2 = input("Enter your Directory Name of Tool To Be Build : ")
                inp_3 = input("Enter your Tool Name File in The Directory : ")
                inp_4 = input("Enter your Name Wanted To Call Tool In Terminal : ")
                if os.path.exists(f"{inp_1}/{inp_3}") :
                    command_1 = f"cp -r {inp_1 } /usr/share/ && chmod +x /usr/share/{inp_2}/{inp_3} "
                    subprocess.run(command_1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                    menues.we_working_g()
                    command_2 = f"touch /usr/bin/{inp_4} && echo '#!/bin/bash \ncd /usr/share/{inp_2}/  && ./{inp_3} \"$@\" ' > /usr/bin/{inp_4} && chmod +x /usr/bin/{inp_4}"
                    subprocess.run(command_2, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                    if os.path.exists(f"/usr/bin/{inp_4}"):
                        print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTBLUE_EX+" Now You Can Use "+Fore.LIGHTRED_EX+f"{inp_4}"+Fore.LIGHTYELLOW_EX+" Successfully")
                        menues.end()
                        exit()
                else :
                   menues.check_3_values()
            if inp_0 in {'R','r','Remove','remove'} :
                inp_1_r = input("Enter your Directory Name of Tool To Be Remove : ")
                inp_2_r = input("Enter your Tool File Name in The Directory : ")
                inp_3_r = input("Enter your Call Of Tool Wanted To Remove : ")
                if os.path.exists(f"/usr/share/{inp_1_r}/{inp_2_r}") and os.path.exists(f"/usr/bin/{inp_3_r}"):
                    print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTBLUE_EX+" We Finded"+Fore.LIGHTRED_EX+f" {inp_3_r}"+Fore.LIGHTYELLOW_EX+" Successfully")
                    command_1 = f"rm -r /usr/share/{inp_1_r} && rm /usr/bin/{inp_3_r}"
                    subprocess.run(command_1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                    menues.we_working_g()
                    print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTBLUE_EX+ " We Removed "+Fore.LIGHTRED_EX+f"{inp_3_r}"+Fore.LIGHTYELLOW_EX+" Successfully")
                    menues.end()
                    exit()
                else :
                    menues.check_3_values()
            else :
                print(f"{Fore.LIGHTRED_EX}Oops, Choosed May Not Be Correct")
        except KeyboardInterrupt:
            print("");menues.end()
    else :
        menues.err_root()
st_2()
