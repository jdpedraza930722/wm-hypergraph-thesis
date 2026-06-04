class Evaluator:
    @staticmethod
    def calculate_precision(recovered: list, original: list) -> float:
        """
        Precisión Inferencial (P)
        P = |Recuperado ∩ Original| / |Original|
        """
        if not original:
            return 0.0
        intersection = set(recovered).intersection(set(original))
        return len(intersection) / len(original)

    @staticmethod
    def calculate_context_preservation(recovered: list, original: list) -> float:
        """
        Preservación Contextual (C)
        C = 1 si se recupera el contexto completo y no existen ambigüedades. C = 0 en otro caso.
        """
        if set(recovered) == set(original):
            return 1.0
        return 0.0

    @staticmethod
    def calculate_fragmentation(context_preservation: float) -> float:
        """
        Fragmentación (F)
        F = 1 - C
        """
        return 1.0 - context_preservation
