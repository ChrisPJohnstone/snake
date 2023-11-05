import pygame


class Snake:
    DEFAULT_CONTROLS: dict[int, str] = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down",
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
    }
    DEFAULT_COLOR: str = "Blue"
    DEFAULT_STARTING_DIRECTION: str = "Right"
    DEFAULT_STARTING_X_POSITION: int = 0
    DEFAULT_STARTING_Y_POSITION: int = 0
    DEFAULT_STARTING_LENGTH: int = 3

    ILLEGAL_MOVES: dict[str, str] = [
        {
            "current": "up",
            "desired": "down",
        },
        {
            "current": "down",
            "desired": "up",
        },
        {
            "current": "left",
            "desired": "right",
        },
        {
            "current": "right",
            "desired": "left",
        }
    ]

    def __init__(
        self,
        block_width: int,
        block_height: int,
        color: str = None,
        starting_direction: str = None,
        starting_x_position: int = None,
        starting_y_position: int = None,
        starting_length: int = None,
    ) -> None:
        self.controls: dict[int, str] = Snake.DEFAULT_CONTROLS
        
        self.block_width: int = block_width
        self.block_height: int = block_height
        self.offsets: dict[str, dict[str, int]] = {
            "up": {"x": 0, "y": -self.block_height},
            "down": {"x": 0, "y": self.block_height},
            "left": {"x": -self.block_width, "y": 0},
            "right": {"x": self.block_width, "y": 0},
        }

        self.color: str = color
        self.starting_direction: str = starting_direction
        self.starting_x_position: int = starting_x_position
        self.starting_y_position: int = starting_y_position
        self.starting_length: int = starting_length
        self.move_to_start()

    @property
    def color(self) -> str:
        return self._color
      
    @color.setter
    def color(self, value: str) -> None:
        if value is None:
            self._color: str = Snake.DEFAULT_COLOR
        else:
            self._color: str = value

    @property
    def starting_direction(self) -> str:
        return self._starting_direction

    @starting_direction.setter
    def starting_direction(self, value: str) -> str:
        if value is None:
            self._starting_direction: str = Snake.DEFAULT_STARTING_DIRECTION
        else:
            self._starting_direction: str = value

    @property
    def starting_length(self) -> int:
        return self._starting_length
      
    @starting_length.setter
    def starting_length(self, value: int) -> None:
        if value is None:
            self._starting_length: int = Snake.DEFAULT_STARTING_LENGTH
        else:
            self._starting_length: int = value

    @property
    def starting_x_position(self) -> int:
        return self._starting_x_position
      
    @starting_x_position.setter
    def starting_x_position(self, value: int) -> None:
        if value is None:
            grid_reference: int = Snake.DEFAULT_STARTING_X_POSITION
        else:
            grid_reference: int = value
        self._starting_x_position: int = grid_reference * self.block_width

    @property
    def starting_y_position(self) -> int:
        return self._starting_y_position
      
    @starting_y_position.setter
    def starting_y_position(self, value: int) -> None:
        if value is None:
            grid_reference: int = Snake.DEFAULT_STARTING_Y_POSITION
        else:
            grid_reference: int = value
        self._starting_y_position: int = grid_reference * self.block_height

    def move_to_start(self) -> None:
        offset: dict[str, int] = self.offsets[self.starting_direction.lower()]
        self.body: list[dict[str, int]] = [
            {
                "x_position": self.starting_x_position + (block * offset["x"]),
                "y_position": self.starting_y_position + (block * offset["y"]),
            }
            for block in range(self.starting_length)
        ]
        self.direction: str = self.starting_direction
        self.length: int = self.starting_length

    def move(self) -> None:
        offset: dict[str, int] = self.offsets[self.direction.lower()]
        head: dict[str, int] = self.body[-1]
        next_block: dict[str, int] = {
            "x_position": head["x_position"] + offset["x"],
            "y_position": head["y_position"] + offset["y"],    
        }
        self.body.append(next_block)
        if len(self.body) > self.length:
            self.body.pop(0)

    def steer(self, direction: str) -> None:
        requested_move: dict[str, str] = {
            "current": self.direction,
            "desired": direction,
        }
        if requested_move not in Snake.ILLEGAL_MOVES:
            self.direction: str = direction

    def eat(self) -> None:
        self.length += 1

    def get_draw_args(self) -> dict[str, str | int]:
        base_args: dict[str, str | int] = {
            "color": self.color,
            "width": self.block_width - 1,
            "height": self.block_height - 1,
        }
        for block in self.body:
            yield base_args | block

    def get_score_args(self) -> dict[str, str | int]:
        score: int = self.length - self.starting_length
        return {
            "text": f"Score: {score}",
            "color": "white",
            "x_position": 0,
            "y_position": 0,
        }
