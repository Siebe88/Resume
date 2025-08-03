"""Generate experience LaTeX files from JSON data."""

from pathlib import Path
from .utils import ensure_directory


def generate_experience_files(data, output_dir):
    """Generate individual experience .tex files from JSON data."""
    output_dir = ensure_directory(output_dir)
    
    for experience in data['experiences']:
        if experience.get('show') == False:
            print(f"Skipped (hidden): {experience['id']}")
            continue
            
        filename = f"{experience['id']}.tex"
        filepath = output_dir / filename
        
        latex_content = f"""\\resumeSubheading
  {{{experience['company']}}}{{{experience['location']}}}
  {{{experience['title']}}}{{{experience['period']}}}
  \\vspace{{\\experienceItemSpacing}}
  \\resumeItemListStart
"""
        
        for item in experience['items']:
            latex_content += f"\\item {item}\n"
        
        latex_content += "  \\resumeItemListEnd"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"Generated: {filepath}")


def generate_experience_section(data, output_dir):
    """Generate main experience.tex file that includes visible entries."""
    output_dir = Path(output_dir)
    visible_experiences = [exp for exp in data['experiences'] if exp.get('show') != False]
    
    experience_content = """%-----------EXPERIENCE-----------------
\\section{\\textbf{Experience}}
\\resumeSubHeadingListStart
"""
    for exp in visible_experiences:
        experience_content += f"\\input{{experience/{exp['id']}}}\n"
    
    experience_content += """\\resumeSubHeadingListEnd
\\vspace{\\sectionEndSpacing}"""
    
    with open(output_dir / "experience.tex", 'w', encoding='utf-8') as f:
        f.write(experience_content)
    
    print(f"Generated: {output_dir}/experience.tex") 