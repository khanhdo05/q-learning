class Grid:
    def __init__(self, rows, cols, value = 0):
        self.rows = rows
        self.cols = cols
        self.grid = [[value for _ in range(cols)] for _ in range(rows)]
        
    def is_out_of_bounds(self, r, c):
        return r < 0 or r >= self.rows or c < 0 or c >= self.cols
        
    def print_grid(self):
        # Determine the maximum width needed for each column
        widths = [max(len(str(item)) for item in col) for col in zip(*self.grid)]

        # Print the top border
        row_separator = f'+{"".join("-" * (width + 2) + "+" for width in widths)}'
        print(row_separator)

        for row in self.grid:
            # Print the row content
            row_str = '|'
            for i, item in enumerate(row):
                # Use f-strings for aligned formatting
                row_str += f' {str(item).ljust(widths[i])} |'
            print(row_str)
            # Print the separator after each row
            print(row_separator)