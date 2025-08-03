"""Generate education LaTeX files from JSON data."""

from pathlib import Path
from .utils import ensure_directory


def generate_education_files(data, output_dir):
    """Generate individual education .tex files from JSON data."""
    output_dir = ensure_directory(output_dir)
    
    for education in data['education']:
        if education.get('show') == False:
            print(f"Skipped (hidden): {education['id']}")
            continue
            
        filename = f"{education['id']}.tex"
        filepath = output_dir / filename
        
        latex_content = f"""\\resumeSubheading
  {{{education['institution']}}}{{{education['location']}}}
  {{{education['degree']}}}{{{education['period']}}}
  \\vspace{{\\experienceItemSpacing}}
  \\resumeItemListStart
\\item {education['description']}
  \\resumeItemListEnd
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"Generated: {filepath}")


def generate_education_section(data, output_dir):
    """Generate main education.tex file that includes visible entries."""
    output_dir = Path(output_dir)
    visible_education = [edu for edu in data['education'] if edu.get('show') != False]
    
    education_content = """%-----------EDUCATION-----------------
\\section{\\textbf{Education}}
\\resumeSubHeadingListStart
"""
    for edu in visible_education:
        education_content += f"\\input{{education/{edu['id']}}}\n"
    
    education_content += """\\resumeSubHeadingListEnd
\\vspace{\\educationEndSpacing}"""
    
    with open(output_dir / "education.tex", 'w', encoding='utf-8') as f:
        f.write(education_content)
    
    print(f"Generated: {output_dir}/education.tex") 