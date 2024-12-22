"""
ctypes.windll.user32:Accesses the user32 DLL, which contains user-interface-related Windows API functions.
SystemParametersInfoW:The SystemParametersInfo function is used to query or set system-wide parameters. The W suffix indicates this is the wide-character (Unicode) version of the function.
Parameters of SystemParametersInfoW:

BOOL SystemParametersInfoW(
    UINT  uiAction,
    UINT  uiParam,
    PVOID pvParam,
    UINT  fWinIni
);

Each parameter in your line corresponds to one of these:
20 (uiAction):This specifies the action to perform. 20 corresponds to SPI_SETDESKWALLPAPER, which sets the desktop wallpaper.
0 (uiParam): This is unused for the SPI_SETDESKWALLPAPER action, so it’s set to 0.
selected_wallpaper (pvParam):A pointer to the path of the image file (as a string) that will be set as the wallpaper. In Python, this string is passed directly.
3 (fWinIni):A combination of flags:
SPIF_UPDATEINIFILE (0x01): Updates the user profile in the registry with the new wallpaper path.
SPIF_SENDCHANGE (0x02): Sends a WM_SETTINGCHANGE message to all windows to notify them of the change.
The value 3 is a combination of these flags (0x01 | 0x02).
"""


import os
import random
import ctypes
import time

def change_wallpaper():
    # Path to the folder containing your wallpapers
    wallpaper_folder = r"C:\Users\saund\Pictures\Spotlight"
    
    # Get a list of all files in the folder
    wallpapers = [os.path.join(wallpaper_folder, f) for f in os.listdir(wallpaper_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    if not wallpapers:
        print("No wallpapers found in the folder.")
        return
    
    # Choose a random wallpaper
    selected_wallpaper = random.choice(wallpapers)
    
    # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, selected_wallpaper, 3)
    print(f"Wallpaper set to: {selected_wallpaper}")

if __name__ == "__main__":
    while True:
        change_wallpaper()
        print("Waiting 1 hour for the next change...")
        time.sleep(60 * 60)  # Wait for 1 hour (60 * 60 seconds)
