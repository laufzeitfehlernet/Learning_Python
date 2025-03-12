#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 07:30:02 2025

@author: snow

https://de.ittrip.xyz/python/python-file-dialog
"""

import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hauptfenster ausblenden
    file_path = filedialog.askopenfilename(filetypes=[("CSV-Dateien", "*.csv"), ("Text-Dateien", "*.txt"), ("Alle Dateien", "*.*")])
    print("Ausgewählte Datei:", file_path)
    return file_path                                                                                   
                                                                                   
def open_file(file_path):
    file = open(file_path)
    for line in file:
        print(line.rstrip())
    file.close()
    

if __name__ == "__main__":
    open_file(open_file_dialog())





