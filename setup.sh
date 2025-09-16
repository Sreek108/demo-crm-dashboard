#!/bin/bash

# CRM Dashboard Setup Script
echo "🚀 Setting up Executive CRM Dashboard..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

echo "✅ Python 3 found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # macOS/Linux
    source venv/bin/activate
fi

# Upgrade pip
echo "⬆️ Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo "📚 Installing requirements..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 To run the application:"
echo ""
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    echo "1. Activate virtual environment: venv\Scripts\activate"
else
    echo "1. Activate virtual environment: source venv/bin/activate"
fi
echo "2. Run Streamlit: streamlit run app.py"
echo "3. Open browser: http://localhost:8501"
echo ""
echo "🚀 For deployment: Push to GitHub and connect to Streamlit Cloud"
echo ""
