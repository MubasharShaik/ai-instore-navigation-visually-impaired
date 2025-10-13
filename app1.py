from flask import Flask, render_template, jsonify, redirect
import random

app = Flask(__name__)

# Maze and state configuration
maze_size = 5
user_position = [0, 0]
destination_position = [0, 0]
maze = [['' for _ in range(maze_size)] for _ in range(maze_size)]
path = []
product_reached = False
current_item = None  # Current selected item
maze_initialized = False

# List of items/products to place in the maze
items = ["Apple", "Banana", "Cherry", "Date", "Eggplant"]

@app.route('/')
def home():
    return render_template('home.html', items=items)

@app.route('/select/<int:item_id>', methods=['GET'])
def select_item(item_id):
    global destination_position, maze, path, product_reached, current_item, maze_initialized

    # Get the selected item
    selected_item = items[item_id]

    # Initialize the maze only once
    if not maze_initialized:
        maze, destination_position = generate_maze(selected_item)
        maze_initialized = True
    else:
        # Locate the destination for the newly selected item
        destination_position = find_item_position(selected_item)

    # Set the current item and reset the product_reached flag
    current_item = selected_item
    product_reached = False

    # Find the shortest path using BFS
    path = bfs(user_position, destination_position)

    return render_template(
        'navigate.html',
        maze=maze,
        user_position=user_position,
        destination_position=destination_position,
    )

def generate_maze(selected_item):
    global maze
    maze = [['' for _ in range(maze_size)] for _ in range(maze_size)]

    # Randomly assign items to the maze
    item_positions = random.sample(range(maze_size * maze_size), len(items))
    shuffled_items = items.copy()
    random.shuffle(shuffled_items)

    for i, pos in enumerate(item_positions):
        row, col = divmod(pos, maze_size)
        maze[row][col] = shuffled_items[i]

    # Set the destination position for the selected item
    dest_pos = item_positions[shuffled_items.index(selected_item)]
    dest_row, dest_col = divmod(dest_pos, maze_size)

    return maze, [dest_row, dest_col]

def find_item_position(item):
    for row in range(maze_size):
        for col in range(maze_size):
            if maze[row][col] == item:
                return [row, col]
    return None

def bfs(start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = [(start, [])]
    visited = set()
    visited.add(tuple(start))

    while queue:
        current_pos, path_taken = queue.pop(0)

        if current_pos == end:
            return path_taken + [end]

        for direction in directions:
            next_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]
            if (
                0 <= next_pos[0] < maze_size
                and 0 <= next_pos[1] < maze_size
                and tuple(next_pos) not in visited
            ):
                visited.add(tuple(next_pos))
                queue.append((next_pos, path_taken + [next_pos]))

    return []

@app.route('/move_user', methods=['GET'])
def move_user():
    global user_position, path, product_reached

    if path and not product_reached:
        next_position = path.pop(0)
        direction = get_direction(user_position, next_position)
        user_position[:] = next_position

        if user_position == destination_position:
            product_reached = True
            return jsonify(
                {
                    "status": "reached",
                    "user_position": user_position,
                    "instruction": "Product destination reached!",
                }
            )

        return jsonify(
            {
                "status": "moving",
                "user_position": user_position,
                "instruction": f"Go {direction}",
            }
        )

    return jsonify({"status": "waiting", "instruction": ""})

def get_direction(current, next_pos):
    row_diff, col_diff = next_pos[0] - current[0], next_pos[1] - current[1]
    if row_diff == 0 and col_diff == 1:
        return "right"
    elif row_diff == 1 and col_diff == 0:
        return "down"
    elif row_diff == 0 and col_diff == -1:
        return "left"
    elif row_diff == -1 and col_diff == 0:
        return "up"
    return ""

@app.route('/new_product', methods=['GET'])
def new_product():
    global current_item, product_reached, path

    # Reset only the current item and path but keep the maze and user position intact
    current_item = None
    product_reached = False
    path = []

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
