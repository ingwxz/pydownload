from database.db import get_db_connection

class DownloadModel:
    @staticmethod
    def find_by_filname(filename):
        conn = get_db_connection()
        file = conn.execute('SELECT * FROM uploads WHERE filename = ?', (filename,)).fetchall
        conn.close()
        return file