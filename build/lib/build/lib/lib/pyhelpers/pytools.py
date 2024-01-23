import os
import shutil

history_folder = "C:/Users/glenj/AppData/Roaming/Code/User/History/"


def clear_history_folder():
    for path, _, _ in os.walk(history_folder):
        shutil.rmtree(path)
