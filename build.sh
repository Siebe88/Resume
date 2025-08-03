#!/bin/bash

echo "Generating LaTeX files from JSON data..."
python3 generate_latex.py

echo "Copying source files to build directory..."
cp -r src/* build/

echo "Compiling PDF..."
pdflatex -interaction=nonstopmode -output-directory=build build/main.tex
pdflatex -interaction=nonstopmode -output-directory=build build/main.tex

echo "Build complete! PDF available at build/main.pdf" 