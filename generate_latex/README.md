# Generate LaTeX Package

This package provides a modular approach to generating LaTeX files from JSON data for the resume project.

## Structure

```
generate_latex/
├── __init__.py          # Package initialization
├── __main__.py          # Entry point for module execution
├── generator.py          # Main orchestrator
├── utils.py             # Common utility functions
├── experience_generator.py  # Experience LaTeX generation
├── projects_generator.py    # Projects LaTeX generation
├── skills_generator.py      # Skills LaTeX generation
├── education_generator.py   # Education LaTeX generation
└── README.md            # This file
```

## Usage

### As a script

```bash
python3 generate_latex.py
```

### As a module

```bash
python3 -m generate_latex
```

### Programmatically

```python
from generate_latex.generator import generate_all

# Generate all files
generate_all()

# Or with custom paths
generate_all(data_dir="custom_data", src_dir="custom_src")
```

## Modules

### `generator.py`

Main orchestrator that coordinates all generation processes.

### `utils.py`

Common utility functions:

- `load_json_data(file_path)`: Load JSON data from file
- `ensure_directory(path)`: Ensure directory exists

### `experience_generator.py`

Handles experience section generation:

- `generate_experience_files(data, output_dir)`: Generate individual experience files
- `generate_experience_section(data, output_dir)`: Generate main experience.tex

### `projects_generator.py`

Handles projects section generation:

- `generate_project_files(data, output_dir)`: Generate individual project files
- `generate_projects_section(data, output_dir)`: Generate main projects.tex

### `skills_generator.py`

Handles skills section generation:

- `generate_skill_files(data, output_dir)`: Generate individual skill files
- `generate_skills_section(data, output_dir)`: Generate main skills.tex

### `education_generator.py`

Handles education section generation:

- `generate_education_files(data, output_dir)`: Generate individual education files
- `generate_education_section(data, output_dir)`: Generate main education.tex

## Benefits

- **Modularity**: Each section type has its own generator
- **Maintainability**: Easy to modify individual components
- **Reusability**: Functions can be imported and used independently
- **Testability**: Each module can be tested in isolation
- **Extensibility**: Easy to add new section types
