import tkinter as tk
from algorithms import bfs,ucs,greedy,a_star
from tkinter import simpledialog
from tkinter import messagebox
import random
import time
from utils import manhattan, euclidean

cell_size = 30

rows = 0
cols = 0

start = None
goal = None

grid = []
rectangles = []

window = tk.Tk()
window.title("Pathfinding Visualizer")
window.geometry("1000x700")
window.resizable(True, True)


left_frame = tk.Frame(window)
right_frame = tk.Frame(window)
left_frame.pack(side="left", padx=10, pady=10)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

heuristic_choice = tk.StringVar()
heuristic_choice.set("Manhattan")

rows = simpledialog.askinteger(
    "Grid Size",
    "Enter Number of Rows:"
)

cols = simpledialog.askinteger(
    "Grid Size",
    "Enter Number of Columns:"
)

if rows is None or cols is None:

    messagebox.showerror(
        "Error",
        "Grid Size is Required."
    )

    window.destroy()
    exit()

for row in range(rows):

    grid_row = []

    for col in range(cols):

        grid_row.append(0)

    grid.append(grid_row)

canvas = tk.Canvas(
    left_frame,
    width=cols * cell_size,
    height=rows * cell_size,
    bg="white"
)

canvas.pack()

def draw_grid():

    for row in range(rows):

        rectangle_row = []

        for col in range(cols):

            x1 = col * cell_size
            y1 = row * cell_size

            x2 = x1 + cell_size
            y2 = y1 + cell_size

            rectangle = canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill="white",
                outline="gray"
            )

            rectangle_row.append(rectangle)

        rectangles.append(rectangle_row)


def cell_clicked(event):

    global start
    global goal

    row = event.y // cell_size
    col = event.x // cell_size

    if row >= rows or col >= cols:
        return

    if start is None:

        start = (row, col)

        canvas.itemconfig(
            rectangles[row][col],
            fill="green"
        )

        print("Start Node:", start)

        return

    if goal is None:

        if (row, col) == start:
            return

        goal = (row, col)

        canvas.itemconfig(
            rectangles[row][col],
            fill="red"
        )

        print("Goal Node:", goal)

        return

    if (row, col) == start or (row, col) == goal:
        return

    if grid[row][col] == 0:

        grid[row][col] = 1

        canvas.itemconfig(
            rectangles[row][col],
            fill="black"
        )

    else:

        grid[row][col] = 0

        canvas.itemconfig(
            rectangles[row][col],
            fill="white"
        )


def generate_maze():

    if start is None or goal is None:

        messagebox.showerror(
            "Error",
            "Please Select Start and Goal First."
        )

        return

    density = simpledialog.askinteger(
        "Maze",
        "Enter Obstacle Density (0-100):"
    )

    if density is None:
        return

    if density < 0 or density > 100:

        messagebox.showerror(
            "Error",
            "Density Must Be Between 0 and 100."
        )

        return

    for row in range(rows):

        for col in range(cols):

            if (row, col) == start or (row, col) == goal:
                continue

            chance = random.randint(1, 100)

            if chance <= density:

                grid[row][col] = 1

                canvas.itemconfig(
                    rectangles[row][col],
                    fill="black"
                )

            else:

                grid[row][col] = 0

                canvas.itemconfig(
                    rectangles[row][col],
                    fill="white"
                )


def run_bfs():

    if start is None or goal is None:

        messagebox.showerror(
            "Error",
            "Please Select Start and Goal First."
        )

        return

    start_time = time.perf_counter()

    path, visited, frontier = bfs(grid, start, goal)

    end_time = time.perf_counter()

    execution_time = round(
        (end_time - start_time) * 1000,
        2
    )

    if path is None:

        messagebox.showinfo(
            "BFS",
            "No Path Found"
        )

        return

    path_cost = len(path) - 1

    # Draw Frontier Nodes => Yellow
    for row, col in frontier:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="yellow"
            )

            window.update()
            window.after(20)

    # Draw Visited Nodes => Blue
    for row, col in visited:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="lightblue"
            )

            window.update()
            window.after(50)

    # Draw Final Path => Green
    for row, col in path:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="green"
            )

            window.update()
            window.after(100)

    stats_label.config(
        text=
        "Algorithm : BFS\n\n"
        "Nodes Explored : " + str(len(visited)) +
        "\n\nPath Length : " + str(len(path)) +
        "\n\nPath Cost : " + str(path_cost) +
        "\n\nExecution Time : " + str(execution_time) + " ms"
    )



def run_ucs():

    if start is None or goal is None:

        messagebox.showerror(
            "Error",
            "Please Select Start and Goal First."
        )

        return

    start_time = time.perf_counter()

    path, visited, frontier = ucs(grid, start, goal)

    end_time = time.perf_counter()

    execution_time = round(
        (end_time - start_time) * 1000,
        2
    )

    if path is None:

        messagebox.showinfo(
            "UCS",
            "No Path Found"
        )

        return

    path_cost = len(path) - 1

    # Draw Frontier Nodes (Yellow)
    for row, col in frontier:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="yellow"
            )

            window.update()
            window.after(20)

    # Draw Visited Nodes (Blue)
    for row, col in visited:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="lightblue"
            )

            window.update()
            window.after(50)

    # Draw Final Path (Green)
    for row, col in path:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="green"
            )

            window.update()
            window.after(100)

    stats_label.config(
        text=
        "Algorithm : UCS\n\n"
        "Nodes Explored : " + str(len(visited)) +
        "\n\nPath Length : " + str(len(path)) +
        "\n\nPath Cost : " + str(path_cost) +
        "\n\nExecution Time : " + str(execution_time) + " ms"
    )
            

def run_greedy():

    if start is None or goal is None:

        messagebox.showerror(
            "Error",
            "Please Select Start and Goal First."
        )

        return

    if heuristic_choice.get() == "Manhattan":

        heuristic = manhattan

    else:

        heuristic = euclidean

    start_time = time.perf_counter()

    path, visited, frontier = greedy(
        grid,
        start,
        goal,
        heuristic
    )

    end_time = time.perf_counter()

    execution_time = round(
        (end_time - start_time) * 1000,
        2
    )

    if path is None:

        messagebox.showinfo(
            "Greedy",
            "No Path Found"
        )

        return

    path_cost = len(path) - 1

    # Draw Frontier Nodes (Yellow)
    for row, col in frontier:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="yellow"
            )

            window.update()
            window.after(20)

    # Draw Visited Nodes (Blue)
    for row, col in visited:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="lightblue"
            )

            window.update()
            window.after(50)

    # Draw Final Path (Green)
    for row, col in path:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="green"
            )

            window.update()
            window.after(100)

    stats_label.config(
        text=
        "Algorithm : Greedy\n\n"
        "Nodes Explored : " + str(len(visited)) +
        "\n\nPath Length : " + str(len(path)) +
        "\n\nPath Cost : " + str(path_cost) +
        "\n\nExecution Time : " + str(execution_time) + " ms"
    )

def run_a_star():

    if start is None or goal is None:

        messagebox.showerror(
            "Error",
            "Please Select Start and Goal First."
        )

        return

    if heuristic_choice.get() == "Manhattan":

        heuristic = manhattan

    else:

        heuristic = euclidean

    start_time = time.perf_counter()

    path, visited, frontier = a_star(
        grid,
        start,
        goal,
        heuristic
    )

    end_time = time.perf_counter()

    execution_time = round(
        (end_time - start_time) * 1000,
        2
    )

    if path is None:

        messagebox.showinfo(
            "A*",
            "No Path Found"
        )

        return

    path_cost = len(path) - 1

    # Draw Frontier Nodes (Yellow)
    for row, col in frontier:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="yellow"
            )

            window.update()
            window.after(20)

    # Draw Visited Nodes (Blue)
    for row, col in visited:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="lightblue"
            )

            window.update()
            window.after(50)

    # Draw Final Path (Green)
    for row, col in path:

        if (row, col) != start and (row, col) != goal:

            canvas.itemconfig(
                rectangles[row][col],
                fill="green"
            )

            window.update()
            window.after(100)

    stats_label.config(
        text=
        "Algorithm : A*\n\n"
        "Nodes Explored : " + str(len(visited)) +
        "\n\nPath Length : " + str(len(path)) +
        "\n\nPath Cost : " + str(path_cost) +
        "\n\nExecution Time : " + str(execution_time) + " ms"
    )
            
def reset_search():

    for row in range(rows):

        for col in range(cols):

            if (row, col) == start:

                canvas.itemconfig(
                    rectangles[row][col],
                    fill="green"
                )

            elif (row, col) == goal:

                canvas.itemconfig(
                    rectangles[row][col],
                    fill="red"
                )

            elif grid[row][col] == 1:

                canvas.itemconfig(
                    rectangles[row][col],
                    fill="black"
                )

            else:

                canvas.itemconfig(
                    rectangles[row][col],
                    fill="white"
                )
def clear_grid():

    global start
    global goal

    start = None
    goal = None

    for row in range(rows):

        for col in range(cols):

            grid[row][col] = 0

            canvas.itemconfig(
                rectangles[row][col],
                fill="white"
            )
draw_grid()



canvas.bind(
    "<Button-1>",
    cell_clicked
)


#Maze Controls
maze_button = tk.Button(
    right_frame,
    text="Generate Maze",
    command=generate_maze,
    width=20
)

maze_button.pack(pady=3)

clear_button = tk.Button(
    right_frame,
    text="Clear Grid",
    command=clear_grid,
    width=20
)

clear_button.pack(pady=3)


#Heuristic Selection
heuristic_label = tk.Label(
    right_frame,
    text="Select Heuristic"
)

heuristic_label.pack(pady=(10, 3))

manhattan_button = tk.Radiobutton(
    right_frame,
    text="Manhattan",
    variable=heuristic_choice,
    value="Manhattan",
    width=20,
    anchor="w"
)

manhattan_button.pack(pady=3)

euclidean_button = tk.Radiobutton(
    right_frame,
    text="Euclidean",
    variable=heuristic_choice,
    value="Euclidean",
    width=20,
    anchor="w"
)

euclidean_button.pack(pady=3)


#Search Algorithms
bfs_button = tk.Button(
    right_frame,
    text="Run BFS",
    command=run_bfs,
    width=20
)

bfs_button.pack(pady=(10, 3))

ucs_button = tk.Button(
    right_frame,
    text="Run UCS",
    command=run_ucs,
    width=20
)

ucs_button.pack(pady=3)

greedy_button = tk.Button(
    right_frame,
    text="Run Greedy",
    command=run_greedy,
    width=20
)

greedy_button.pack(pady=3)

a_star_button = tk.Button(
    right_frame,
    text="Run A*",
    command=run_a_star,
    width=20
)

a_star_button.pack(pady=3)


#Reset
reset_button = tk.Button(
    right_frame,
    text="Reset Search",
    command=reset_search,
    width=20
)

reset_button.pack(pady=(10, 3))


#Statistics
stats_label = tk.Label(
    right_frame,
    text="Run Any Algorithm",
    justify="left",
    font=("Arial", 10)
)

stats_label.pack(pady=(15, 5))

window.mainloop()
