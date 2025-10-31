#!/bin/bash
# Setup script for nbutils development

echo "🔧 Setting up nbutils development environment..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install package in development mode
echo "Installing nbutils in development mode..."
pip install -e ".[dev]"

# Create necessary directories
echo "Creating directory structure..."
mkdir -p tests/fixtures

# Run tests
echo "Running tests..."
pytest tests/ -v

echo "✅ Setup complete!"
echo ""
echo "To activate the environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "Try it out:"
echo "  nbutils --help"
echo "  nbutils clean --help"