import math
from typing import List, Union

class Vector:
    def __init__(self, components: List[float]):
        self.components = components

    def length(self) -> float:
        return math.sqrt(sum(x * x for x in self.components))

    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        return Vector([x * scalar for x in self.components])

    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        return self * scalar

    def scalarProduct(self, other: 'Vector') -> float:
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны быть одной размерности.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def angleWith(self, other: 'Vector', degrees: bool = False) -> float:
        mag1 = self.length()
        mag2 = other.length()

        if mag1 == 0 or mag2 == 0:
            raise ValueError("Нельзя вычислить угол с нулевым вектором.")

        cosTheta = self.scalarProduct(other) / (mag1 * mag2)
        cosTheta = max(-1.0, min(1.0, cosTheta))

        angleRad = math.acos(cosTheta)
        return math.degrees(angleRad) if degrees else angleRad