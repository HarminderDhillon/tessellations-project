"""Command-line interface for tessellations generator."""
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Literal

from tessellations.core.generator import TessellationGenerator
from tessellations.core.svg_generator import SVGTessellationGenerator
from tessellations.core.complex_svg_generator import ComplexSVGTessellationGenerator
from tessellations.utils.file import generate_filename, get_output_path

FileFormat = Literal["svg", "png"]
PatternComplexity = Literal["simple", "complex"]

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate tessellation patterns for coloring books")
    parser.add_argument(
        "--output-dir", 
        type=str, 
        default="output",
        help="Directory to save generated tessellations"
    )
    parser.add_argument(
        "--pattern", 
        type=str, 
        choices=[
            "triangular", "square", "hexagonal",
            "islamic_stars", "penrose", "celtic_knots",
            "floral", "escher"
        ], 
        default="hexagonal",
        help="Type of tessellation pattern to generate"
    )
    parser.add_argument(
        "--complexity",
        type=str,
        choices=["simple", "complex"],
        default="simple",
        help="Complexity level of the pattern (simple uses basic patterns, complex uses advanced patterns)"
    )
    parser.add_argument(
        "--size", 
        type=int, 
        default=800,
        help="Size of the output image in pixels"
    )
    parser.add_argument(
        "--line-width", 
        type=float, 
        default=1.0,
        help="Width of the lines in the tessellation"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["svg", "png"],
        default="svg",
        help="Output file format (svg or png)"
    )
    parser.add_argument(
        "--stroke-color",
        type=str,
        default="#000000",
        help="Color of the lines in the tessellation (hex format)"
    )
    parser.add_argument(
        "--background-color",
        type=str,
        default="#FFFFFF",
        help="Background color of the image (hex format)"