# Line chart helper
from dataclasses import dataclass
from typing import Sequence

@dataclass
class LineChart:
    title: str
    points: Sequence[tuple[float, float]]

    def y_range(self) -> tuple[float, float]:
        ys = [p[1] for p in self.points]
        return (min(ys), max(ys))
