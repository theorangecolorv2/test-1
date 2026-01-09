class SortingStrategy:
    """Базовый класс стратегии."""
    def sort(self, data):
        raise NotImplementedError

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        # Сортировка пузырьком
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("Сортировка пузырьком")
        return arr

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        # Быстрая сортировка (встроенная)
        print("Быстрая сортировка")
        return sorted(data)

class Sorter:
    """Контекст."""
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

if __name__ == "__main__":
    print("=== STRATEGY ===")
    data = [5, 3, 8, 4, 2]
    
    sorter = Sorter(BubbleSortStrategy())
    print("Результат:", sorter.sort(data))

    sorter.set_strategy(QuickSortStrategy())
    print("Результат с другой стратегией:", sorter.sort(data))