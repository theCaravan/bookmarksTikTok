#!/usr/bin/python3

import os
import random
import webbrowser

TXT_FILE = "_bookmarks.txt"
BOOKMARKS = []

def open_bookmarks(bookmarks):

    # Set the directory of the current script location
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open(TXT_FILE, "r", encoding = "utf-8") as fr:
        for line in fr.readlines():
            BOOKMARKS.append(line.strip())
        fr.close()

    random.shuffle(bookmarks)
    total_bookmarks = len(bookmarks)
    
    for i, bookmark in enumerate(bookmarks):
        print(f"Opening bookmark {i + 1:02}/{total_bookmarks:02}: {bookmark.split('/')[-1]}")
        webbrowser.open(bookmark)
        
        user_input = input("Press Enter to open the next bookmark, or 'n' to exit: ")
        if user_input.lower() == 'n':
            print("Exiting...")
            break

def main():
    try:
        open_bookmarks(BOOKMARKS)
    
    except Exception as e:
        print(repr(e))
        input("Press Enter to exit")

if __name__ == "__main__":
    main()