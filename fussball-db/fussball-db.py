#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:54:24 2025

@author: snow
"""
import sqlite3
import csv
import tkinter as tk
from tkinter import filedialog

# Definition of a class which handles the database
class DB():
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.max_id = 0

        try:
            self.cursor.execute("SELECT * FROM spiele")
        except:
            self.init_tables()
        self.determine_max_id()
        self.data = []


    def init_tables(self):
        self.cursor = self.connection.cursor()

        # Eine Tabelle erstellen
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS spiele
                   (id INTEGER PRIMARY KEY,
                    season TEXT NOT NULL,
                    league INTEGER,
                    game_day INTEGER,
                    home TEXT NOT NULL, 
                    away TEXT NOT NULL,
                    home_goal INTEGER,
                    away_goal INTEGER)''')

        self.connection.commit()


    def determine_max_id(self):
        self.cursor.execute("select max(id) from spiele")
        rows = self.cursor.fetchall()
        if rows[0][0] == None: 
            self.max_id = 0
        else:
            self.max_id += rows[0][0]


    def get_max_id(self):
        return self.max_id

    def get_next_id(self):
        self.max_id += 1
        return self.max_id


    def read_data_from_file(self):
        file_path = open_file_dialog()
        csv_data = open(file_path, 'r')
        reader = csv.reader(csv_data, delimiter=',')
        next(reader) #Skip the header line
        self.data = []

        for zeile in reader:
            self.data.append(zeile)
            
        csv_data.close()
        return self.data


    def add_to_db(self):
        for list_entry in self.data:
            new_entry= (self.get_next_id(),  #ID
                        list_entry[0],       #Season
                        list_entry[1],       #League
                        list_entry[2],       #Game Day
                        list_entry[3],       #Home
                        list_entry[4],       #Away
                        list_entry[5],       #Goal home
                        list_entry[6],       #Gaol away
                        )
            self.cursor.execute("INSERT INTO spiele (id, season, league, game_day, home, away, home_goal, away_goal) VALUES (?, ?, ?, ?, ? ,? ,? ,?)", new_entry)
        
        self.connection.commit()


    def read_data_from_db(self):
        self.cursor.execute("SELECT * FROM spiele")

        # Alle Datensätze abrufen
        data = self.cursor.fetchall()
        return data

    def show_raw_data(self):
        print(self.data)

    def quit_programm(self):
        self.connection.close



def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hauptfenster ausblenden
    file_path = filedialog.askopenfilename(filetypes=[("CSV-Dateien", "*.csv"), ("Text-Dateien", "*.txt"), ("Alle Dateien", "*.*")])
    print("Ausgewählte Datei:", file_path)
    return file_path    



if __name__ == "__main__":

    # Initialisiert die Datenbank 
    db = DB("fussball-db.db")
    
    # Main loop 
    choice = 0
    while choice < 9:
        print("Welcome to the German Football Database")
        print("=======================================")
        print("")
        print("Menu")
        print("1. Add Data")
        print("2. Show data")
        print("9. Quit program")
        print()
        choice = int(input("Please Select:"))
        
        if choice == 1:
            db.read_data_from_file()
            db.add_to_db()
            

        if choice == 2:
            print(db.read_data_from_db())
            
    
    
    

    # Close the database
    db.quit_programm()
    
