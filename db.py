import sqlite3

#def get_connetion():
#   global __connection
#  if __connection is None:
#     __connection = sqlite3.connect('anketa.db')
# return __connection


# Создадим потоко-безопасное подклбчение

def ensure_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('anketa.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res
    return inner


@ensure_connection
def init_db(conn, force: bool = False):
    '''Проверить что нужные таблицы существуют
        Иначе создать их по новой
        :param force пересоздаст таблицы независимо от их статуса
    '''


    c = conn.cursor()

    # Information about user
    # TODO: create if will be necessary

    # Сообщения от пользовтелей
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
                CREATE TABLE IF NOT EXISTS user_message (
                id          INTEGER PRIMARY KEY,
                user_id     INTEGER NOT NULL,
                text        TEXT NOT NULL,
                is_ready INTEGER NOT NULL default 0
                )
    ''')

    # Save changes
    conn.commit()


@ensure_connection
def add_message(conn, user_id: int, text: str):
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text) VALUES (?, ?)', (user_id, text))
    conn.commit()

@ensure_connection
def change_status(conn, user_id: int, text: str, member: int):
    #ONLY VALUES 0 AND 1 ARE ACCEPTED AS MEMEBER BOOL PARAMETER
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text, is_ready) VALUES (?, ?, ?)', (user_id, text, member))
    conn.commit()

@ensure_connection
def count_messages(conn, user_id: int):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM user_message WHERE user_id = ?", (user_id,))
    (res,) = c.fetchone()
    # Commit не нужене потому что мы ничего не меняем в базе, мы только из нее читаем
    # conn.commit()
    return res


@ensure_connection
def list_messages(conn, user_id: int, limit: int = 10):
    c = conn.cursor()
    c.execute('SELECT id, text FROM user_message WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id, limit))
    # Упрощаем код
    return c.fetchall()


@ensure_connection
def check_club(conn):
    c = conn.cursor()
    c.execute('SELECT id, user_id FROM user_message WHERE is_ready = 1')
    return c.fetchall()

#if __name__ == "__main__":
#  init_db()
#
#  add_message(user_id=123, text="kekeus solved")
#
#  r = count_messages(user_id=123)

#  print(r)

  #  h = list_messages(user_id=123, limit=3)
   # for i in h:
   #     print(i)
