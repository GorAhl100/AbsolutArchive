import sqlite3
from typing import List, Tuple
from bottle import Bottle


class BottleManager:
    def __init__(self, db_name="bottles.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def add_bottle(self, bottle: Bottle):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO bottles (name, volume, date, quality, price, notes)
                       VALUES (?, ?, ?, ?, ?, ?)
                       """, (bottle.name, bottle.volume, bottle.date, bottle.quality, bottle.price, bottle.notes))

        bottle.id = cursor.lastrowid

        conn.commit()
        conn.close()

        print(f"Flaskan har lagts till i databasen med ID {bottle.id} och namn {bottle.name}\n")

    def delete_bottle(self):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            bottle_id = int(input("Ange ID på flaskan som ska tas bort: "))
            cursor.execute("SELECT * FROM bottles WHERE id = ?", (bottle_id,))
            row = cursor.fetchone()
            if row:
                cursor.execute("DELETE FROM bottles WHERE id = ?", (bottle_id,))
                conn.commit()
                print(f"Flaska = {row[1]}, ID {bottle_id} har tagits bort.\n")
            else:
                print("Ingen flaska med det ID hittades.\n")
        except ValueError:
            print("Ogiltig inmatning, ange ett heltal.\n")

        conn.close()

    def get_all_bottles(self) -> List[Bottle]:
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bottles")
        rows = cursor.fetchall()
        conn.close()

        return [Bottle.from_row(row) for row in rows]
