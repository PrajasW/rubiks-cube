import tkinter as tk
from colors import RED, BLUE, GREEN, YELLOW, ORANGE, WHITE
# Create a 3D tensor data (6, 3, 3)
tensor_data = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ],
    [
        [28, 29, 30],
        [31, 32, 33],
        [34, 35, 36]
    ],
    [
        [37, 38, 39],
        [40, 41, 42],
        [43, 44, 45]
    ],
    [
        [46, 47, 48],
        [49, 50, 51],
        [52, 53, 54]
    ]
]

# Create the main window
root = tk.Tk()
root.title("Tensor Cube Visualization")

# Create a canvas to draw the cube
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Define the size of the cube
cube_size = 50

# Calculate the cube positions and draw the cube
for x in range(6):
    for y in range(3):
        for z in range(3):
            value = tensor_data[x][y][z]
            color = "#%02x%02x%02x" % (value, value, value)
            canvas.create_rectangle(
                x * cube_size, y * cube_size,
                (x + 1) * cube_size, (y + 1) * cube_size,
                fill=color, outline="black"
            )

# Run the Tkinter main loop
root.mainloop()
