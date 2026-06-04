"""
Implementación del Grafo Binario Puro.
"""
from src.entities.entity import Entity

class BinaryGraph:
    def __init__(self):
        # Diccionario de adyacencia: Entity -> List[Entity]
        self.adjacency_list = {}
        # Mantenemos las entidades por nombre para facilitar el acceso
        self._entities_by_name = {}

    def add_entity(self, name: str):
        if name not in self._entities_by_name:
            entity = Entity(name)
            self._entities_by_name[name] = entity
            self.adjacency_list[entity] = []

    def get_entity(self, name: str) -> Entity:
        return self._entities_by_name.get(name)

    def add_binary_relation(self, name1: str, name2: str):
        """Añade una relación binaria no dirigida entre dos entidades."""
        self.add_entity(name1)
        self.add_entity(name2)
        
        e1 = self.get_entity(name1)
        e2 = self.get_entity(name2)
        
        if e2 not in self.adjacency_list[e1]:
            self.adjacency_list[e1].append(e2)
        if e1 not in self.adjacency_list[e2]:
            self.adjacency_list[e2].append(e1)

    def get_entities(self):
        return list(self.adjacency_list.keys())

    def get_neighbors(self, entity: Entity):
        return self.adjacency_list.get(entity, [])
