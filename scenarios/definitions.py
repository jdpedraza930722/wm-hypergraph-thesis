from src.graph.binary_graph import BinaryGraph
from src.hypergraph.hyper_graph import HyperGraph
from src.memory.active_structure import ActiveStructure

def build_scenario_1_e1() -> tuple:
    """ E1: Juan estudia Matemáticas (Aridad 2) """
    entities = ["Juan", "Matemáticas"]
    
    # Binary
    bg = BinaryGraph()
    bg.add_binary_relation("Juan", "Matemáticas")
    
    # Hypergraph
    hg = HyperGraph()
    hg.add_hyperedge("Escena1", entities)
    
    return ActiveStructure(bg, "E1"), ActiveStructure(hg, "E1"), entities

def build_scenario_2_e2() -> tuple:
    """ E2: Juan estudia Matemáticas con un Profesor (Aridad 3) """
    entities = ["Juan", "Matemáticas", "Profesor"]
    
    bg = BinaryGraph()
    # Relaciones binarias independientes (clique para preservar toda la info por pares sin nodo central)
    bg.add_binary_relation("Juan", "Matemáticas")
    bg.add_binary_relation("Profesor", "Matemáticas")
    bg.add_binary_relation("Juan", "Profesor")
    
    hg = HyperGraph()
    hg.add_hyperedge("Escena2", entities)
    
    return ActiveStructure(bg, "E2"), ActiveStructure(hg, "E2"), entities

def build_scenario_3_e3() -> tuple:
    """ E3: Juan estudia Matemáticas con un Profesor en Aula 5 (Aridad 4) """
    entities = ["Juan", "Matemáticas", "Profesor", "Aula 5"]
    
    bg = BinaryGraph()
    # Fragmentación en todas las combinaciones posibles de pares
    for i in range(len(entities)):
        for j in range(i + 1, len(entities)):
            bg.add_binary_relation(entities[i], entities[j])
            
    hg = HyperGraph()
    hg.add_hyperedge("Escena3", entities)
    
    return ActiveStructure(bg, "E3"), ActiveStructure(hg, "E3"), entities

def build_scenario_4_e4() -> tuple:
    """ E4: Juan estudia Matemáticas con el Profesor García en Aula 5 usando Álgebra Moderna (Aridad 5) """
    entities = ["Juan", "Matemáticas", "Profesor García", "Aula 5", "Álgebra Moderna"]
    
    bg = BinaryGraph()
    # Fragmentación máxima en pares
    for i in range(len(entities)):
        for j in range(i + 1, len(entities)):
            bg.add_binary_relation(entities[i], entities[j])
            
    hg = HyperGraph()
    hg.add_hyperedge("Escena4", entities)
    
    return ActiveStructure(bg, "E4"), ActiveStructure(hg, "E4"), entities

def get_all_scenarios():
    return {
        "E1": build_scenario_1_e1,
        "E2": build_scenario_2_e2,
        "E3": build_scenario_3_e3,
        "E4": build_scenario_4_e4
    }
