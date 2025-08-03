#!/bin/bash

echo "Generating LaTeX files from JSON data..."
python3 generate_latex.py

echo "Compiling PDF..."
pdflatex -output-directory=build src/main.tex
pdflatex -output-directory=build src/main.tex

echo "Build complete! PDF available at build/main.pdf" 