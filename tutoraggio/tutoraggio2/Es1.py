class CEnemy:
    def __init__(self, energy, damage, defense) -> None:
        self.energy: int = energy
        self.damage: int = damage
        self.defense: int = defense


class CReplicants(CEnemy):
    def __init__(self, energy, damage, defense, mechanical_systems, mechanical_system_damage):
        super().__init__(energy, damage, defense)
        self.mechanical_systems = mechanical_systems
        self.mechanical_system_damage = mechanical_system_damage


class CCyberHackers(CEnemy):
    def __init__(self, energy, damage, defense, ram, hacking_damage):
        super().__init__(energy, damage, defense)
        self.ram = ram
        self.hacking_damage = hacking_damage
