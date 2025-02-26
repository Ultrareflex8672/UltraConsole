from application.menu_olusturucu import MenuSystem as MS
import sqlite3

class SqlProcess():
    def __init__(self, path=None):
        try:
            if path:
                self.path = path
                self.conn = sqlite3.connect(self.path)
                self.cursor = self.conn.cursor()
            else:
                MS.create_frame("Hata!", "Veri Tabanı Dosyası Yolu Eksik!", "info")
        except sqlite3.Error as e:
            print(f"Hata oluştu: {e}")

##################################################################################################################

    def sql_add_user(self, username, password, role, name, surname, email, tel):
        try:
            # Eğer tablo yoksa oluştur (opsiyonel güvenlik önlemi)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    role INTEGER,
                    name TEXT,
                    surname TEXT,
                    email TEXT,
                    tel TEXT
                )
            """)
            
            # Kullanıcı ekleme sorgusu (OR IGNORE sayesinde tekrar eden kayıt eklenmez)
            self.cursor.execute("""
                INSERT OR IGNORE INTO users (username, password, role, name, surname, email, tel)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (username, password, role, name, surname, email, tel))

            self.conn.commit()  # Değişiklikleri kaydet
            print(f"Kullanıcı eklendi veya zaten var: {username}")
        
        except sqlite3.Error as e:
            print(f"Hata oluştu: {e}")

##################################################################################################################

    def sql_read_users(self, username=None):
        if username:
            self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        else:
            self.cursor.execute("SELECT * FROM users")
        existing_user = self.cursor.fetchone()
        
        if existing_user:
            return existing_user
        else:
            return False

##################################################################################################################
    
    def is_user_table_exist(self, table_name):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = self.cursor.fetchone()
        if result:
            return True
        else: 
            return False
        
##################################################################################################################
        
    def sql_update_user(self, user_id, username, password, role, name, surname, email, tel):
        try:
            self.cursor.execute("""
                UPDATE users SET 
                    username = ?,
                    password = ?,
                    role = ?,
                    name = ?,
                    surname = ?,
                    email = ?,
                    tel = ?
                WHERE id = ?
            """, (username, password, role, name, surname, email, tel, user_id))

            self.conn.commit()  # Değişiklikleri kaydet
            print(f"Kullanıcı eklendi veya zaten var: {username}")
        
        except sqlite3.Error as e:
            print(f"Hata oluştu: {e}")
        
##################################################################################################################
        
    def conncls(self):
        self.conn.close()  # Bağlantıyı kapat

##################################################################################################################

    def sql_add_user2(self, username, password, role, name, surname, email, tel):
        try:
            user_info = (
            username,  # username
            password,      # password
            role,               # role (örneğin: 1 = admin, 2 = kullanıcı)
            name,         # name
            surname,      # surname
            email,  # email
            tel     # tel
        )

            # Kullanıcı ekleme sorgusu (OR IGNORE sayesinde tekrar eden kayıt eklenmez)
            self.cursor.execute("""
            INSERT INTO users (username, password, role, name, surname, email, tel)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, user_info)

            self.conn.commit()  # Değişiklikleri kaydet
            print(f"Kullanıcı eklendi veya zaten var: {username}")
        
        except sqlite3.Error as e:
            print(f"Hata oluştu: {e}")

##################################################################################################################
