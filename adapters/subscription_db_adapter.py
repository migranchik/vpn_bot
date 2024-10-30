import mysql.connector
import datetime


class SubscriptionDB:
    def __init__(self):
        self.database_connection = mysql.connector.connect(host='localhost', user='root', password='Ilyas2006#', database='vpn_bot')

    def add_subscription(self, user_id, end_time, vpn_key):
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            query = "INSERT INTO subscriptions (user_id, end_time, vpn_key) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, end_time, vpn_key))
            self.database_connection.commit()

        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()

    def extend_subscription(self, user_id, end_time):
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            query = "UPDATE subscriptions SET end_time = %s WHERE user_id = %s"
            cursor.execute(query, (end_time, user_id))
            self.database_connection.commit()

        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()

    def get_all(self):
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            query = "SELECT * FROM subscriptions"

            cursor.execute(query)

            return cursor.fetchall()
        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()

    def get_user_subscription(self, user_id) -> datetime.date:
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            query = "SELECT * FROM subscriptions WHERE user_id = %s"

            cursor.execute(query, (user_id,))
            response = cursor.fetchall()

            return response[0][2]

        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()

    def get_user_vpn_key(self, user_id) -> datetime.date:
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            query = "SELECT * FROM subscriptions WHERE user_id = %s"

            cursor.execute(query, (user_id,))
            response = cursor.fetchall()

            return response[0][3]

        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()

    def delete_user(self, user_id):
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            delete_query = "DELETE FROM subscriptions WHERE user_id = %s"

            cursor.execute(delete_query, (user_id,))
            self.database_connection.commit()

            return cursor.fetchall()
        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()


if __name__ == '__main__':
    subscription_db = SubscriptionDB()
    print(type(subscription_db.get_user_vpn_key(874477006)))
