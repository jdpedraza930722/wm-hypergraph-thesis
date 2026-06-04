import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import os

class Plotter:
    def __init__(self, df: pd.DataFrame, output_dir="outputs"):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def plot_all(self):
        self.plot_metric("precision", "Precisión Promedio por Escenario", "Precisión")
        self.plot_metric("context", "Preservación Contextual Promedio", "Preservación Contextual")
        self.plot_metric("fragmentation", "Fragmentación Promedio", "Fragmentación")

    def plot_metric(self, metric_name: str, title: str, ylabel: str):
        # Crear copia para traducir los modelos al español para la leyenda
        df_plot = self.df.copy()
        df_plot['model'] = df_plot['model'].replace({
            'BinaryGraph': 'Grafo Binario',
            'HyperGraph': 'Hipergrafo'
        })
        
        # Agrupar por escenario y modelo
        grouped = df_plot.groupby(['scenario', 'model'])[metric_name].mean().unstack()
        
        # El orden de los escenarios debe ser E1, E2, E3, E4
        grouped = grouped.reindex(['E1', 'E2', 'E3', 'E4'])
        
        fig, ax = plt.subplots(figsize=(8, 6))
        grouped.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e'])
        
        ax.set_title(title, fontsize=14)
        ax.set_xlabel("Escenario (Complejidad Creciente)", fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12)
        ax.set_ylim(0, 1.05)
        ax.legend(title="Modelo de Representación")

        
        plt.tight_layout()
        filename = f"{metric_name}_comparison.png"
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.close(fig)
