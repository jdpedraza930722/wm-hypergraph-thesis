"""
Módulo principal (Punto de entrada).
Orquesta la ejecución de la simulación, guarda los resultados y genera las gráficas.
"""
import os
from src.simulation.experiment import Experiment
from src.visualization.plotter import Plotter

def main():
    print("Iniciando simulación experimental: Memoria de Trabajo (Hipergrafos vs Grafos Binarios)")
    print("--------------------------------------------------------------------------------")
    
    # Configuración de reproducibilidad y parámetros
    SEED = 42
    ITERATIONS = 100
    
    print(f"-> Semilla configurada: {SEED}")
    print(f"-> Iteraciones por escenario: {ITERATIONS}")
    
    # 1. Ejecutar experimento
    print("\n[1/3] Ejecutando iteraciones del experimento...")
    exp = Experiment(iterations=ITERATIONS, seed=SEED)
    exp.run()
    
    # 2. Guardar resultados (CSV, JSON)
    print("[2/3] Guardando datos en outputs/ ...")
    df = exp.save_results(output_dir="outputs")
    print("      - results.csv y results.json generados exitosamente.")
    
    # 3. Generar gráficas
    print("[3/3] Generando gráficas comparativas...")
    plotter = Plotter(df, output_dir="outputs")
    plotter.plot_all()
    print("      - Gráficas PNG generadas exitosamente.")
    
    print("\n--------------------------------------------------------------------------------")
    print("Simulación completada. Los resultados se encuentran en la carpeta 'outputs/'.")

if __name__ == "__main__":
    main()
