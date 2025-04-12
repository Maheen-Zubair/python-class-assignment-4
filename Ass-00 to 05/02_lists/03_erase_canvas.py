import tkinter as tk

CELL_SIZE = 40
ROWS = 10
COLS = 10

def create_cells(canvas):
    cells = []
    for row in range(ROWS):
        row_cells = []
        for col in range(COLS):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            cell = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
            row_cells.append(cell)
        cells.append(row_cells)
    return cells

def erase(event):
    eraser_x = event.x
    eraser_y = event.y

    # eraser ki size
    eraser_size = 40
    x1 = eraser_x - eraser_size // 2
    y1 = eraser_y - eraser_size // 2
    x2 = eraser_x + eraser_size // 2
    y2 = eraser_y + eraser_size // 2

    # check which rectangles overlap
    overlapping = canvas.find_overlapping(x1, y1, x2, y2)
    for item in overlapping:
        canvas.itemconfig(item, fill="white")

root = tk.Tk()
root.title("Canvas Eraser")

canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
canvas.pack()

cells = create_cells(canvas)

# bind mouse drag to erase function
canvas.bind("<B1-Motion>", erase)

root.mainloop()