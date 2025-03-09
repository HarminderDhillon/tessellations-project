"""SVG generator for complex tessellation patterns."""
from pathlib import Path
from typing import Literal, Tuple, List
import math
import random

PatternType = Literal["hexagonal", "floral"]

class ComplexSVGTessellationGenerator:
    """Generator for complex SVG tessellation patterns."""
    
    def __init__(
        self, 
        size: int = 800, 
        line_width: float = 1.0, 
        stroke_color: str = "#000000",
        background_color: str = "#FFFFFF"
    ):
        """
        Initialize the SVG tessellation generator.
        
        Args:
            size: Width and height of the output image in pixels
            line_width: Width of the lines in the tessellation
            stroke_color: Color of the lines in the tessellation
            background_color: Background color of the SVG
        """
        self.size = size
        self.line_width = line_width
        self.stroke_color = stroke_color
        self.background_color = background_color
    
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
        if pattern_type == "hexagonal":
            svg_content = self._generate_hexagonal_pattern()
        elif pattern_type == "floral":
            svg_content = self._generate_floral_pattern()
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
            f'<desc>Complex Tessellation Pattern</desc>\n'
            f'<rect width="{self.size}" height="{self.size}" fill="{self.background_color}"/>\n'
        )
    
    def _svg_footer(self) -> str:
        """Generate SVG footer."""
        return '</svg>'
    
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
    
    def _generate_floral_pattern(self) -> str:
        """Generate a floral tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Create a grid of floral elements
        cell_size = self.size // 6
        
        for row in range(6):
            for col in range(6):
                x = col * cell_size
                y = row * cell_size
                
                # Draw a floral element
                svg = self._draw_floral_element(svg, x, y, cell_size)
        
        # Close the group and SVG
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _draw_floral_element(self, svg, x, y, size):
        """Draw a floral element."""
        center_x = x + size / 2
        center_y = y + size / 2
        petal_size = size * 0.4
        
        # Draw petals
        num_petals = 8
        for i in range(num_petals):
            angle = 2 * math.pi * i / num_petals
            
            # Calculate control points for bezier curve (petal shape)
            x1 = center_x + petal_size * 0.5 * math.cos(angle)
            y1 = center_y + petal_size * 0.5 * math.sin(angle)
            
            ctrl_angle1 = angle + math.pi / 8
            ctrl_angle2 = angle - math.pi / 8
            
            ctrl_x1 = center_x + petal_size * math.cos(ctrl_angle1)
            ctrl_y1 = center_y + petal_size * math.sin(ctrl_angle1)
            
            ctrl_x2 = center_x + petal_size * math.cos(ctrl_angle2)
            ctrl_y2 = center_y + petal_size * math.sin(ctrl_angle2)
            
            x2 = center_x + petal_size * 0.5 * math.cos(angle)
            y2 = center_y + petal_size * 0.5 * math.sin(angle)
            
            # Draw the petal using a bezier curve
            svg += f'  <path d="M {center_x},{center_y} Q {ctrl_x1},{ctrl_y1} {x1},{y1} Q {ctrl_x2},{ctrl_y2} {center_x},{center_y}" />\n'
        
        # Draw center circle
        svg += f'  <circle cx="{center_x}" cy="{center_y}" r="{size * 0.1}" />\n'
        
        # Draw some dots for stamens
        for i in range(num_petals):
            angle = 2 * math.pi * (i + 0.5) / num_petals
            stamen_x = center_x + size * 0.15 * math.cos(angle)
            stamen_y = center_y + size * 0.15 * math.sin(angle)
            
            svg += f'  <circle cx="{stamen_x}" cy="{stamen_y}" r="{size * 0.02}" />\n'
        
        return svg