class Config:
    DEFAULT_REFRESH_RATE: int = 100
    DEFAULT_SQUARE_WIDTH: int = 20
    DEFAULT_SQUARE_HEIGHT: int = 20
    DEFAULT_GRID_WIDTH: int = 15
    DEFAULT_GRID_HEIGHT: int = 15

    def __init__(
        self,
        refresh_rate: int = None,
        square_width: int = None,
        square_height: int = None,
        grid_width: int = None,
        grid_height: int = None,
    ) -> None:
        self.refresh_rate: int = refresh_rate
        self.square_width: int = square_width
        self.square_height: int = square_height
        self.grid_width: int = grid_width
        self.grid_height: int = grid_height
        
        self.window_bounds: tuple[int, int] = (
            self.square_width * self.grid_width,
            self.square_height * self.grid_height,
        )

    @property
    def refresh_rate(self) -> int:
        return self._refresh_rate
      
    @refresh_rate.setter
    def refresh_rate(self, value: int) -> None:
        if value is None:
            self._refresh_rate: int = Config.DEFAULT_REFRESH_RATE
        else:
            self._refresh_rate: int = value

    @property
    def square_width(self) -> int:
        return self._square_width
      
    @square_width.setter
    def square_width(self, value: int) -> None:
        if value is None:
            self._square_width: int = Config.DEFAULT_SQUARE_WIDTH
        else:
            self._square_width: int = value

    @property
    def square_height(self) -> int:
        return self._square_height
      
    @square_height.setter
    def square_height(self, value: int) -> None:
        if value is None:
            self._square_height: int = Config.DEFAULT_SQUARE_HEIGHT
        else:
            self._square_height: int = value

    @property
    def grid_width(self) -> int:
        return self._grid_width
      
    @grid_width.setter
    def grid_width(self, value: int) -> None:
        if value is None:
            self._grid_width: int = Config.DEFAULT_GRID_WIDTH
        else:
            self._grid_width: int = value

    @property
    def grid_height(self) -> int:
        return self._grid_height
      
    @grid_height.setter
    def grid_height(self, value: int) -> None:
        if value is None:
            self._grid_height: int = Config.DEFAULT_GRID_HEIGHT
        else:
            self._grid_height: int = value
