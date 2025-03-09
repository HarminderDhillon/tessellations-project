"""Tests for the complex SVG tessellation generator."""
import os
from pathlib import Path

import pytest

from tessellations.core.complex_svg_generator import ComplexSVGTessellationGenerator

@pytest.fixture
def tmp_output_dir(tmp_path):
    """Create a temporary output directory."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir

def test_generate_hexagonal_svg(tmp_output_dir):
    """Test generating a hexagonal tessellation as SVG."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "hexagonal_test.svg"
    
    result_path = generator.generate("hexagonal", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<?xml version="1.0"' in content
        assert '<svg width="400" height="400"' in content
        assert '<polygon ' in content

def test_generate_floral_svg(tmp_output_dir):
    """Test generating a floral tessellation as SVG."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "floral_test.svg"
    
    result_path = generator.generate("floral", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<svg width="400" height="400"' in content
        assert '<path ' in content or '<circle ' in content

def test_invalid_pattern(tmp_output_dir):
    """Test that an invalid pattern raises an error."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "invalid_test.svg"
    
    with pytest.raises(ValueError):
        generator.generate("invalid_pattern", output_path)

def test_custom_styling(tmp_output_dir):
    """Test custom styling options."""
    generator = ComplexSVGTessellationGenerator(
        size=400,
        line_width=2.5,
        stroke_color="#FF0000",
        background_color="#FFFFCC"
    )
    output_path = tmp_output_dir / "custom_style_test.svg"
    
    result_path = generator.generate("hexagonal", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert 'stroke="#FF0000"' in content
        assert 'stroke-width="2.5"' in content
        assert 'fill="#FFFFCC"' in content or 'fill="#FFFFCC"' in content