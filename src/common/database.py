import sqlite3

class DataBase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER, timestamp INTEGER, method TEXT, target TEXT, port INTEGER, time TEXT)')
        self.conn.commit()

    def add_log(self, id, timestamp, method, target, port, time):
        self.cursor.execute('INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)', (id, timestamp, method, target, port, time))
        self.conn.commit()

    def get_logs(self):
        self.cursor.execute('SELECT * FROM logs')
        return self.cursor.fetchall()

    def get_log(self, id):
        self.cursor.execute('SELECT * FROM logs WHERE id = ?', (id,))
        return self.cursor.fetchone()

    def delete_log(self, id):
        self.cursor.execute('DELETE FROM logs WHERE id = ?', (id,))
        self.conn.commit()

    def delete_logs(self):
        self.cursor.execute('DELETE FROM logs')
        self.conn.commit()

    def __del__(self):
        self.conn.close()