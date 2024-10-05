import sqlite3

# Agar jadval mavjud bo'lmasa, uni yaratish funksiyasi
def jadvalni_yarat(connection, jadval_nomi):
    cursor = connection.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {jadval_nomi} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            video_url TEXT NOT NULL
        );
    ''')
    connection.commit()

# Ma'lumotlarni jadvalga qo'shish funksiyasi
def malumotni_kirit(name, video_url, jadval_nomi='abdurahman'):
    try:
        # SQLite bazasiga ulanish
        connection = sqlite3.connect('quran_audio.db')
        cursor = connection.cursor()

        # Jadval borligini tekshirish va bo'lmasa yaratish
        jadvalni_yarat(connection, jadval_nomi)

        # Ma'lumotlarni jadvalga qo'shish
        sqlite_insert_query = f"""INSERT INTO {jadval_nomi} (name, video_url) VALUES (?, ?);"""
        cursor.execute(sqlite_insert_query, (name, video_url))
        connection.commit()

        print("Ma'lumotlar muvaffaqiyatli qo'shildi")

    except sqlite3.Error as error:
        print("Ma'lumotlarni qo'shishda xatolik yuz berdi")
        print("Xato turi: ", type(error))
        print("Xato: ", error)

    finally:
        if connection:
            connection.close()
            print("SQLite ulanishi yopildi")

# Misol uchun foydalanish
name = input('ism: ')
video_url = input('url: ')
malumotni_kirit(name, video_url)