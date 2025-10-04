class TargetIncome:

    TAX_FREE = 12750

    def __init__(self, target:float):
        self._original_target = self._current_target = target

    def current(self) -> float:
        return self._current_target

    def original(self) -> float:
        return self._original_target

    def current_with_tax(self) -> float:
        return (self._current_target - self.TAX_FREE) * 1.25 + self.TAX_FREE

    def current_percent_of_original(self) -> float:
        return round((self._current_target / self._original_target) * 100, 2)