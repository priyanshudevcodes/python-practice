RESET   = "\033[0m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
RED     = "\033[91m"
BLUE    = "\033[94m"
GOLD    = "\033[33m"
WHITE   = "\033[97m"
MAGENTA = "\033[95m"
DIM     = "\033[2m"

keeper = f"""
{BLUE}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈{RESET}
{GOLD}
   ██╗  ██╗███████╗███████╗██████╗ ███████╗██████╗
   ██║ ██╔╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
   █████╔╝ █████╗  █████╗  ██████╔╝█████╗  ██████╔╝
   ██╔═██╗ ██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗
   ██║  ██╗███████╗███████╗██║     ███████╗██║  ██║
   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝{RESET}
{BLUE}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈{RESET}
{DIM}                . * .  *  . * .
           *  .    *    .    *   .  *{RESET}
{CYAN}                        |{RESET}
{YELLOW}                       )))    {DIM}← torch{RESET}
{YELLOW}                        |{RESET}
{DIM}              _________|_________{RESET}
{WHITE}             |   {CYAN}  .-~~~-.    {WHITE}   |
             |  {CYAN} /  o_o  \\   {WHITE}   |
             |  {CYAN}|  (^_^)  |  {WHITE}   |
             |   {CYAN}\\  ~~~  /   {WHITE}   |
             |    {CYAN}`-----'    {WHITE}   |
             |   THE KEEPER     |
{DIM}             |_________________|
            /                   \\{RESET}
{GOLD}           /  {YELLOW}██████████████████{GOLD}  \\
          |  {YELLOW}█{GOLD} .-----------. {YELLOW}█{GOLD}  |
          |  {YELLOW}█{GOLD} |{MAGENTA} ✦ ✦ ✦ ✦ ✦ {GOLD}|{YELLOW}█{GOLD}  |
          |  {YELLOW}█{GOLD} |{CYAN}  ??? chest  {GOLD}|{YELLOW}█{GOLD}  |
          |  {YELLOW}█{GOLD} `-----------' {YELLOW}█{GOLD}  |
           \\  {YELLOW}██████████████████{GOLD}  /{RESET}
{BLUE}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈{RESET}
{WHITE}The Keeper speaks in a deep voice:
{CYAN}"I have been waiting... Another chest lies beyond."
"But only those who know the secret word may pass."
{YELLOW}"Speak the word, traveller..."{RESET}
"""

secret_unlock = f"""
{GOLD}
 ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ███╗   ██╗███████╗██╗  ██╗██╗   ██╗
 ██╔══██╗██╔══██╗██║╚██╗ ██╔╝██╔══██╗████╗  ██║██╔════╝██║  ██║██║   ██║
 ██████╔╝██████╔╝██║ ╚████╔╝ ███████║██╔██╗ ██║███████╗███████║██║   ██║
 ██╔═══╝ ██╔══██╗██║  ╚██╔╝  ██╔══██║██║╚██╗██║╚════██║██╔══██║██║   ██║
 ██║     ██║  ██║██║   ██║   ██║  ██║██║ ╚████║███████║██║  ██║╚██████╔╝
 ╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝{RESET}
{CYAN}
    ██╗███████╗    ████████╗██╗  ██╗███████╗    ██████╗ ███████╗███████╗████████╗██╗
    ██║██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║
    ██║███████╗       ██║   ███████║█████╗      ██████╔╝█████╗  ███████╗   ██║   ██║
    ██║╚════██║       ██║   ██╔══██║██╔══╝      ██╔══██╗██╔══╝  ╚════██║   ██║   ╚═╝
    ╚█████╔╝███████║  ██║   ██║  ██║███████╗    ██████╔╝███████╗███████║   ██║   ██╗
     ╚════╝ ╚══════╝  ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝{RESET}

{GOLD}  ╔══════════════════════════════════════════════════════════════╗
  ║{MAGENTA}  💎  THE ULTIMATE TREASURE HAS BEEN UNLOCKED, PRIYANSHU  💎 {GOLD} ║
  ║{GREEN}       Your destiny: BUILD THE FUTURE WITH YOUR HANDS        {GOLD}║
  ║{YELLOW}      You got 9999999999999 Gold Coin        {GOLD}║
  ╚══════════════════════════════════════════════════════════════╝{RESET}

{DIM}  The Keeper bows slowly and vanishes into the mist...{RESET}
"""


def run_keeper():
    print(keeper)
    word = input(">> ")
    if word.strip() == "Priyanshuisbest":
        print(secret_unlock)
    else:
        print(f"{RED}The Keeper shakes his head. 'That is not the word.'{RESET}")


if __name__ == "__main__":
    run_keeper()
