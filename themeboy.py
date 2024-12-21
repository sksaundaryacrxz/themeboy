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
