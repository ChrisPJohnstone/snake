import random


class Food:
    DEFAULT_COLOR: str = "Red"

    def __init__(
        self,
        block_width: int,
        block_height: int,
        grid_width: int,
        grid_height: int,
        color: str = None,
    ) -> None:
        self.block_width: int = block_width
        self.block_height: int = block_height
        self.grid_width: int = grid_width
        self.grid_height: int = grid_height
        self.color: str = color
        self.move()

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        if value is None:
            self._color: str = Food.DEFAULT_COLOR
        else:
            self._color: str = value
    
    def move(self, prohibited_blocks: list[dict[str, int]] = None) -> None:
        if prohibited_blocks is None:
            prohibited_blocks: list[dict[str, int]] = []
        while True:
            x_grid_position: int = random.randint(0, self.grid_width - 1)
            y_grid_position: int = random.randint(0, self.grid_height - 1)
            position: dict[str, int] = {
                "x_position": self.block_width * x_grid_position,
                "y_position": self.block_height * y_grid_position,
            }
            if position not in prohibited_blocks:
                self.position: dict[str, int] = position
                break
    
    def get_draw_args(self) -> None:
        return {
            "color": self.color,
            "width": self.block_width - 1,
            "height": self.block_height - 1,
        } | self.position
