import shutil
import os

def moveDirectory(name):
    shutil.move("C:/Users/Monir/Downloads/google.csv", "C:/Users/Monir/Documents/pyGuiAutomation/files/CSV Files")
    os.rename("C:/Users/Monir/Documents/pyGuiAutomation/files/CSV Files/google.csv", f"C:/Users/Monir/Documents/pyGuiAutomation/files/CSV Files/{name}.csv")

moveDirectory("plumber")