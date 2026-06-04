import random
from src.graph.binary_graph import BinaryGraph
from src.hypergraph.hyper_graph import HyperGraph

class ActivationEngine:
    def __init__(self, decay_range=(0.85, 0.95), threshold=0.5):
        self.decay_range = decay_range
        self.threshold = threshold

    def get_random_decay(self) -> float:
        return random.uniform(self.decay_range[0], self.decay_range[1])

    def propagate(self, active_structure, stimulus_name: str, decay: float):
        """
        Propaga la activación desde el estímulo a través de la topología.
        - Grafo Binario: Sufre el 'Fan Effect', la activación se divide por el grado de salida.
        - Hipergrafo: La activación fluye a la hiperarista y se distribuye preservando la fuerza,
          modelando la retención de un contexto holístico.
        """
        topology = active_structure.get_topology()
        entities = topology.get_entities()
        
        # Reiniciar activaciones
        for e in entities:
            e.activation = 0.0
            
        stimulus = topology.get_entity(stimulus_name)
        if not stimulus:
            return
            
        # Inyectar activación al estímulo
        stimulus.activation = 1.0
        
        # Diccionario para acumular las nuevas activaciones (propagación de 1 paso)
        # Esto modela la recuperación de memoria episódica desde una pista (cue)
        new_activations = {e: 0.0 for e in entities}
        new_activations[stimulus] = 1.0 # El estímulo retiene su activación
        
        if isinstance(topology, BinaryGraph):
            neighbors = topology.get_neighbors(stimulus)
            if neighbors:
                # Fan Effect: penalización por fragmentación de múltiples relaciones binarias independientes
                signal_per_neighbor = (stimulus.activation * decay) / len(neighbors)
                for neighbor in neighbors:
                    new_activations[neighbor] += signal_per_neighbor
                    
        elif isinstance(topology, HyperGraph):
            hyperedges = topology.get_hyperedges_for_entity(stimulus)
            if hyperedges:
                # Grado de salida hacia hiperaristas (usualmente 1 por escena episódica)
                signal_per_hyperedge = (stimulus.activation * decay) / len(hyperedges)
                for he in hyperedges:
                    other_nodes = [n for n in he.entities if n != stimulus]
                    for n in other_nodes:
                        # La hiperarista vincula el contexto completo sin penalización combinatoria
                        new_activations[n] += signal_per_hyperedge

        # Actualizar las activaciones finales en las entidades
        for e in entities:
            e.activation = new_activations[e]

    def get_recovered_context(self, active_structure):
        """Devuelve las entidades cuya activación superó el umbral."""
        topology = active_structure.get_topology()
        recovered = []
        for e in topology.get_entities():
            if e.activation >= self.threshold:
                recovered.append(e.name)
        return recovered
