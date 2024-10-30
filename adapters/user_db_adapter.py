import mysql.connector


class UserDB:
    def __init__(self):
        self.database_connection = mysql.connector.connect(host='localhost', user='root', password='Ilyas2006#', database='vpn_bot')

    def create_user(self, user_id, username):
        self.database_connection.reconnect()

        cursor = self.database_connection.cursor()
        query = "INSERT INTO users (user_id, username) VALUES (%s, %s)"

        cursor.execute(query, (user_id, username))

        self.database_connection.commit()
        print('User added successfully!')

        cursor.close()


if __name__ == '__main__':
    user_db = UserDB()
    user_db.create_user(23421234,'sdfwe1231')