"""Command-line interface for tessellations generator."""
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Literal

from tessellations.core.svg_generator import SVGTessellationGenerator
from tessellations.core.complex_svg_generator import ComplexSVGTessellationGenerator
from tessellations.utils.file import generate_filename, get_output_path

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
        choices=["hexagonal", "floral"], 
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
    )
    return parser.parse_args()

def main():
    """Main entry point for the tessellation generator."""
    args = parse_args()
    
    print("Tessellations Generator")
    print(f"Current time: {datetime.now()}")
    
    # Generate filename and output path
    filename = generate_filename(args.pattern)
    output_path = get_output_path(args.output_dir, filename)
    
    print(f"Generating {args.pattern} tessellation...")
    print(f"Complexity: {args.complexity}")
    print(f"Size: {args.size}x{args.size} pixels")
    print(f"Line width: {args.line_width} pixels")
    print(f"Format: svg")
    
    # Generate the tessellation
    if args.pattern == "floral" or args.complexity == "complex":
        # Use the ComplexSVGTessellationGenerator for floral pattern or complex mode
        generator = ComplexSVGTessellationGenerator(
            size=args.size, 
            line_width=args.line_width,
            stroke_color=args.stroke_color,
            background_color=args.background_color
        )
    else:
        # Use the regular SVGTessellationGenerator for simple hexagonal pattern
        generator = SVGTessellationGenerator(
            size=args.size, 
            line_width=args.line_width
        )
    
    output_file = generator.generate(args.pattern, output_path)
    
    print(f"Tessellation generated and saved to: {output_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main())