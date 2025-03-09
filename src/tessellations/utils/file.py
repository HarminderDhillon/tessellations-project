"""File-related utility functions."""
import os
from datetime import datetime
from pathlib import Path
from typing import Union

def generate_filename(pattern_type: str) -> str:
    """
    Generate a filename based on the pattern type and current timestamp.
    
    Args:
        pattern_type: Type of tessellation pattern
        
    Returns:
        Generated filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"tessellation_{pattern_type}_{timestamp}.svg"

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