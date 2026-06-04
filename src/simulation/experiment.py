import json
import pandas as pd
from scenarios.definitions import get_all_scenarios
from src.memory.activation_engine import ActivationEngine
from src.metrics.evaluator import Evaluator

class Experiment:
    def __init__(self, iterations=100, seed=42):
        self.iterations = iterations
        self.seed = seed
        self.engine = ActivationEngine(decay_range=(0.85, 0.95), threshold=0.5)
        self.results = []
        self.json_dumps = []

    def run(self):
        import random
        random.seed(self.seed)
        
        scenarios = get_all_scenarios()
        
        for scene_name, builder_func in scenarios.items():
            for i in range(1, self.iterations + 1):
                decay = self.engine.get_random_decay()
                
                # Para evitar estados compartidos, reconstruimos en cada iteración
                bg_struct, hg_struct, original_entities = builder_func()
                
                # El estímulo siempre será "Juan" (el primer elemento en la lista original)
                stimulus = "Juan"
                
                # Evaluar Grafo Binario
                self._run_trial(scene_name, i, "BinaryGraph", bg_struct, original_entities, stimulus, decay)
                
                # Evaluar Hipergrafo
                self._run_trial(scene_name, i, "HyperGraph", hg_struct, original_entities, stimulus, decay)

    def _run_trial(self, scenario, iteration, model_name, active_struct, original_entities, stimulus, decay):
        self.engine.propagate(active_struct, stimulus, decay)
        recovered = self.engine.get_recovered_context(active_struct)
        
        precision = Evaluator.calculate_precision(recovered, original_entities)
        context = Evaluator.calculate_context_preservation(recovered, original_entities)
        fragmentation = Evaluator.calculate_fragmentation(context)
        
        self.results.append({
            "scenario": scenario,
            "iteration": iteration,
            "model": model_name,
            "precision": precision,
            "context": context,
            "fragmentation": fragmentation,
            "decay_applied": decay
        })
        
        # Guardar para JSON dump
        activations_dump = {e.name: e.activation for e in active_struct.get_topology().get_entities()}
        self.json_dumps.append({
            "scenario": scenario,
            "iteration": iteration,
            "model": model_name,
            "original_entities": original_entities,
            "recovered_entities": recovered,
            "activations": activations_dump,
            "metrics": {
                "precision": precision,
                "context": context,
                "fragmentation": fragmentation
            }
        })

    def save_results(self, output_dir="outputs"):
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Save CSV (Datos Crudos)
        df = pd.DataFrame(self.results)
        df.to_csv(os.path.join(output_dir, "results.csv"), index=False)
        
        # Generar Reporte Resumen (Promedios)
        summary_df = df.groupby(['scenario', 'model'])[['precision', 'context', 'fragmentation']].mean().reset_index()
        summary_df.to_csv(os.path.join(output_dir, "summary_stats.csv"), index=False)
        
        # Crear un reporte de texto legible para humanos
        with open(os.path.join(output_dir, "summary_report.txt"), "w", encoding="utf-8") as f:
            f.write("REPORTE ESTADÍSTICO PROMEDIO (100 Iteraciones)\n")
            f.write("==============================================\n\n")
            for scenario in ['E1', 'E2', 'E3', 'E4']:
                f.write(f"--- Escenario {scenario} ---\n")
                scenario_data = summary_df[summary_df['scenario'] == scenario]
                for _, row in scenario_data.iterrows():
                    f.write(f"Modelo: {row['model']}\n")
                    f.write(f"  - Precisión Inferencial:    {row['precision']:.4f}\n")
                    f.write(f"  - Preservación Contextual:  {row['context']:.4f}\n")
                    f.write(f"  - Fragmentación Relacional: {row['fragmentation']:.4f}\n")
                f.write("\n")

        # Save JSON
        with open(os.path.join(output_dir, "results.json"), "w", encoding="utf-8") as f:
            json.dump({
                "metadata": {
                    "seed": self.seed,
                    "iterations": self.iterations,
                    "threshold": self.engine.threshold
                },
                "trials": self.json_dumps
            }, f, indent=4, ensure_ascii=False)
        
        return df
