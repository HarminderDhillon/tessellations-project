"""Command-line interface for tessellations generator."""
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Literal

from tessellations.core.generator import TessellationGenerator
from tessellations.core.svg_generator import SVGTessellationGenerator
from tessellations.utils.file import generate_filename, get_output_path

FileFormat = Literal["svg", "png"]

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
        choices=["triangular", "square", "hexagonal"], 
        default="hexagonal",
        help="Type of tessellation pattern to generate"
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
    return parser.parse_args()

def main():
    """Main entry point for the tessellation generator."""
    args = parse_args()
    
    print("Tessellations Generator")
    print(f"Current time: {datetime.now()}")
    
    # Generate filename and output path
    filename = generate_filename(args.pattern, args.format)
    output_path = get_output_path(args.output_dir, filename)
    
    print(f"Generating {args.pattern} tessellation...")
    print(f"Size: {args.size}x{args.size} pixels")
    print(f"Line width: {args.line_width} pixels")
    print(f"Format: {args.format}")
    
    # Generate the tessellation
    if args.format == "svg":
        generator = SVGTessellationGenerator(
            size=args.size, 
            line_width=args.line_width
        )
    else:  # PNG
        generator = TessellationGenerator(
            size=args.size, 
            line_width=int(args.line_width)
        )
    
    output_file = generator.generate(args.pattern, output_path)
    
    print(f"Tessellation generated and saved to: {output_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main())