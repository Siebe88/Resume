# Professional Resume

A data-driven LaTeX resume with separated content and structure.

## Structure

- **`data/`** - JSON files containing all resume content
- **`src/`** - LaTeX templates and generated files
- **`build/`** - Generated PDF output

## Data Files

- `data/experience.json` - Work experience entries
- `data/projects.json` - Project portfolio
- `data/skills.json` - Skills organized by category
- `data/education.json` - Education history

## Quick Start

### Using Docker Compose (Recommended)

```bash
docker-compose up --build
```

This will:

1. Generate LaTeX files from JSON data
2. Compile the resume PDF
3. Output the result to `build/`

### Manual Generation

```bash
# Generate LaTeX files from JSON data
python generate_latex.py

# Compile PDF (requires LaTeX installation)
pdflatex -output-directory=build src/main.tex
```

## Adding Content

### Experience

Edit `data/experience.json`:

```json
{
  "id": "company-name",
  "company": "Company Name",
  "location": "Location",
  "title": "Job Title",
  "period": "2020 - Present",
  "show": true,
  "items": ["Achievement 1", "Achievement 2"]
}
```

### Projects

Edit `data/projects.json`:

```json
{
  "id": "project-name",
  "name": "Project Name",
  "description": "Brief description",
  "technologies": ["Tech1", "Tech2"],
  "show": true,
  "items": ["Key accomplishment 1", "Key accomplishment 2"]
}
```

### Skills

Edit `data/skills.json`:

```json
{
  "id": "category-name",
  "name": "Category Name",
  "show": true,
  "skills": ["Skill1", "Skill2", "Skill3"]
}
```

## Show/Hide Functionality

Each entry in the JSON files has a `show` property that controls visibility:

- `"show": true` - Entry will be included in the resume (default)
- `"show": false` - Entry will be hidden from the resume

This allows you to:

- Create different resume versions for different roles
- Temporarily hide content without deleting it
- Maintain a complete database of all experiences/projects

## Benefits

- **Separation of Concerns**: Data and presentation are separate
- **Easy Maintenance**: Update content without touching LaTeX
- **Version Control**: JSON files are easier to diff and merge
- **Consistency**: Structured data ensures formatting consistency
- **Automation**: Scripts handle file generation automatically
- **Flexible Visibility**: Show/hide content without deletion

## File Structure

```
Resume/
├── data/                    # JSON data files
│   ├── experience.json
│   ├── projects.json
│   ├── skills.json
│   └── education.json
├── src/                     # LaTeX source files
│   ├── main.tex            # Main document
│   ├── constants.tex       # Formatting constants
│   ├── experience/         # Generated experience files
│   ├── projects/           # Generated project files
│   ├── skills/             # Generated skill files
│   └── education/          # Generated education files
├── build/                  # Generated PDF output
├── generate_latex.py       # Data to LaTeX converter
├── docker-compose.yml      # Docker setup
└── Dockerfile              # Container definition
```
