class Database:
    """Интерфейс."""
    def query(self, sql):
        raise NotImplementedError

class RealDatabase(Database):
    """Реальная база данных."""
    def query(self, sql):
        print(f"[RealDatabase] Выполняю запрос: {sql}")

class DatabaseProxy(Database):
    """Прокси с проверкой доступа."""
    def __init__(self, has_access):
        self._has_access = has_access
        self._real_db = RealDatabase()

    def query(self, sql):
        if self._has_access:
            print("[Proxy] Доступ разрешён")
            self._real_db.query(sql)
        else:
            print("[Proxy] Доступ запрещён! Запрос не будет выполнен.")

if __name__ == "__main__":
    print("=== PROXY ===")
    user_db = DatabaseProxy(has_access=False)
    admin_db = DatabaseProxy(has_access=True)

    user_db.query("SELECT * FROM users")
    admin_db.query("SELECT * FROM users")