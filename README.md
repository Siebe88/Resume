# Siebe Kylstra - Resume

This repository contains my professional resume in LaTeX format with a modular structure for easy maintenance and updates.

## Project Structure

```
Resume/
├── main.tex                 # Main LaTeX document
├── src/                     # Source files
│   ├── header.tex          # Contact information and header
│   ├── skills.tex          # Skills section
│   ├── experience.tex      # Professional experience
│   ├── projects.tex        # Projects section
│   ├── education.tex       # Education details
│   ├── interests.tex       # Personal interests
│   └── experience/         # Individual job files
│       ├── helperduck.tex
│       ├── performation.tex
│       ├── ilionx.tex
│       └── axians.tex
├── build/                  # Build artifacts (auto-generated)
├── output/                 # Final PDF output
├── .vscode/               # VS Code settings
└── README.md              # This file
```

## Prerequisites

- LaTeX distribution (BasicTeX or MacTeX)
- Required packages: fontawesome, enumitem, xcolor, hyperref

## Building the Resume

### Command Line

```bash
pdflatex main.tex
```

### VS Code

1. Install the LaTeX Workshop extension
2. Open `main.tex`
3. Use `Ctrl+Alt+B` (or `Cmd+Alt+B` on Mac) to build

## File Organization

- **Source files** (`src/`): All LaTeX content files
- **Build artifacts** (`build/`): Temporary files generated during compilation
- **Output** (`output/`): Final PDF files

## Updating Content

To update specific sections:

1. Edit the corresponding `.tex` file in `src/`
2. Recompile with `pdflatex main.tex`
3. The updated PDF will be generated in `build/`

## Version Control

The `.gitignore` file excludes build artifacts and temporary files, keeping only the source files in version control.
