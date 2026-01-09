from abc import ABC, abstractmethod

# Абстрактный продукт
class Transport(ABC):
    @abstractmethod
    def deliver(self, destination):
        pass

# Конкретные продукты
class Truck(Transport):
    def deliver(self, destination):
        return f"Доставка грузовиком в {destination}"

class Ship(Transport):
    def deliver(self, destination):
        return f"Доставка кораблём в {destination}"

class Plane(Transport):
    def deliver(self, destination):
        return f"Доставка самолётом в {destination}"

# Абстрактная фабрика (Создатель)
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self, destination):
        # Делегируем создание объекта подклассу
        transport = self.create_transport()
        return transport.deliver(destination)

# Конкретные фабрики
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Plane()

# Демонстрация работы
if __name__ == "__main__":
    print("Планирование доставок:")

    road = RoadLogistics()
    print(road.plan_delivery("Санкт-Петербург"))

    sea = SeaLogistics()
    print(sea.plan_delivery("Новороссийск"))

    air = AirLogistics()
    print(air.plan_delivery("Пекин"))