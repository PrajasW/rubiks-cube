from cube import Cube3x3

cube = Cube3x3()
moves = "U’ L’ U’ F’ R2 B’ R F U B2 U B’ L U’ F U R F’"
cube.move(moves,print_moves=False,threeD=True,save=True,save_dir="moves")
cube.print_3d()