"""
Módulo que define la Entidad base para las estructuras relacionales.
"""

class Entity:
    def __init__(self, name: str):
        self.name = name
        self.activation = 0.0

    def __repr__(self):
        return f"Entity({self.name}, act={self.activation:.4f})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.name == other.name
