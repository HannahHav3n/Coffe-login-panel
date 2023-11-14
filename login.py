import hashlib
import os
from datetime import datetime
from pystyle import Colorate, Colors
from colorama import Fore

ascii_art = f"""  _____     ______          __          _                           __
 / ___/__  / _/ _/__ ___   / /__  ___ _(_)__    ___  ___ ____  ___ / /
/ /__/ _ \/ _/ _/ -_) -_) / / _ \/ _ `/ / _ \  / _ \/ _ `/ _ \/ -_) / 
\___/\___/_//_/ \__/\__/ /_/\___/\_, /_/_//_/ / .__/\_,_/_//_/\__/_/  
                                /___/        /_/                      
"""


print(Colorate.Vertical(Colors.red_to_blue, ascii_art))

print(f"Time: {datetime.now().strftime('%H:%M')}")


rl = input("Register or login [r/l]: ")

if rl.lower() == "l":
    username = input(f"{Fore.YELLOW}[!]{Fore.RESET} Username: ")
    password = input(f"{Fore.YELLOW}[!]{Fore.RESET} Password: ")
    data_to_check = f"{username}:{password}"
    hashed_user_and_pass = hashlib.sha256(data_to_check.encode()).hexdigest()
    with open(f"database/LOGONS.hannahs_login_system", 'r') as f:
        file_content = f.read()
        if hashed_user_and_pass in file_content:
            print(f"{Fore.GREEN}[+]{Fore.RESET} Logged in")
        else:
            print(f"{Fore.RED}[-]{Fore.RESET} Incorrect user or password")



elif rl.lower() == "r":
    username = input(f"{Fore.YELLOW}[!]{Fore.RESET} Username: ")
    password = input(f"{Fore.YELLOW}[!]{Fore.RESET} Password: ")
    data_to_hash = f"{username}:{password}"
    hashed_user_and_pass = hashlib.sha256(data_to_hash.encode()).hexdigest()
    with open("database/LOGONS.hannahs_login_system", 'r') as f:
        file_content = f.read()
        if hashed_user_and_pass in file_content:
            print(f"{Fore.RED}[-]{Fore.RESET} This username it taken")
            exit()
        else:
            with open(f"database/LOGONS.hannahs_login_system", 'a') as f:
                f.write(f"\n{hashed_user_and_pass}")
            print(f"{Fore.GREEN}[+]{Fore.RESET} Registered succesfully")
            exit()
            print(f"{Fore.GREEN}[+]{Fore.RESET} Registered succesfully")
            exit()
