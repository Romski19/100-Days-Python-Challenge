board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

def get_row_col(position):
    if position[0] == "A":
        col = 0
        row = int(position[1]) - 1
        return row, col
    elif position[0] == "B":
        col = 1
        row = int(position[1]) - 1
        return row, col
    elif position[0] == "C":
        col = 2
        row = int(position[1]) - 1
        return row, col
get_row_col("A3")