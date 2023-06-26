import logging
import sqlite3

def main():
    logging.basicConfig(level=logging.INFO)
    connection = sqlite3.connect('application.db')
    try:
        cursor = connection.cursor()
        cursor.execute('select * from blogs')
        logging.info(cursor.fetchall())
    finally:
        logging.info('Closing connection')
        connection.close()

if __name__ == '__main__':
    main()