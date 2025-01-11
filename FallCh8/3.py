import sqlite3

# Создание класса для представления альбома
class Album:
    def __init__(self, album_id, title, artist_id):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"

# Функция для подключения к базе данных
def get_connection(db_file):
    return sqlite3.connect(db_file)

# CRUD операции для альбомов

# 1. Создание (Create)
def create_album(connection, title, artist_id):
    cursor = connection.cursor()
    insert_artist_query = '''
    INSERT INTO Album (Title,ArtistId) VALUES (?,?)
    '''
    cursor.execute(insert_artist_query,(title,artist_id))
    connection.commit()

# 2. Чтение (Read)
def read_albums(connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT *
        FROM Album     
        ''')
    a = cursor.fetchall()
    return [Album(album_id, title, artist_id) for album_id, title, artist_id in a]


# 3. Обновление (Update)
def update_album(connection, album_id, new_title):
    cursor = connection.cursor()
    update_artist_query = '''
    UPDATE Album
    SET Title = ?
    WHERE AlbumId = ?
    '''
    cursor.execute(update_artist_query,(new_title,album_id))
    connection.commit()


# 4. Удаление (Delete)
def delete_album(connection, album_id):
    cursor = connection.cursor()
    delete_album_query = '''
            DELETE FROM Album WHERE AlbumId = ?
            '''
    cursor.execute(delete_album_query, (album_id,))
    connection.commit()


def test():
    conn = get_connection('Chinook_Sqlite.sqlite')

    artist_id = 1
    album_title = "Тест1"

    create_album(conn, album_title, artist_id)

    albums = read_albums(conn)
    print("Список альбомов:")
    for album in albums:
        print(album)

    if albums != None:
        album_id = albums[0].album_id
        new_title = "Обновленный Альбом"
        update_album(conn, album_id, new_title)
        print(f"Альбом с ID {album_id} обновлен.")

        updated_albums = read_albums(conn)
        print("Список альбомов после обновления:")
        for album in updated_albums:
            print(album)

    if albums != None:
        delete_album(conn, album_id)
        print(f"Альбом с ID {album_id} удален.")

    final_albums = read_albums(conn)
    print("Список альбомов после удаления:")
    for album in final_albums:
        print(album)
    conn.close()

test()