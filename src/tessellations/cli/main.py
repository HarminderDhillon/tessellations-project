"""Command-line interface for tessellations generator."""
import argparse
import sys
from datetime import datetime
from pathlib import Path

from tessellations.core.generator import TessellationGenerator
from tessellations.utils.file import generate_filename, get_output_path

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
        type=int, 
        default=2,
        help="Width of the lines in the tessellation"
    )
    return parser.parse_args()

def main():
    """Main entry point for the tessellation generator."""
    args = parse_args()
    
    print("Tessellations Generator")
    print(f"Current time: {datetime.now()}")
    
    # Initialize the generator
    generator = TessellationGenerator(size=args.size, line_width=args.line_width)
    
    # Generate filename and output path
    filename = generate_filename(args.pattern)
    output_path = get_output_path(args.output_dir, filename)
    
    print(f"Generating {args.pattern} tessellation...")
    print(f"Size: {args.size}x{args.size} pixels")
    print(f"Line width: {args.line_width} pixels")
    
    # Generate the tessellation
    output_file = generator.generate(args.pattern, output_path)
    
    print(f"Tessellation generated and saved to: {output_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main())