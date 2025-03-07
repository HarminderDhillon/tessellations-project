"""Tests for the tessellation generator."""
import os
from pathlib import Path

import pytest
from PIL import Image

from tessellations.core.generator import TessellationGenerator

@pytest.fixture
def tmp_output_dir(tmp_path):
    """Create a temporary output directory."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir

def test_generate_triangular(tmp_output_dir):
    """Test generating a triangular tessellation."""
    generator = TessellationGenerator(size=400)
    output_path = tmp_output_dir / "triangular_test.png"
    
    result_path = generator.generate("triangular", output_path)
    
    assert result_path.exists()
    with Image.open(result_path) as img:
        assert img.size == (400, 400)
        assert img.mode == "RGB"

def test_generate_square(tmp_output_dir):
    """Test generating a square tessellation."""
    generator = TessellationGenerator(size=400)
    output_path = tmp_output_dir / "square_test.png"
    
    result_path = generator.generate("square", output_path)
    
    assert result_path.exists()
    with Image.open(result_path) as img:
        assert img.size == (400, 400)
        assert img.mode == "RGB"

def test_generate_hexagonal(tmp_output_dir):
    """Test generating a hexagonal tessellation."""
    generator = TessellationGenerator(size=400)
    output_path = tmp_output_dir / "hexagonal_test.png"
    
    result_path = generator.generate("hexagonal", output_path)
    
    assert result_path.exists()
    with Image.open(result_path) as img:
        assert img.size == (400, 400)
        assert img.mode == "RGB"