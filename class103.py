import os
import time
import shutil
import random
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir = "C:/Users/Madhu K/Desktop/NIhar"
todir = "C:/Users/Madhu K/Desktop/PYTHON/New folder"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value :
                file_name = os.path.basename(event.src.path)
                print("Downloaded"+ file_name)
                path1 = fromdir + '/' + file_name
                path2 = todir + '/' + key
                path3 = todir + '/' +  key + '/' + file_name
                
                if os.path.exists(path2):
                    print("Directory exists")
                    print("Moving File"+ file_name)
                    shutil.move(path1,path3)
                    time.sleep(2)
                     
                else : 
                    print("Making Directory")
                    os.makedirs(path2)
                    print("Moving File"+ file_name)
                    shutil.move(path1,path3)
                    time.sleep(2)
                    
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,fromdir,recursive = True)
observer.start()
try : 
    time.sleep(2)
    print("Running")
except  KeyboardInterrupt : 
    print("Stopped")
    observer.stop()