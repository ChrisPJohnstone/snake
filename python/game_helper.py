import pygame


class GameHelper:
    COLORS: dict[str, tuple[int, int, int]] = {
        "black": (0, 0, 0),
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
        "white": (255, 255, 255),
    }

    def __init__(
        self,
        window_bounds: tuple[int, int],
        caption: str = None,
    ) -> None:
        pygame.init()
        self.window_bounds: tuple[int, int] = window_bounds
        self.window = pygame.display.set_mode(self.window_bounds)
        if caption is not None:
            pygame.display.set_caption(caption)
    
    def fill_window(self, color: str) -> None:
        self.window.fill(color)
      
    def draw_rectangle(
        self,
        color: str,
        x_position: int,
        y_position: int,
        width: int,
        height: int,
    ) -> None:
        pygame.draw.rect(
            surface=self.window,
            color=GameHelper._get_color(color),
            rect=(
                x_position,
                y_position,
                width,
                height,
            )
        )
        
    def draw_text(
        self,
        text: str,
        color: str,
        x_position: int,
        y_position: int,
    ) -> None:
        font = pygame.font.SysFont("comicsans", 20, True)
        text_image = font.render(text, True, GameHelper._get_color(color))
        self.window.blit(
            source=text_image,
            dest=(x_position, y_position),
        )

    def refresh_display(self) -> None:
        pygame.display.flip()
        
    def is_out_of_bounds(self, position: dict[str, int]) -> bool:
        if position["x_position"] > self.window_bounds[0]:
            return True
        elif position["x_position"] < 0:
            return True
        elif position["y_position"] > self.window_bounds[1]:
            return True
        elif position["y_position"] < 0:
            return True
        return False

    @staticmethod
    def _get_color(color: str) -> tuple[int, int, int]:
        if color.lower() not in GameHelper.COLORS:
            raise ValueError(color)
        return GameHelper.COLORS[color.lower()]