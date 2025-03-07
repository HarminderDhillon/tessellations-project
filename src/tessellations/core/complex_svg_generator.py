"""SVG generator for complex tessellation patterns."""
from pathlib import Path
from typing import Literal, Tuple, List
import math
import random

PatternType = Literal[
    "triangular", "square", "hexagonal", 
    "islamic_stars", "penrose", "celtic_knots", 
    "floral", "escher"
]

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
        if pattern_type == "triangular":
            svg_content = self._generate_triangular_pattern()
        elif pattern_type == "square":
            svg_content = self._generate_square_pattern()
        elif pattern_type == "hexagonal":
            svg_content = self._generate_hexagonal_pattern()
        elif pattern_type == "islamic_stars":
            svg_content = self._generate_islamic_stars_pattern()
        elif pattern_type == "penrose":
            svg_content = self._generate_penrose_pattern()
        elif pattern_type == "celtic_knots":
            svg_content = self._generate_celtic_knots_pattern()
        elif pattern_type == "floral":
            svg_content = self._generate_floral_pattern()
        elif pattern_type == "escher":
            svg_content = self._generate_escher_pattern()
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
    
    def _generate_islamic_stars_pattern(self) -> str:
        """Generate an Islamic star tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Pattern parameters
        tile_size = self.size // 4
        
        # Create a pattern of Islamic 8-pointed stars
        for row in range(5):
            for col in range(5):
                x = col * tile_size - tile_size // 2
                y = row * tile_size - tile_size // 2
                
                # Skip some positions to create offset
                if (row + col) % 2 == 0:
                    self._draw_islamic_star(svg, x, y, tile_size)
        
        # Draw connecting lines between stars
        for row in range(6):
            y = row * tile_size - tile_size // 2
            svg += f'  <line x1="0" y1="{y}" x2="{self.size}" y2="{y}" />\n'
            
        for col in range(6):
            x = col * tile_size - tile_size // 2
            svg += f'  <line x1="{x}" y1="0" x2="{x}" y2="{self.size}" />\n'
        
        # Draw diagonal connecting lines
        for i in range(-5, 6):
            svg += f'  <line x1="0" y1="{(i+5)*tile_size}" x2="{self.size}" y2="{i*tile_size}" />\n'
            svg += f'  <line x1="0" y1="{i*tile_size}" x2="{self.size}" y2="{(i+5)*tile_size}" />\n'
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _draw_islamic_star(self, svg, x, y, size):
        """Draw an 8-pointed Islamic star."""
        center_x = x + size // 2
        center_y = y + size // 2
        outer_radius = size // 2
        inner_radius = outer_radius * 0.4
        
        points = []
        for i in range(8):
            # Outer point
            angle_outer = math.pi / 4 * i
            x_outer = center_x + outer_radius * math.cos(angle_outer)
            y_outer = center_y + outer_radius * math.sin(angle_outer)
            points.append(f"{x_outer},{y_outer}")
            
            # Inner point
            angle_inner = math.pi / 4 * (i + 0.5)
            x_inner = center_x + inner_radius * math.cos(angle_inner)
            y_inner = center_y + inner_radius * math.sin(angle_inner)
            points.append(f"{x_inner},{y_inner}")
        
        svg += f'  <polygon points="{" ".join(points)}" />\n'
        
        # Draw internal decoration
        internal_radius = inner_radius * 0.8
        for i in range(8):
            angle = math.pi / 4 * i
            end_x = center_x + internal_radius * math.cos(angle)
            end_y = center_y + internal_radius * math.sin(angle)
            svg += f'  <line x1="{center_x}" y1="{center_y}" x2="{end_x}" y2="{end_y}" />\n'
    
    def _generate_penrose_pattern(self) -> str:
        """Generate a Penrose tiling pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Create a simplified Penrose-like pattern (not a true Penrose tiling which is more complex)
        # We'll use a star pattern with overlaid triangles
        
        center_x = self.size // 2
        center_y = self.size // 2
        radius = self.size * 0.45
        
        # Create a 10-pointed star as the base
        for i in range(10):
            angle1 = 2 * math.pi * i / 10
            angle2 = 2 * math.pi * (i + 0.5) / 10
            
            x1 = center_x + radius * math.cos(angle1)
            y1 = center_y + radius * math.sin(angle1)
            
            x2 = center_x + (radius * 0.4) * math.cos(angle2)
            y2 = center_y + (radius * 0.4) * math.sin(angle2)
            
            points = [
                f"{center_x},{center_y}",
                f"{x1},{y1}",
                f"{x2},{y2}"
            ]
            
            svg += f'  <polygon points="{" ".join(points)}" />\n'
        
        # Add some additional triangles to create more complexity
        for i in range(10):
            angle1 = 2 * math.pi * i / 10
            angle2 = 2 * math.pi * (i + 1) / 10
            
            x1 = center_x + radius * math.cos(angle1)
            y1 = center_y + radius * math.sin(angle1)
            
            x2 = center_x + radius * math.cos(angle2)
            y2 = center_y + radius * math.sin(angle2)
            
            x3 = center_x + (radius * 1.2) * math.cos((angle1 + angle2) / 2)
            y3 = center_y + (radius * 1.2) * math.sin((angle1 + angle2) / 2)
            
            points = [
                f"{x1},{y1}",
                f"{x2},{y2}",
                f"{x3},{y3}"
            ]
            
            svg += f'  <polygon points="{" ".join(points)}" />\n'
            
        # Add rhombuses between the triangles
        for i in range(10):
            angle1 = 2 * math.pi * i / 10
            angle2 = 2 * math.pi * (i + 1) / 10
            angle_mid = (angle1 + angle2) / 2
            
            x1 = center_x + (radius * 0.6) * math.cos(angle1)
            y1 = center_y + (radius * 0.6) * math.sin(angle1)
            
            x2 = center_x + (radius * 0.6) * math.cos(angle2)
            y2 = center_y + (radius * 0.6) * math.sin(angle2)
            
            x3 = center_x + (radius * 0.9) * math.cos(angle_mid)
            y3 = center_y + (radius * 0.9) * math.sin(angle_mid)
            
            points = [
                f"{center_x},{center_y}",
                f"{x1},{y1}",
                f"{x3},{y3}",
                f"{x2},{y2}"
            ]
            
            svg += f'  <polygon points="{" ".join(points)}" />\n'
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _generate_celtic_knots_pattern(self) -> str:
        """Generate a Celtic knots tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Create a grid of basic Celtic knot elements
        cell_size = self.size // 8
        
        for row in range(8):
            for col in range(8):
                x = col * cell_size
                y = row * cell_size
                
                # Alternate between different knot patterns
                pattern = (row + col) % 4
                if pattern == 0:
                    self._draw_celtic_knot_element1(svg, x, y, cell_size)
                elif pattern == 1:
                    self._draw_celtic_knot_element2(svg, x, y, cell_size)
                elif pattern == 2:
                    self._draw_celtic_knot_element3(svg, x, y, cell_size)
                else:
                    self._draw_celtic_knot_element4(svg, x, y, cell_size)
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _draw_celtic_knot_element1(self, svg, x, y, size):
        """Draw a Celtic knot element with curved corners."""
        # Curve radius
        r = size / 4
        
        # Control point offset for Bezier curves (to make smoother curves)
        cp = size / 3
        
        # Define the four corners
        tl = (x + r, y + r)  # top-left
        tr = (x + size - r, y + r)  # top-right
        bl = (x + r, y + size - r)  # bottom-left
        br = (x + size - r, y + size - r)  # bottom-right
        
        # Draw the curves (this is a simplified representation)
        # Top-left to bottom-right curved path
        svg += f'  <path d="M {tl[0]},{tl[1]} C {tl[0]-cp},{tl[1]+cp} {br[0]-cp},{br[1]-cp} {br[0]},{br[1]}" />\n'
        
        # Bottom-left to top-right curved path
        svg += f'  <path d="M {bl[0]},{bl[1]} C {bl[0]+cp},{bl[1]-cp} {tr[0]-cp},{tr[1]+cp} {tr[0]},{tr[1]}" />\n'
        
        # Add decorative elements
        center = (x + size/2, y + size/2)
        svg += f'  <circle cx="{center[0]}" cy="{center[1]}" r="{r/2}" />\n'
    
    def _draw_celtic_knot_element2(self, svg, x, y, size):
        """Draw a Celtic knot element with interlaced loops."""
        # Center and dimensions
        center_x = x + size/2
        center_y = y + size/2
        r = size * 0.4
        
        # Draw interlocking circles
        svg += f'  <circle cx="{center_x-size/6}" cy="{center_y}" r="{r/2}" />\n'
        svg += f'  <circle cx="{center_x+size/6}" cy="{center_y}" r="{r/2}" />\n'
        
        # Draw arcs to connect them
        svg += f'  <path d="M {center_x-size/6+r/2},{center_y} A {r},{r} 0 0,1 {center_x+size/6-r/2},{center_y}" />\n'
        svg += f'  <path d="M {center_x+size/6-r/2},{center_y} A {r/2},{r/2} 0 0,0 {center_x+size/6+r/2},{center_y}" />\n'
        svg += f'  <path d="M {center_x+size/6+r/2},{center_y} A {r},{r} 0 0,1 {center_x-size/6+r/2},{center_y}" />\n'
    
    def _draw_celtic_knot_element3(self, svg, x, y, size):
        """Draw a Celtic knot element with a cross pattern."""
        # Center of the cell
        center_x = x + size/2
        center_y = y + size/2
        r = size * 0.4
        
        # Draw a cross shape
        hwidth = size * 0.1  # half width of the cross arms
        
        points1 = [
            f"{x+hwidth},{y+hwidth}",
            f"{center_x-hwidth},{center_y-hwidth}",
            f"{center_x+hwidth},{center_y-hwidth}",
            f"{x+size-hwidth},{y+hwidth}",
            f"{x+size-hwidth},{y+3*hwidth}",
            f"{center_x+hwidth},{center_y-hwidth}",
            f"{center_x+hwidth},{center_y+hwidth}",
            f"{x+size-hwidth},{y+size-3*hwidth}",
            f"{x+size-hwidth},{y+size-hwidth}",
            f"{center_x+hwidth},{center_y+hwidth}",
            f"{center_x-hwidth},{center_y+hwidth}",
            f"{x+hwidth},{y+size-hwidth}",
            f"{x+hwidth},{y+size-3*hwidth}",
            f"{center_x-hwidth},{center_y+hwidth}",
            f"{center_x-hwidth},{center_y-hwidth}",
            f"{x+hwidth},{y+3*hwidth}"
        ]
        
        svg += f'  <polygon points="{" ".join(points1)}" />\n'
    
    def _draw_celtic_knot_element4(self, svg, x, y, size):
        """Draw a Celtic knot element with a spiral pattern."""
        center_x = x + size/2
        center_y = y + size/2
        
        # Draw a simple spiral using path commands
        max_radius = size * 0.4
        min_radius = size * 0.1
        num_turns = 3
        num_points = 40
        
        for start_angle in [0, math.pi]:
            path = f'M '
            
            for i in range(num_points + 1):
                t = i / num_points
                radius = max_radius - (max_radius - min_radius) * t
                angle = start_angle + num_turns * 2 * math.pi * t
                
                x_point = center_x + radius * math.cos(angle)
                y_point = center_y + radius * math.sin(angle)
                
                if i == 0:
                    path += f'{x_point},{y_point} '
                else:
                    path += f'L {x_point},{y_point} '
            
            svg += f'  <path d="{path}" />\n'
    
    def _generate_floral_pattern(self) -> str:
        """Generate a floral tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Create a grid of floral elements
        cell_size = self.size // 6
        
        for row in range(7):
            for col in range(7):
                x = col * cell_size
                y = row * cell_size
                
                # Add offset to alternating rows
                if row % 2 == 1:
                    x += cell_size / 2
                
                self._draw_floral_element(svg, x, y, cell_size)
        
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
    
    def _generate_escher_pattern(self) -> str:
        """Generate an Escher-inspired tessellation pattern as SVG."""
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # We'll create a simplified Escher-like pattern based on a grid
        cell_size = self.size // 6
        
        # Create a grid of alternating fish-like shapes
        for row in range(6):
            for col in range(6):
                x = col * cell_size
                y = row * cell_size
                
                if (row + col) % 2 == 0:
                    self._draw_escher_fish(svg, x, y, cell_size, "right")
                else:
                    self._draw_escher_fish(svg, x, y, cell_size, "left")
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _draw_escher_fish(self, svg, x, y, size, direction):
        """Draw an Escher-inspired fish shape."""
        # Fish body parameters
        body_width = size * 0.8
        body_height = size * 0.5
        
        # Center of the cell
        center_x = x + size / 2
        center_y = y + size / 2
        
        # Direction determines the orientation of the fish
        flip = -1 if direction == "left" else 1
        
        # Draw the fish body (simplified as a curved shape)
        fish_path = f"M {center_x - flip*body_width/2},{center_y} "
        fish_path += f"Q {center_x},{center_y + body_height/2} {center_x + flip*body_width/2},{center_y} "
        fish_path += f"Q {center_x},{center_y - body_height/2} {center_x - flip*body_width/2},{center_y}"
        
        svg += f'  <path d="{fish_path}" />\n'
        
        # Add an eye
        eye_x = center_x + flip * body_width * 0.3
        eye_y = center_y - body_height * 0.1
        
        svg += f'  <circle cx="{eye_x}" cy="{eye_y}" r="{size * 0.06}" />\n'
        
        # Add a tail
        tail_x1 = center_x - flip * body_width * 0.4
        tail_y1 = center_y
        
        tail_x2 = center_x - flip * body_width * 0.7
        tail_y2 = center_y - body_height * 0.4
        
        tail_x3 = center_x - flip * body_width * 0.7
        tail_y3 = center_y + body_height * 0.4
        
        svg += f'  <path d="M {tail_x1},{tail_y1} L {tail_x2},{tail_y2} L {tail_x3},{tail_y3} Z" />\n'