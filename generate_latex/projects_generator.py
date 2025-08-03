"""Generate project LaTeX files from JSON data."""

from pathlib import Path
from .utils import ensure_directory


def generate_project_files(data, output_dir):
    """Generate individual project .tex files from JSON data."""
    output_dir = ensure_directory(output_dir)
    
    for project in data['projects']:
        if project.get('show') == False:
            print(f"Skipped (hidden): {project['id']}")
            continue
            
        filename = f"{project['id']}.tex"
        filepath = output_dir / filename
        
        latex_content = f"""\\resumeSubheading
  {{{project['name']}}}{{{', '.join(project['technologies'])}}}
  {{{project['description']}}}{{""}}
  \\vspace{{\\experienceItemSpacing}}
  \\resumeItemListStart
"""
        
        for item in project['items']:
            latex_content += f"\\item {item}\n"
        
        latex_content += "  \\resumeItemListEnd"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"Generated: {filepath}")


def generate_projects_section(data, output_dir):
    """Generate main projects.tex file that includes visible entries."""
    output_dir = Path(output_dir)
    visible_projects = [proj for proj in data['projects'] if proj.get('show') != False]
    
    projects_content = """%-----------PROJECTS-----------------
\\section{\\textbf{Professional Projects}}
\\resumeSubHeadingListStart
"""
    for proj in visible_projects:
        projects_content += f"\\input{{projects/{proj['id']}}}\n"
    
    projects_content += """\\resumeSubHeadingListEnd
\\vspace{\\projectsEndSpacing}"""
    
    with open(output_dir / "projects.tex", 'w', encoding='utf-8') as f:
        f.write(projects_content)
    
    print(f"Generated: {output_dir}/projects.tex") 