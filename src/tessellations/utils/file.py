"""File-related utility functions."""
import os
from datetime import datetime
from pathlib import Path
from typing import Literal, Union

FileFormat = Literal["svg", "png"]

def generate_filename(pattern_type: str, extension: FileFormat = "svg") -> str:
    """
    Generate a filename based on the pattern type and current timestamp.
    
    Args:
        pattern_type: Type of tessellation pattern
        extension: File extension (without the dot)
        
    Returns:
        Generated filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"tessellation_{pattern_type}_{timestamp}.{extension}"

def get_output_path(output_dir: Union[str, Path], filename: str) -> Path:
    """
    Get the full path to save the output file.
    
    Args:
        output_dir: Directory to save the generated image
        filename: Name of the output file
        
    Returns:
        Full path to the output file
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / filename