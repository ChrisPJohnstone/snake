import pygame

from _config import Config
from food import Food
from game_helper import GameHelper
from snake import Snake


def handler() -> None:
    config: Config = Config(
        refresh_rate=40,
        grid_width=30,
        grid_height=30,
    )
    game_helper: GameHelper = GameHelper(config.window_bounds, "Snake")
    snake: Snake = Snake(
        color="blue",
        block_width=config.square_width,
        block_height=config.square_height,
    )
    food: Food = Food(
        color="red",
        block_height=config.square_height,
        block_width=config.square_width,
        grid_width=config.grid_width,
        grid_height=config.grid_height,
    )

    run: bool = True
    while run:
        pygame.time.delay(config.refresh_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run: bool = False
            
            keys = pygame.key.get_pressed()
            for key, direction in snake.controls.items():
                if keys[key]:
                    snake.steer(direction)
                    break

        game_helper.fill_window("black")
        if snake.body[-1] in snake.body[:-1]:
            snake.move_to_start()
        elif game_helper.is_out_of_bounds(snake.body[-1]):
            snake.move_to_start()
        snake.move()

        if snake.body[-1] == food.position:
            snake.eat()
            food.move(snake.body)

        game_helper.draw_text(**snake.get_score_args())
        for rectangle_args in snake.get_draw_args():
            game_helper.draw_rectangle(**rectangle_args)
        game_helper.draw_rectangle(**food.get_draw_args())
        game_helper.refresh_display()


if __name__ == "__main__":
    handler()
