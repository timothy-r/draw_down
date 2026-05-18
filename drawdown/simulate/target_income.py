from drawdown.source.money import Money
class TargetIncome:

    TAX_FREE = 12750

    def __init__(self, target:Money):
        self._original_target = self._current_target = target

    def current(self) -> Money:
        return self._current_target

    def original(self) -> Money:
        return self._original_target

    def current_with_tax(self) -> float:
        return (self._current_target - self.TAX_FREE) * 1.25 + self.TAX_FREE

    def current_percent_of_original(self) -> float:
        return round((self._current_target / self._original_target) * 100, 2)