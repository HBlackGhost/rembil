import time
from colorama import Fore
def we_working_g () :
    print(Fore.LIGHTGREEN_EX+"[!]"+Fore.LIGHTRED_EX+" Okay "+Fore.LIGHTGREEN_EX+", We Working In Your Goal"+Fore.LIGHTBLUE_EX+" (Please Be Patient) ")
    time.sleep(5)
def check_3_values () :
    print(Fore.LIGHTRED_EX+"[!]"+Fore.LIGHTYELLOW_EX+" ERROR :"+Fore.LIGHTGREEN_EX+" checks your first three values, "+Fore.LIGHTCYAN_EX+"it's correct ? ")
    exit()
def err_root () :
        print (Fore.LIGHTRED_EX+"[!]"+Fore.LIGHTYELLOW_EX+" ERROR : "+Fore.LIGHTGREEN_EX+"Rembil"+Fore.LIGHTYELLOW_EX+" must be run as"+Fore.LIGHTRED_EX+" root")
        print (Fore.LIGHTRED_EX+"[!]"+Fore.LIGHTYELLOW_EX+" Try that : "+Fore.RESET+"sudo rembil -args")
        exit()
def end () :
     print(Fore.LIGHTGREEN_EX+f"[-]"f" Thank you for {Fore.LIGHTBLUE_EX}using {Fore.LIGHTRED_EX}Rembil")
     print(Fore.LIGHTGREEN_EX+f"[-]"f"{Fore.LIGHTGREEN_EX} Created By {Fore.YELLOW}Black{Fore.WHITE} Ghost{Fore.LIGHTRED_EX} Hacker")
