Set Up a Scheduled Task

1. Configure the path to the folder containing the images in themeboy.py (wallpaper_folder)
2. Adjust the period after which new wallpaper will be set (time.sleep(60 * 60)  # Wait for 1 hour (60 * 60 seconds))
3. Press Win + S, search for Task Scheduler, and open it.
4. In the Task Scheduler window, click Create Basic Task on the right.
5. Name the task (e.g., "Change Wallpaper on Startup").
6. Choose When I log on as the trigger.
7. Select Start a program as the action.
8. Browse to the Python executable (e.g., C:\Python\Python39\pythonw.exe) as the program/script.
9. Add the path to your Python script (e.g., C:\Scripts\change_wallpaper.py) in the Add arguments field.
10. Complete the setup and save the task.
11. Adjust the power settings for the task as per preference (e.g., disable startup on AC only - this is default setting and will not allow the task to start if the computer is running on battery)
