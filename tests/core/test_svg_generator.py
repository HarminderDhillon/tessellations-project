"""Tests for the SVG tessellation generator."""
import os
from pathlib import Path

import pytest

from tessellations.core.svg_generator import SVGTessellationGenerator

@pytest.fixture
def tmp_output_dir(tmp_path):
    """Create a temporary output directory."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir

def test_generate_triangular_svg(tmp_output_dir):
    """Test generating a triangular tessellation as SVG."""
    generator = SVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "triangular_test.svg"
    
    result_path = generator.generate("triangular", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<?xml version="1.0"' in content
        assert '<svg width="400" height="400"' in content
        assert '<line ' in content

def test_generate_square_svg(tmp_output_dir):
    """Test generating a square tessellation as SVG."""
    generator = SVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "square_test.svg"
    
    result_path = generator.generate("square", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<svg width="400" height="400"' in content
        assert '<line ' in content

def test_generate_hexagonal_svg(tmp_output_dir):
    """Test generating a hexagonal tessellation as SVG."""
    generator = SVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "hexagonal_test.svg"
    
    result_path = generator.generate("hexagonal", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<svg width="400" height="400"' in content
        assert '<polygon ' in content