import mysql.connector


class TariffDB:
    def __init__(self):
        self.database_connection = mysql.connector.connect(host='localhost', user='root', password='Ilyas2006#', database='vpn_bot')

    def get_tariffs(self):
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            query = "SELECT `id`, `name`, `price` FROM tariffs WHERE 1"

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()

    def get_one_tariff(self, tariff_id):
        try:
            self.database_connection.reconnect()

            cursor = self.database_connection.cursor()
            query = "SELECT * FROM tariffs WHERE `id` = %s"

            cursor.execute(query, (tariff_id,))

            return cursor.fetchall()[0]

        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()

    def get_price(self, tariff_id):
        try:
            self.database_connection.reconnect()
            cursor = self.database_connection.cursor()
            query = f"SELECT `price` FROM tariffs WHERE `id`= %s"

            cursor.execute(query, (tariff_id,))

            return cursor.fetchall()[0][0]

        except Exception as e:
            print("Ошибка при работе с MySQL", e)
        finally:
            cursor.close()


if __name__ == '__main__':
    tariff_db = TariffDB()
    print(tariff_db.get_one_tariff(1))
