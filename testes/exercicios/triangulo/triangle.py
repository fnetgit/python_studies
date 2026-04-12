class Triangle:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def is_triangle(self) -> bool:
        return (
            self.x + self.y > self.z
            and self.x + self.z > self.y
            and self.y + self.z > self.x
        )

    def triangle_type(self) -> str:
        if not self.is_triangle():
            return "Não é triângulo"

        if self.x == self.y == self.z:
            return "Equilátero"
        if self.x == self.y or self.x == self.z or self.y == self.z:
            return "Isósceles"
        return "Escaleno"
