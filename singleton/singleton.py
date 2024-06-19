class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self, connection_string):
        if not hasattr(self, 'initialized'):
            self.connection_string = connection_string
            self.connection = self.connect_to_database()
            self.initialized = True

    def connect_to_database(self):
        # Логика подключения к базе данных
        return f"Connected to database with {self.connection_string}"

    def execute_query(self, query):
        # Логика выполнения запроса
        return f"Executing: {query}"


# Использование паттерна Одиночка
if __name__ == "__main__":
    db1 = DatabaseConnection("DatabaseURL1")
    db2 = DatabaseConnection("DatabaseURL2")

    print(db1.connection)  # Вывод: Connected to database with DatabaseURL1
    print(db2.connection)  # Вывод: Connected to database with DatabaseURL1

    print(db1.execute_query("SELECT * FROM users"))  # Вывод: Executing: SELECT * FROM users
    print(db2.execute_query("SELECT * FROM products"))  # Вывод: Executing: SELECT * FROM products

    # Проверка того, что db1 и db2 действительно один и тот же объект
    print(db1 is db2)  # Вывод: True