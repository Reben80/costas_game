## Costas Game

A simple Python grid game using Pygame library. In this game, players place points on an n x m grid. The game is inspired by the [Costas array](https://en.wikipedia.org/wiki/Costas_array) problem. The game is terminated when one of the following conditions is met:

1. A point is placed outside the grid.
2. A point is placed at the same location as another point.
3. Two points are placed on the same row.
4. Two points are placed on the same column.
5. Two line segments share the same slope.
### Installation

To run this game, you need to install Pygame library. You can install it using pip:


```pip install pygame```
## Usage

To start the game, simply run the `ostas_game.py` file:

```python grid_game.py```

## Game Rules

1. Click on the grid to place a point.
2. If any of the termination conditions are met, the game will display an appropriate message, and the game will end.

# Screenshots
<img width="399" alt="Screenshot 2023-03-20 at 10 53 38 PM" src="https://user-images.githubusercontent.com/41596499/226758658-53bf7fe9-2b48-4dbc-9fcd-a0ba268c4993.png">

Grid Game Screenshot

#
### License

[MIT](https://choosealicense.com/licenses/mit/)
