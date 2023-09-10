# rubiks-cube

<img src="https://github.com/PrajasW/rubiks-cube/blob/master/pattern.gif" > </img>

Create animations like this using this notebook,
```python
from cube import Cube3x3

cube = Cube3x3()
moves = "U’ L’ U’ F’ R2 B’ R F U B2 U B’ L U’ F U R F’"
cube.move(moves,print_moves=False,threeD=True,save=True,save_dir="moves")
```
Use this to create the animation using the images of the moves.
