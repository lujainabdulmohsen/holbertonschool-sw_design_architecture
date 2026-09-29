#!/usr/bin/env python3
"""Decorator design pattern example."""

from abc import ABC, abstractmethod


class Beverage(ABC):
    """Base beverage interface."""

    @abstractmethod
    def cost(self):
        """Return beverage cost."""

    @abstractmethod
    def description(self):
        """Return beverage description."""


class Coffee(Beverage):
    """Basic coffee."""

    def cost(self):
        """Return coffee cost."""
        return 50

    def description(self):
        """Return coffee description."""
        return "Coffee"


class BeverageDecorator(Beverage):
    """Base beverage decorator."""

    def __init__(self, inner):
        """Initialize decorator."""
        self._inner = inner


class MilkDecorator(BeverageDecorator):
    """Add milk."""

    def cost(self):
        """Return cost with milk."""
        return self._inner.cost() + 10

    def description(self):
        """Return description with milk."""
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    """Add sugar."""

    def cost(self):
        """Return cost with sugar."""
        return self._inner.cost() + 5

    def description(self):
        """Return description with sugar."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    """Add caramel."""

    def cost(self):
        """Return cost with caramel."""
        return self._inner.cost() + 15

    def description(self):
        """Return description with caramel."""
        return self._inner.description() + " + caramel"


def main():
    """Run decorator examples."""
    drink1 = MilkDecorator(Coffee())
    print(drink1.description(), drink1.cost())

    drink2 = MilkDecorator(SugarDecorator(Coffee()))
    print(drink2.description(), drink2.cost())

    drink3 = CaramelDecorator(
        MilkDecorator(SugarDecorator(Coffee()))
    )
    print(drink3.description(), drink3.cost())


if __name__ == "__main__":
    main()
