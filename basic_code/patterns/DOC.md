# Square Pattern Generator
[source code](circle.py)

This Python script generates a square pattern of asterisks (`*`) based on a specified size. The pattern is printed to the console.

## Overview

The script defines a variable `size` which determines the dimensions of the square pattern. It then uses a loop to print a square grid of asterisks.

## Code Explanation

- `size = 5`: This line sets the size of the square pattern. The pattern will be a 5x5 grid of asterisks.

- The commented-out section of the code provides an alternative method to generate the pattern using nested loops:
  - The outer loop iterates over each row.
  - The inner loop iterates over each column within a row, printing an asterisk without a newline (`end=""`).
  - After completing a row, `print()` is called to move to the next line.

- The active section of the code uses a more concise method:
  - `for i in range(0, size):`: This loop iterates `size` times, once for each row.
  - `print("*" * size)`: This line prints a row of asterisks. The expression `"*" * size` creates a string of `size` asterisks.

## Usage

To use this script, simply run it in a Python environment. You can modify the `size` variable to change the dimensions of the square pattern.

## Example Output

For `size = 5`, the output will be:


# Function Documentation: `draw_circle_pattern`

## Purpose
The `draw_circle_pattern` function generates an ASCII art representation of a circle using asterisks (`*`). It prints the pattern directly to the console, approximating a circle based on a specified radius.

## Parameters
- **`radius`** (int): The radius of the circle to be drawn. This determines the size of the circle and the grid used for drawing.

## Description
The function calculates the diameter of the circle based on the given radius and iterates over a grid of size `(diameter + 1) x (diameter + 1)`. For each point `(x, y)` in the grid, it calculates the Euclidean distance from the center of the grid `(radius, radius)`. If this distance is approximately equal to the radius, an asterisk is printed; otherwise, a space is printed. This creates the visual effect of a circle.

## Implementation Details
1. **Grid Calculation**: The grid size is determined by the diameter of the circle, which is `2 * radius`. The iteration includes `diameter + 1` to ensure the right and bottom edges are covered.

2. **Distance Calculation**: The distance from the center `(radius, radius)` to each point `(x, y)` is calculated using the formula:
   \[______________
   \text{distance} = \sqrt{(x - \text{radius})^2 + (y - \text{radius})^2}
   \]

3. **Printing Condition**: An asterisk is printed if the calculated distance falls within the range `radius - 0.5 < distance < radius + 0.5`. This range helps in smoothing the circle's outline.

4. **Output**: The function prints the circle pattern directly to the console, line by line.

## Example Usage
```python
draw_circle_pattern(10)
```