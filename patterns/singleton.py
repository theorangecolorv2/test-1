class DatabaseConnection:
    """Класс для управления подключением к базе данных (Singleton)."""
    _instance = None  # Хранит единственный экземпляр

    def __new__(cls):
        # Если экземпляра нет, создаем его
        if cls._instance is None:
            print("Создание нового подключения к базе данных...")
            cls._instance = super().__new__(cls)
            cls._instance.connection_string = "postgresql://localhost:5432/mydb"
        return cls._instance

    def query(self, sql):
        return f"Выполнение запроса '{sql}' через {self.connection_string}"

# Демонстрация работы
if __name__ == "__main__":
    # Первое обращение - создается объект
    db1 = DatabaseConnection()
    print(f"db1 ID: {id(db1)}")
    print(db1.query("SELECT * FROM users") + "\n")

    # Второе обращение - возвращается тот же самый объект
    db2 = DatabaseConnection()
    print(f"db2 ID: {id(db2)}")
    print(db2.query("INSERT INTO users VALUES (1, 'John')") + "\n")

    # Проверка идентичности
    print(f"db1 и db2 - это один объект?: {db1 is db2}")