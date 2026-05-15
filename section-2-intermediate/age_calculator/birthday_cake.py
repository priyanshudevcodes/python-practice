import time
import sys
import random

# --- ANSI Color Codes for the Terminal ---
COLORS = {
    "red": "\033[91m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "cyan": "\033[96m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "reset": "\033[0m",
    "bold": "\033[1m"
}

# A list of colors for the rainbow text effect
RAINBOW = [COLORS["red"], COLORS["yellow"], COLORS["green"], 
           COLORS["cyan"], COLORS["blue"], COLORS["magenta"]]

def rainbow_print(text, delay=0.03):
    """
    Prints text letter by letter in random colors for a festive effect.
    """
    for char in text:
        # Ignore spaces for color application to keep it clean
        if char == " ":
            sys.stdout.write(char)
        else:
            color = random.choice(RAINBOW)
            sys.stdout.write(f"{COLORS['bold']}{color}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    print() # Move to the next line when done

def print_cake():
    """
    Prints a large, multi-colored ASCII birthday cake.
    """
    c_flame = COLORS["yellow"]
    c_candle = COLORS["red"]
    c_frosting = COLORS["cyan"]
    c_cake = COLORS["magenta"]
    c_decor = COLORS["green"]
    reset = COLORS["reset"]
    bold = COLORS["bold"]

    cake = f"""
               {bold}{c_flame}  ( )   ( )   ( )   ( ){reset}
               {bold}{c_candle}  _|_   _|_   _|_   _|_{reset}
               {c_candle} |___| |___| |___| |___|{reset}
               {c_frosting} ~~~~~~~~~~~~~~~~~~~~~~~{reset}
             {c_cake}_{c_frosting}~~~~~~~~~~~~~~~~~~~~~~~~~{c_cake}_{reset}
            {c_cake}|{c_decor} : . : . : . : . : . : . : {c_cake}|{reset}
            {c_cake}|{c_decor} . : . : . : . : . : . : . {c_cake}|{reset}
            {c_cake}|{reset}{bold}{COLORS['yellow']}* * * * * * * * * * * * * *{reset}{c_cake}|{reset}
            {c_cake}|{c_decor} : . : . : . : . : . : . : {c_cake}|{reset}
            {c_cake}|{c_decor} . : . : . : . : . : . : . {c_cake}|{reset}
            {c_frosting}==============================={reset}
    """
    print(cake)

def celebrate(name="Awesome Friend"):
    """
    The main function to trigger the colorful birthday animation.
    """
    print("\n")
    rainbow_print("Mixing the batter...", delay=0.05)
    time.sleep(0.5)
    rainbow_print("Baking a spectacular cake...", delay=0.05)
    time.sleep(0.5)
    rainbow_print("Lighting the candles... Make a wish!\n", delay=0.05)
    time.sleep(1)
    
    # Reveal the colorful cake
    print_cake()
    
    # Format and display the customized birthday message
    message = f"!!! HAPPY BIRTHDAY, {name.upper()} !!!"
    
    print(" " * 4, end="")
    rainbow_print("*" * len(message), delay=0.01)
    
    print(" " * 4, end="")
    rainbow_print(message, delay=0.08) # Slower delay for the main message
    
    print(" " * 4, end="")
    rainbow_print("*" * len(message), delay=0.01)
    
    print("\n")
    rainbow_print("  Wishing you a year filled with joy, vibrant moments, and bug-free code!", delay=0.04)
    print("\n")

# If you run this file directly, it will test the function
if __name__ == "__main__":
    celebrate("Python Coder")