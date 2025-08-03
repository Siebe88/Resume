"""Generate skills LaTeX files from JSON data."""

from pathlib import Path
from .utils import ensure_directory


def generate_skill_files(data, output_dir):
    """Generate individual skill category .tex files from JSON data."""
    output_dir = ensure_directory(output_dir)
    
    for category in data['skillCategories']:
        if category.get('show') == False:
            print(f"Skipped (hidden): {category['id']}")
            continue
            
        filename = f"{category['id']}.tex"
        filepath = output_dir / filename
        
        category_name = category['name'].replace('&', '\\&')
        skills_with_bars = ' | '.join(category['skills'])
        latex_content = f"""\\textbf{{{category_name}:}} \\\\ {skills_with_bars}"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"Generated: {filepath}")


def generate_skills_section(data, output_dir):
    """Generate main skills.tex file that includes visible entries."""
    output_dir = Path(output_dir)
    visible_skills = [skill for skill in data['skillCategories'] if skill.get('show') != False]
    
    # Calculate column width based on number of visible skills
    num_skills = len(visible_skills)
    if num_skills == 0:
        return
    
    # Calculate width per column (leave some margin)
    column_width = 0.95 / num_skills  # 95% of textwidth divided by number of columns
    
    # Create dynamic column specification
    column_spec = ''.join([f'p{{{column_width:.3f}\\textwidth}}' for _ in range(num_skills)])
    
    skills_content = f"""%-----------SKILLS-----------------
\\section{{\\textbf{{Technical Skills}}}}
\\begin{{tabular}}{{{column_spec}}}
"""
    
    # First row: category names
    header_row = []
    for skill in visible_skills:
        skill_name = skill['name'].replace('&', '\\&')
        header_row.append(f"\\textbf{{{skill_name}}}")
    
    skills_content += " & ".join(header_row) + " \\\\\n"
    
    # Second row: skills
    skills_row = []
    for skill in visible_skills:
        skills_text = ', '.join(skill['skills'])
        skills_row.append(skills_text)
    
    skills_content += " & ".join(skills_row) + " \\\\\n"
    
    skills_content += """\\end{tabular}
\\vspace{\\skillsEndSpacing}"""
    
    with open(output_dir / "skills.tex", 'w', encoding='utf-8') as f:
        f.write(skills_content)
    
    print(f"Generated: {output_dir}/skills.tex") 