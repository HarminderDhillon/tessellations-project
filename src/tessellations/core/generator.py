"""Core functionality for generating tessellation patterns."""
from pathlib import Path
from typing import Literal, Tuple

import numpy as np
from PIL import Image, ImageDraw

PatternType = Literal["triangular", "square", "hexagonal"]
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

class TessellationGenerator:
    """Generator for tessellation patterns."""
    
    def __init__(self, size: int = 800, line_width: int = 2):
        """
        Initialize the tessellation generator.
        
        Args:
            size: Width and height of the output image in pixels
            line_width: Width of the lines in the tessellation
        """
        self.size = size
        self.line_width = line_width
    
    def generate(
        self, 
        pattern_type: PatternType, 
        output_path: Path
    ) -> Path:
        """
        Generate a tessellation pattern and save it to the output path.
        
        Args:
            pattern_type: Type of tessellation pattern
            output_path: Directory to save the generated image
            
        Returns:
            Path to the generated image
        """
        # Create a blank white image
        image = Image.new("RGB", (self.size, self.size), COLOR_WHITE)
        draw = ImageDraw.Draw(image)
        
        # Generate the pattern
        if pattern_type == "triangular":
            self._draw_triangular_pattern(draw)
        elif pattern_type == "square":
            self._draw_square_pattern(draw)
        elif pattern_type == "hexagonal":
            self._draw_hexagonal_pattern(draw)
        else:
            raise ValueError(f"Unknown pattern type: {pattern_type}")
        
        # Ensure the output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save the image
        image.save(output_path)
        return output_path
    
    def _draw_triangular_pattern(self, draw: ImageDraw.Draw) -> None:
        """Draw a triangular tessellation pattern."""
        cell_size = self.size // 10
        
        # Draw horizontal lines
        for i in range(0, self.size + 1, cell_size):
            draw.line([(0, i), (self.size, i)], fill=COLOR_BLACK, width=self.line_width)
        
        # Draw diagonal lines (/)
        for i in range(-self.size, self.size + 1, cell_size):
            draw.line([(0, i + self.size), (self.size, i)], fill=COLOR_BLACK, width=self.line_width)
        
        # Draw diagonal lines (\)
        for i in range(-self.size, self.size + 1, cell_size):
            draw.line([(0, i), (self.size, i + self.size)], fill=COLOR_BLACK, width=self.line_width)
    
    def _draw_square_pattern(self, draw: ImageDraw.Draw) -> None:
        """Draw a square tessellation pattern."""
        cell_size = self.size // 10
        
        # Draw horizontal lines
        for i in range(0, self.size + 1, cell_size):
            draw.line([(0, i), (self.size, i)], fill=COLOR_BLACK, width=self.line_width)
        
        # Draw vertical lines
        for i in range(0, self.size + 1, cell_size):
            draw.line([(i, 0), (i, self.size)], fill=COLOR_BLACK, width=self.line_width)
    
    def _draw_hexagonal_pattern(self, draw: ImageDraw.Draw) -> None:
        """Draw a hexagonal tessellation pattern."""
        # Hexagon parameters
        hex_size = self.size // 10
        h = hex_size
        r = hex_size  # Distance from center to corner
        
        # Calculate row and column spacing
        row_height = int(3 * h / 2)
        col_width = int(np.sqrt(3) * r)
        
        # Calculate number of rows and columns needed
        num_rows = self.size // row_height + 2
        num_cols = self.size // col_width + 2
        
        # Draw hexagons
        for row in range(num_rows):
            for col in range(num_cols):
                # Calculate center position
                cx = int(col * col_width + (row % 2) * col_width / 2)
                cy = int(row * row_height)
                
                # Draw hexagon
                self._draw_hexagon(draw, cx, cy, r)
    
    def _draw_hexagon(self, draw: ImageDraw.Draw, cx: int, cy: int, r: int) -> None:
        """Draw a single hexagon."""
        vertices = []
        for i in range(6):
            angle_rad = np.pi / 3 * i
            x = cx + int(r * np.cos(angle_rad))
            y = cy + int(r * np.sin(angle_rad))
            vertices.append((x, y))
        
        # Draw the hexagon
        draw.polygon(vertices, outline=COLOR_BLACK, width=self.line_width)