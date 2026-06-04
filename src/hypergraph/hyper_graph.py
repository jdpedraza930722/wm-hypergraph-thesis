"""
Implementación del Hipergrafo.
"""
from src.entities.entity import Entity

class HyperEdge:
    def __init__(self, name: str):
        self.name = name
        self.entities = set()

    def add_entity(self, entity: Entity):
        self.entities.add(entity)

    def __repr__(self):
        return f"HyperEdge({self.name}, size={len(self.entities)})"

class HyperGraph:
    def __init__(self):
        self._entities_by_name = {}
        self.hyperedges = []

    def add_entity(self, name: str) -> Entity:
        if name not in self._entities_by_name:
            self._entities_by_name[name] = Entity(name)
        return self._entities_by_name[name]

    def get_entity(self, name: str) -> Entity:
        return self._entities_by_name.get(name)

    def add_hyperedge(self, edge_name: str, entity_names: list):
        """Crea una hiperarista que agrupa múltiples entidades."""
        hyperedge = HyperEdge(edge_name)
        for name in entity_names:
            ent = self.add_entity(name)
            hyperedge.add_entity(ent)
        self.hyperedges.append(hyperedge)

    def get_entities(self):
        return list(self._entities_by_name.values())

    def get_hyperedges_for_entity(self, entity: Entity):
        return [he for he in self.hyperedges if entity in he.entities]
