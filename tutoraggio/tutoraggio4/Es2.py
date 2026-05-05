from abc import ABC, abstractmethod


class CEnemy (ABC):
    """Abstratct class for enemies"""

    @abstractmethod
    def make_damage(self) -> int:
        """Create damage"""
        pass

    @abstractmethod
    def damage(self, punti_vita):
        """Recieve the health points"""
        pass
