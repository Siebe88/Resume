# Siebe Kylstra - Resume

This repository contains my professional resume in LaTeX format with a modular structure for easy maintenance and updates.

## Project Structure

```
Resume/
├── main.tex                 # Main LaTeX document
├── src/                     # Source files
│   ├── constants.tex       # Spacing and formatting constants
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

## Formatting and Spacing

### Spacing Constants

The resume uses centralized spacing constants in `src/constants.tex` for consistent formatting:

- `\experienceItemSpacing`: Space between job title and bullet points (-0.5mm)
- `\sectionEndSpacing`: Space after experience section (-8.5mm)
- `\itemListSpacing`: Space after item lists (1mm)
- `\subheadingSpacing`: Space after subheadings (-2.0mm)

### Quick Spacing Adjustments

For quick spacing changes, use these predefined values:

- `\tightSpacing`: -2.0mm (compact)
- `\normalSpacing`: -0.5mm (balanced)
- `\looseSpacing`: 1.0mm (spacious)

To adjust spacing globally, modify the values in `src/constants.tex` and recompile.

## Version Control

The `.gitignore` file excludes build artifacts and temporary files, keeping only the source files in version control.
