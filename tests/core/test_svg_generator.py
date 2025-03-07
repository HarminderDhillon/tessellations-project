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

def test_generate_triangular_svg(tmp_output_dir):
    """Test generating a triangular tessellation as SVG."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "triangular_test.svg"
    
    result_path = generator.generate("triangular", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<?xml version="1.0"' in content
        assert '<svg width="400" height="400"' in content
        assert '<line ' in content

def test_generate_islamic_stars_svg(tmp_output_dir):
    """Test generating an Islamic stars tessellation as SVG."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "islamic_stars_test.svg"
    
    result_path = generator.generate("islamic_stars", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<svg width="400" height="400"' in content
        assert '<polygon ' in content or '<line ' in content

def test_generate_penrose_svg(tmp_output_dir):
    """Test generating a Penrose tessellation as SVG."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "penrose_test.svg"
    
    result_path = generator.generate("penrose", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<svg width="400" height="400"' in content
        assert '<polygon ' in content

def test_generate_celtic_knots_svg(tmp_output_dir):
    """Test generating a Celtic knots tessellation as SVG."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "celtic_knots_test.svg"
    
    result_path = generator.generate("celtic_knots", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<svg width="400" height="400"' in content
        assert '<path ' in content or '<circle ' in content

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

def test_generate_escher_svg(tmp_output_dir):
    """Test generating an Escher-inspired tessellation as SVG."""
    generator = ComplexSVGTessellationGenerator(size=400)
    output_path = tmp_output_dir / "escher_test.svg"
    
    result_path = generator.generate("escher", output_path)
    
    assert result_path.exists()
    with open(result_path, 'r') as f:
        content = f.read()
        assert '<svg width="400" height="400"' in content
        assert '<path ' in content

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