"""
Definición de la Estructura Relacional Activa (ER).
"""
import datetime

class ActiveStructure:
    def __init__(self, topology, context: str):
        """
        Inicializa la Estructura Relacional Activa.
        
        Args:
            topology: Grafo Binario o Hipergrafo.
            context: Referencia contextual de la escena (ej. "Escenario 1").
        """
        self.topology = topology
        self.context = context
        self.timestamp = datetime.datetime.now().isoformat()

    @property
    def entities(self):
        """Retorna la lista de entidades en la estructura."""
        return self.topology.get_entities()

    def get_topology(self):
        return self.topology
