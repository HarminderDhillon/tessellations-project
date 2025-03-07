"""SVG generator for tessellation patterns."""
from pathlib import Path
from typing import List, Literal, Tuple, Union
import math

PatternType = Literal["triangular", "square", "hexagonal"]

class SVGTessellationGenerator:
    """Generator for SVG tessellation patterns."""
    
    def __init__(self, size: int = 800, line_width: float = 1.0, stroke_color: str = "#000000"):
        """
        Initialize the SVG tessellation generator.
        
        Args:
            size: Width and height of the output image in pixels
            line_width: Width of the lines in the tessellation
            stroke_color: Color of the lines in the tessellation
        """
        self.size = size
        self.line_width = line_width
        self.stroke_color = stroke_color
    
    def generate(
        self, 
        pattern_type: PatternType, 
        output_path: Path
    ) -> Path:
        """
        Generate a tessellation pattern as SVG and save it to the output path.
        
        Args:
            pattern_type: Type of tessellation pattern
            output_path: Path to save the generated SVG
            
        Returns:
            Path to the generated SVG file
        """
        # Generate the SVG content based on pattern type
        if pattern_type == "triangular":
            svg_content = self._generate_triangular_pattern()
        elif pattern_type == "square":
            svg_content = self._generate_square_pattern()
        elif pattern_type == "hexagonal":
            svg_content = self._generate_hexagonal_pattern()
        else:
            raise ValueError(f"Unknown pattern type: {pattern_type}")
        
        # Ensure the output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the SVG content to the file
        with open(output_path, 'w') as f:
            f.write(svg_content)
        
        return output_path
    
    def _svg_header(self) -> str:
        """Generate SVG header."""
        return (
            f'<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
            f'<svg width="{self.size}" height="{self.size}" '
            f'xmlns="http://www.w3.org/2000/svg">\n'
            f'<desc>Tessellation Pattern</desc>\n'
        )
    
    def _svg_footer(self) -> str:
        """Generate SVG footer."""
        return '</svg>'
    
    def _generate_triangular_pattern(self) -> str:
        """Generate a triangular tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        cell_size = self.size // 10
        
        # Draw horizontal lines
        for i in range(0, self.size + 1, cell_size):
            svg += f'  <line x1="0" y1="{i}" x2="{self.size}" y2="{i}" />\n'
        
        # Draw diagonal lines (/)
        for i in range(-self.size, self.size + 1, cell_size):
            svg += f'  <line x1="0" y1="{i + self.size}" x2="{self.size}" y2="{i}" />\n'
        
        # Draw diagonal lines (\)
        for i in range(-self.size, self.size + 1, cell_size):
            svg += f'  <line x1="0" y1="{i}" x2="{self.size}" y2="{i + self.size}" />\n'
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _generate_square_pattern(self) -> str:
        """Generate a square tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        cell_size = self.size // 10
        
        # Draw horizontal lines
        for i in range(0, self.size + 1, cell_size):
            svg += f'  <line x1="0" y1="{i}" x2="{self.size}" y2="{i}" />\n'
        
        # Draw vertical lines
        for i in range(0, self.size + 1, cell_size):
            svg += f'  <line x1="{i}" y1="0" x2="{i}" y2="{self.size}" />\n'
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _generate_hexagonal_pattern(self) -> str:
        """Generate a hexagonal tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Hexagon parameters
        hex_size = self.size // 10
        r = hex_size  # Distance from center to corner
        
        # Calculate row and column spacing
        row_height = int(3 * r / 2)
        col_width = int(math.sqrt(3) * r)
        
        # Calculate number of rows and columns needed
        num_rows = self.size // row_height + 2
        num_cols = self.size // col_width + 2
        
        # Draw hexagons
        for row in range(num_rows):
            for col in range(num_cols):
                # Calculate center position
                cx = int(col * col_width + (row % 2) * col_width / 2)
                cy = int(row * row_height)
                
                # Generate hexagon points
                points = []
                for i in range(6):
                    angle_rad = math.pi / 3 * i
                    x = cx + int(r * math.cos(angle_rad))
                    y = cy + int(r * math.sin(angle_rad))
                    points.append(f"{x},{y}")
                
                # Draw the hexagon
                svg += f'  <polygon points="{" ".join(points)}" />\n'
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg