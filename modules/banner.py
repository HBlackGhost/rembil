import pyfiglet
from colorama import Fore
def banner() :
    text_1 ="R E M B I L"
    text_2=pyfiglet.figlet_format(text_1 )
    print(Fore.LIGHTCYAN_EX+text_2,end="")