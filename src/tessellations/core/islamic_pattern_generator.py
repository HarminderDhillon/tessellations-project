"""Advanced Islamic geometric pattern generator."""
from pathlib import Path
import math
from typing import List, Tuple, Union, Optional, Literal

class IslamicPatternGenerator:
    """Generator for authentic Islamic geometric patterns."""
    
    def __init__(
        self, 
        size: int = 1000, 
        line_width: float = 1.0, 
        stroke_color: str = "#000000",
        background_color: str = "#FFFFFF",
        pattern_type: str = "eight_fold"
    ):
        """
        Initialize the Islamic pattern generator.
        
        Args:
            size: Width and height of the output SVG in pixels
            line_width: Width of the lines in the pattern
            stroke_color: Color of the lines in the pattern
            background_color: Background color of the SVG
            pattern_type: Type of Islamic pattern (eight_fold, ten_fold, twelve_fold)
        """
        self.size = size
        self.line_width = line_width
        self.stroke_color = stroke_color
        self.background_color = background_color
        self.pattern_type = pattern_type
    
    def generate(self, output_path: Path) -> Path:
        """
        Generate an Islamic geometric pattern as SVG and save it to the output path.
        
        Args:
            output_path: Path to save the generated SVG
            
        Returns:
            Path to the generated SVG file
        """
        # Generate the SVG content based on pattern type
        if self.pattern_type == "eight_fold":
            svg_content = self._generate_eight_fold_pattern()
        elif self.pattern_type == "ten_fold":
            svg_content = self._generate_ten_fold_pattern()
        elif self.pattern_type == "twelve_fold":
            svg_content = self._generate_twelve_fold_pattern()
        else:
            raise ValueError(f"Unknown pattern type: {self.pattern_type}")
        
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
            f'viewBox="0 0 {self.size} {self.size}" '
            f'xmlns="http://www.w3.org/2000/svg">\n'
            f'<desc>Islamic Geometric Pattern</desc>\n'
            f'<rect width="{self.size}" height="{self.size}" fill="{self.background_color}"/>\n'
        )
    
    def _svg_footer(self) -> str:
        """Generate SVG footer."""
        return '</svg>'
    
    def _generate_eight_fold_pattern(self) -> str:
        """
        Generate an eight-fold Islamic geometric pattern.
        
        This pattern creates an intricate design based on 8-pointed stars
        with overlapping geometric elements and detailed interior structure.
        """
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Calculate the size of the basic unit
        unit_size = self.size / 4
        
        # Draw the full pattern
        for row in range(-1, 5):
            for col in range(-1, 5):
                x = col * unit_size
                y = row * unit_size
                
                # Draw the primary 8-pointed star
                svg += self._draw_eight_pointed_star(x, y, unit_size)
                
                # Draw the secondary elements (octagons and squares)
                svg += self._draw_octagon_grid(x, y, unit_size)
        
        # Draw connecting lines and additional geometric elements
        svg += self._draw_connecting_elements(unit_size)
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _draw_eight_pointed_star(self, x: float, y: float, size: float) -> str:
        """Draw an 8-pointed star with interior details."""
        center_x = x + size / 2
        center_y = y + size / 2
        
        outer_radius = size * 0.45
        mid_radius = size * 0.35
        inner_radius = size * 0.2
        
        # Generate the star points
        svg = ""
        
        # Draw the primary star shape
        points = []
        for i in range(8):
            # Outer points
            angle_outer = math.pi / 4 * i
            px = center_x + outer_radius * math.cos(angle_outer)
            py = center_y + outer_radius * math.sin(angle_outer)
            points.append(f"{px:.2f},{py:.2f}")
            
            # Inner points
            angle_inner = math.pi / 4 * (i + 0.5)
            px = center_x + mid_radius * math.cos(angle_inner)
            py = center_y + mid_radius * math.sin(angle_inner)
            points.append(f"{px:.2f},{py:.2f}")
        
        svg += f'  <polygon points="{" ".join(points)}" />\n'
        
        # Draw interior details
        svg += self._draw_star_interior(center_x, center_y, inner_radius, 8)
        
        # Draw additional decorative elements within the star
        for i in range(8):
            angle = math.pi / 4 * i
            
            # Inner decorative lines
            x1 = center_x + inner_radius * 0.4 * math.cos(angle)
            y1 = center_y + inner_radius * 0.4 * math.sin(angle)
            
            x2 = center_x + mid_radius * 0.8 * math.cos(angle)
            y2 = center_y + mid_radius * 0.8 * math.sin(angle)
            
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        return svg
    
    def _draw_star_interior(self, center_x: float, center_y: float, radius: float, points: int) -> str:
        """Draw interior details of a star."""
        svg = ""
        
        # Draw an inner polygon
        inner_points = []
        for i in range(points):
            angle = 2 * math.pi * i / points
            px = center_x + radius * math.cos(angle)
            py = center_y + radius * math.sin(angle)
            inner_points.append(f"{px:.2f},{py:.2f}")
        
        svg += f'  <polygon points="{" ".join(inner_points)}" />\n'
        
        # Draw internal decorative elements
        for i in range(points):
            angle1 = 2 * math.pi * i / points
            angle2 = 2 * math.pi * ((i + 1) % points) / points
            
            x1 = center_x + radius * math.cos(angle1)
            y1 = center_y + radius * math.sin(angle1)
            
            x2 = center_x + radius * math.cos(angle2)
            y2 = center_y + radius * math.sin(angle2)
            
            # Draw a line to the center
            svg += f'  <line x1="{center_x:.2f}" y1="{center_y:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" />\n'
            
            # Draw decorative arcs
            svg += self._draw_decorative_arc(center_x, center_y, radius * 0.7, angle1, angle2)
        
        return svg
    
    def _draw_decorative_arc(
        self, 
        center_x: float, 
        center_y: float, 
        radius: float, 
        start_angle: float, 
        end_angle: float
    ) -> str:
        """Draw a decorative arc between two angles."""
        # Convert angles to SVG arc format
        start_x = center_x + radius * math.cos(start_angle)
        start_y = center_y + radius * math.sin(start_angle)
        
        end_x = center_x + radius * math.cos(end_angle)
        end_y = center_y + radius * math.sin(end_angle)
        
        # Use SVG path arc command
        large_arc_flag = (end_angle - start_angle) > math.pi
        
        svg = f'  <path d="M {start_x:.2f},{start_y:.2f} '
        svg += f'A {radius:.2f},{radius:.2f} 0 {1 if large_arc_flag else 0},1 {end_x:.2f},{end_y:.2f}" />\n'
        
        return svg
    
    def _draw_octagon_grid(self, x: float, y: float, size: float) -> str:
        """Draw octagonal grid elements that connect stars."""
        svg = ""
        center_x = x + size / 2
        center_y = y + size / 2
        
        # Size of the octagon
        octagon_radius = size * 0.3
        
        # Generate octagon points
        octagon_points = []
        for i in range(8):
            angle = math.pi / 4 * i
            px = center_x + octagon_radius * math.cos(angle)
            py = center_y + octagon_radius * math.sin(angle)
            octagon_points.append((px, py))
        
        # Draw the octagon
        points_str = " ".join([f"{px:.2f},{py:.2f}" for px, py in octagon_points])
        svg += f'  <polygon points="{points_str}" />\n'
        
        # Draw interior details
        for i in range(4):
            # Draw crossing lines
            x1 = octagon_points[i][0]
            y1 = octagon_points[i][1]
            x2 = octagon_points[i+4][0]
            y2 = octagon_points[i+4][1]
            
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        return svg
    
    def _draw_connecting_elements(self, unit_size: float) -> str:
        """Draw elements that connect the stars and octagons."""
        svg = ""
        
        # Calculate coordinates for connecting elements
        for row in range(5):
            for col in range(5):
                x = col * unit_size
                y = row * unit_size
                
                center_x = x + unit_size / 2
                center_y = y + unit_size / 2
                
                # Draw diamond connectors at the midpoints
                if col < 4:
                    # Horizontal connector
                    right_x = center_x + unit_size / 2
                    self._draw_diamond_connector(svg, center_x, center_y, right_x, center_y, unit_size * 0.15)
                
                if row < 4:
                    # Vertical connector
                    bottom_y = center_y + unit_size / 2
                    self._draw_diamond_connector(svg, center_x, center_y, center_x, bottom_y, unit_size * 0.15)
        
        return svg
    
    def _draw_diamond_connector(
        self, 
        svg: str, 
        x1: float, 
        y1: float, 
        x2: float, 
        y2: float, 
        width: float
    ) -> str:
        """Draw a diamond shape connector between two points."""
        # Calculate the midpoint
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        # Calculate perpendicular direction
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx*dx + dy*dy)
        
        # Normalize and rotate 90 degrees
        perp_x = -dy / length
        perp_y = dx / length
        
        # Calculate diamond points
        diamond_points = [
            f"{x1:.2f},{y1:.2f}",
            f"{mid_x + width * perp_x:.2f},{mid_y + width * perp_y:.2f}",
            f"{x2:.2f},{y2:.2f}",
            f"{mid_x - width * perp_x:.2f},{mid_y - width * perp_y:.2f}"
        ]
        
        return f'  <polygon points="{" ".join(diamond_points)}" />\n'
    
    def _generate_ten_fold_pattern(self) -> str:
        """
        Generate a ten-fold Islamic geometric pattern.
        
        This pattern creates an intricate design based on 10-pointed stars
        with overlapping geometric elements and detailed interior structure.
        """
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Calculate the size of the basic unit
        unit_size = self.size / 3
        
        # Draw the pattern
        for row in range(-1, 4):
            for col in range(-1, 4):
                x = col * unit_size
                y = row * unit_size
                
                # Draw 10-pointed stars as the primary elements
                svg += self._draw_ten_pointed_star(x, y, unit_size)
                
                # Draw the interlocking secondary elements
                svg += self._draw_decagon_elements(x, y, unit_size)
        
        # Draw connecting lines and additional geometric elements
        svg += self._draw_ten_fold_connections(unit_size)
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _draw_ten_pointed_star(self, x: float, y: float, size: float) -> str:
        """Draw a 10-pointed star with interior details."""
        center_x = x + size / 2
        center_y = y + size / 2
        
        outer_radius = size * 0.45
        mid_radius = size * 0.35
        inner_radius = size * 0.25
        
        # Generate the star points
        svg = ""
        
        # Draw the primary star shape
        points = []
        for i in range(10):
            # Outer points
            angle_outer = math.pi / 5 * i
            px = center_x + outer_radius * math.cos(angle_outer)
            py = center_y + outer_radius * math.sin(angle_outer)
            points.append(f"{px:.2f},{py:.2f}")
            
            # Inner points
            angle_inner = math.pi / 5 * (i + 0.5)
            px = center_x + mid_radius * math.cos(angle_inner)
            py = center_y + mid_radius * math.sin(angle_inner)
            points.append(f"{px:.2f},{py:.2f}")
        
        svg += f'  <polygon points="{" ".join(points)}" />\n'
        
        # Draw interior details
        svg += self._draw_star_interior(center_x, center_y, inner_radius, 10)
        
        # Create additional inner details specific to 10-fold symmetry
        svg += self._draw_ten_fold_interior(center_x, center_y, inner_radius)
        
        return svg
    
    def _draw_ten_fold_interior(self, center_x: float, center_y: float, radius: float) -> str:
        """Draw interior details specific to 10-fold symmetry."""
        svg = ""
        
        # Draw internal pentagon
        inner_radius = radius * 0.5
        pentagon_points = []
        for i in range(5):
            angle = 2 * math.pi * i / 5
            px = center_x + inner_radius * math.cos(angle)
            py = center_y + inner_radius * math.sin(angle)
            pentagon_points.append(f"{px:.2f},{py:.2f}")
        
        svg += f'  <polygon points="{" ".join(pentagon_points)}" />\n'
        
        # Draw decorative elements
        for i in range(5):
            angle1 = 2 * math.pi * i / 5
            angle2 = 2 * math.pi * ((i + 1) % 5) / 5
            
            # Draw internal star lines
            x1 = center_x + inner_radius * math.cos(angle1)
            y1 = center_y + inner_radius * math.sin(angle1)
            
            for j in range(1, 4):
                idx = (i + j) % 5
                angle_target = 2 * math.pi * idx / 5
                x2 = center_x + inner_radius * math.cos(angle_target)
                y2 = center_y + inner_radius * math.sin(angle_target)
                
                svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        return svg
    
    def _draw_decagon_elements(self, x: float, y: float, size: float) -> str:
        """Draw decagonal grid elements that connect stars."""
        svg = ""
        center_x = x + size / 2
        center_y = y + size / 2
        
        # Size of the decagon
        decagon_radius = size * 0.3
        
        # Generate decagon points
        decagon_points = []
        for i in range(10):
            angle = math.pi / 5 * i
            px = center_x + decagon_radius * math.cos(angle)
            py = center_y + decagon_radius * math.sin(angle)
            decagon_points.append((px, py))
        
        # Draw the decagon
        points_str = " ".join([f"{px:.2f},{py:.2f}" for px, py in decagon_points])
        svg += f'  <polygon points="{points_str}" />\n'
        
        # Draw interior details
        for i in range(5):
            # Draw 5-fold interior lines
            x1 = decagon_points[i*2][0]
            y1 = decagon_points[i*2][1]
            
            for j in range(1, 5):
                idx = ((i + j) % 5) * 2
                x2 = decagon_points[idx][0]
                y2 = decagon_points[idx][1]
                
                svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        return svg
    
    def _draw_ten_fold_connections(self, unit_size: float) -> str:
        """Draw elements that connect the 10-fold stars and decagons."""
        svg = ""
        
        # Calculate coordinates for connecting elements
        for row in range(4):
            for col in range(4):
                x = col * unit_size
                y = row * unit_size
                
                center_x = x + unit_size / 2
                center_y = y + unit_size / 2
                
                # Draw diamond connectors at the midpoints
                if col < 3:
                    # Horizontal connector
                    right_x = center_x + unit_size / 2
                    self._draw_diamond_connector(svg, center_x, center_y, right_x, center_y, unit_size * 0.15)
                
                if row < 3:
                    # Vertical connector
                    bottom_y = center_y + unit_size / 2
                    self._draw_diamond_connector(svg, center_x, center_y, center_x, bottom_y, unit_size * 0.15)
                
                # Draw diagonal connectors for more complexity
                if col < 3 and row < 3:
                    diag_x = center_x + unit_size / 2
                    diag_y = center_y + unit_size / 2
                    self._draw_diamond_connector(svg, center_x, center_y, diag_x, diag_y, unit_size * 0.1)
        
        return svg
    
    def _generate_twelve_fold_pattern(self) -> str:
        """
        Generate a twelve-fold Islamic geometric pattern.
        
        This pattern creates an intricate design based on 12-pointed stars
        with overlapping geometric elements and detailed interior structure.
        """
        svg = self._svg_header()
        
        # Add a group for the pattern with styling
        svg += f'<g stroke="{self.stroke_color}" stroke-width="{self.line_width}" fill="none">\n'
        
        # Calculate the size of the basic unit
        unit_size = self.size / 3
        
        # Draw the pattern
        for row in range(-1, 4):
            for col in range(-1, 4):
                x = col * unit_size
                y = row * unit_size
                
                # Draw 12-pointed stars as the primary elements
                svg += self._draw_twelve_pointed_star(x, y, unit_size)
                
                # Draw the secondary elements
                svg += self._draw_dodecagon_elements(x, y, unit_size)
        
        # Draw connecting elements
        svg += self._draw_twelve_fold_connections(unit_size)
        
        svg += '</g>\n'
        svg += self._svg_footer()
        
        return svg
    
    def _draw_twelve_pointed_star(self, x: float, y: float, size: float) -> str:
        """Draw a 12-pointed star with interior details."""
        center_x = x + size / 2
        center_y = y + size / 2
        
        outer_radius = size * 0.45
        mid_radius = size * 0.35
        inner_radius = size * 0.25
        
        # Generate the star points
        svg = ""
        
        # Draw the primary star shape
        points = []
        for i in range(12):
            # Outer points
            angle_outer = math.pi / 6 * i
            px = center_x + outer_radius * math.cos(angle_outer)
            py = center_y + outer_radius * math.sin(angle_outer)
            points.append(f"{px:.2f},{py:.2f}")
            
            # Inner points
            angle_inner = math.pi / 6 * (i + 0.5)
            px = center_x + mid_radius * math.cos(angle_inner)
            py = center_y + mid_radius * math.sin(angle_inner)
            points.append(f"{px:.2f},{py:.2f}")
        
        svg += f'  <polygon points="{" ".join(points)}" />\n'
        
        # Draw interior details
        svg += self._draw_star_interior(center_x, center_y, inner_radius, 12)
        
        # Create additional inner details specific to 12-fold symmetry
        svg += self._draw_twelve_fold_interior(center_x, center_y, inner_radius)
        
        return svg
    
    def _draw_twelve_fold_interior(self, center_x: float, center_y: float, radius: float) -> str:
        """Draw interior details specific to 12-fold symmetry."""
        svg = ""
        
        # Draw internal hexagon
        inner_radius = radius * 0.6
        hexagon_points = []
        for i in range(6):
            angle = 2 * math.pi * i / 6
            px = center_x + inner_radius * math.cos(angle)
            py = center_y + inner_radius * math.sin(angle)
            hexagon_points.append(f"{px:.2f},{py:.2f}")
        
        svg += f'  <polygon points="{" ".join(hexagon_points)}" />\n'
        
        # Draw interior star
        star_points = []
        for i in range(6):
            outer_angle = 2 * math.pi * i / 6
            inner_angle = 2 * math.pi * (i + 0.5) / 6
            
            px_outer = center_x + inner_radius * math.cos(outer_angle)
            py_outer = center_y + inner_radius * math.sin(outer_angle)
            
            px_inner = center_x + (inner_radius * 0.4) * math.cos(inner_angle)
            py_inner = center_y + (inner_radius * 0.4) * math.sin(inner_angle)
            
            star_points.append(f"{px_outer:.2f},{py_outer:.2f}")
            star_points.append(f"{px_inner:.2f},{py_inner:.2f}")
        
        svg += f'  <polygon points="{" ".join(star_points)}" />\n'
        
        # Draw additional decorative elements
        for i in range(6):
            angle1 = 2 * math.pi * i / 6
            angle2 = 2 * math.pi * ((i + 1) % 6) / 6
            
            x1 = center_x + inner_radius * 0.4 * math.cos(angle1)
            y1 = center_y + inner_radius * 0.4 * math.sin(angle1)
            
            x2 = center_x + inner_radius * 0.4 * math.cos(angle2)
            y2 = center_y + inner_radius * 0.4 * math.sin(angle2)
            
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        return svg
    
    def _draw_dodecagon_elements(self, x: float, y: float, size: float) -> str:
        """Draw dodecagonal grid elements that connect stars."""
        svg = ""
        center_x = x + size / 2
        center_y = y + size / 2
        
        # Size of the dodecagon
        dodecagon_radius = size * 0.3
        
        # Generate dodecagon points
        dodecagon_points = []
        for i in range(12):
            angle = math.pi / 6 * i
            px = center_x + dodecagon_radius * math.cos(angle)
            py = center_y + dodecagon_radius * math.sin(angle)
            dodecagon_points.append((px, py))
        
        # Draw the dodecagon
        points_str = " ".join([f"{px:.2f},{py:.2f}" for px, py in dodecagon_points])
        svg += f'  <polygon points="{points_str}" />\n'
        
        # Draw interior details - lines connecting opposite points
        for i in range(6):
            x1 = dodecagon_points[i][0]
            y1 = dodecagon_points[i][1]
            
            x2 = dodecagon_points[i+6][0]
            y2 = dodecagon_points[i+6][1]
            
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        # Draw another set of interior details
        for i in range(4):
            idx1 = i * 3
            idx2 = (idx1 + 6) % 12
            
            x1 = dodecagon_points[idx1][0]
            y1 = dodecagon_points[idx1][1]
            
            x2 = dodecagon_points[idx2][0]
            y2 = dodecagon_points[idx2][1]
            
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        return svg
    
    def _draw_twelve_fold_connections(self, unit_size: float) -> str:
        """Draw elements that connect the 12-fold stars and dodecagons."""
        svg = ""
        
        # Calculate coordinates for connecting elements
        for row in range(4):
            for col in range(4):
                x = col * unit_size
                y = row * unit_size
                
                center_x = x + unit_size / 2
                center_y = y + unit_size / 2
                
                # Draw diamond connectors at the midpoints
                if col < 3:
                    # Horizontal connector
                    right_x = center_x + unit_size / 2
                    svg += self._draw_diamond_connector(svg, center_x, center_y, right_x, center_y, unit_size * 0.15)
                
                if row < 3:
                    # Vertical connector
                    bottom_y = center_y + unit_size / 2
                    svg += self._draw_diamond_connector(svg, center_x, center_y, center_x, bottom_y, unit_size * 0.15)
                
                # Draw complex crossing patterns between stars
                if col < 3 and row < 3:
                    svg += self._draw_crossing_pattern(center_x, center_y, unit_size)
        
        return svg
    
    def _draw_crossing_pattern(self, center_x: float, center_y: float, unit_size: float) -> str:
        """Draw complex crossing patterns between stars."""
        svg = ""
        
        # Define crossing pattern
        radius = unit_size * 0.2
        points = 6
        
        for i in range(points):
            angle1 = 2 * math.pi * i / points
            angle2 = 2 * math.pi * ((i + points//2) % points) / points
            
            x1 = center_x + radius * math.cos(angle1)
            y1 = center_y + radius * math.sin(angle1)
            
            x2 = center_x + radius * math.cos(angle2)
            y2 = center_y + radius * math.sin(angle2)
            
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />\n'
        
        return svg