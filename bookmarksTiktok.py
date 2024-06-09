#!/usr/bin/python3

import random
import webbrowser

TXT_FILE = "_bookmarks.txt"
BOOKMARKS = []

with open(TXT_FILE, "r", encoding = "utf-8") as fr:
    for line in fr.readlines():
        BOOKMARKS.append(line.strip())
    fr.close()

def open_bookmarks(bookmarks):
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
    if BOOKMARKS:
        open_bookmarks(BOOKMARKS)
    else:
        print("No bookmarks found.")

if __name__ == "__main__":
    main()
