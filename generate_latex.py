#!/usr/bin/env python3
"""
Generate LaTeX files from JSON data for the resume project.
This script separates data from structure, making it easier to maintain.
"""

import json
import os
from pathlib import Path

def load_json_data(file_path):
    """Load JSON data from file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_experience_files(data, output_dir):
    """Generate individual experience .tex files from JSON data."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for experience in data['experiences']:
        # Skip if show is explicitly set to false
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

def generate_project_files(data, output_dir):
    """Generate individual project .tex files from JSON data."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for project in data['projects']:
        # Skip if show is explicitly set to false
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

def generate_skill_files(data, output_dir):
    """Generate individual skill category .tex files from JSON data."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for category in data['skillCategories']:
        # Skip if show is explicitly set to false
        if category.get('show') == False:
            print(f"Skipped (hidden): {category['id']}")
            continue
            
        filename = f"{category['id']}.tex"
        filepath = output_dir / filename
        
        # Escape & characters for LaTeX
        category_name = category['name'].replace('&', '\\&')
        latex_content = f"""\\textbf{{{category_name}:}} {', '.join(category['skills'])}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"Generated: {filepath}")

def generate_education_files(data, output_dir):
    """Generate individual education .tex files from JSON data."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for education in data['education']:
        # Skip if show is explicitly set to false
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

def generate_section_files(data_dir, src_dir):
    """Generate main section files that only include visible entries."""
    src_dir = Path(src_dir)
    
    # Generate experience.tex
    if (data_dir / "experience.json").exists():
        experience_data = load_json_data(data_dir / "experience.json")
        visible_experiences = [exp for exp in experience_data['experiences'] if exp.get('show') != False]
        
        experience_content = """%-----------EXPERIENCE-----------------
\\section{\\textbf{Experience}}
\\resumeSubHeadingListStart
"""
        for exp in visible_experiences:
            experience_content += f"\\input{{experience/{exp['id']}}}\n"
        
        experience_content += """\\resumeSubHeadingListEnd
\\vspace{\\sectionEndSpacing}"""
        
        with open(src_dir / "experience.tex", 'w', encoding='utf-8') as f:
            f.write(experience_content)
        
        print(f"Generated: {src_dir}/experience.tex")
    
    # Generate projects.tex
    if (data_dir / "projects.json").exists():
        projects_data = load_json_data(data_dir / "projects.json")
        visible_projects = [proj for proj in projects_data['projects'] if proj.get('show') != False]
        
        projects_content = """%-----------PROJECTS-----------------
\\section{\\textbf{Professional Projects}}
\\resumeSubHeadingListStart
"""
        for proj in visible_projects:
            projects_content += f"\\input{{projects/{proj['id']}}}\n"
        
        projects_content += """\\resumeSubHeadingListEnd
\\vspace{\\projectsEndSpacing}"""
        
        with open(src_dir / "projects.tex", 'w', encoding='utf-8') as f:
            f.write(projects_content)
        
        print(f"Generated: {src_dir}/projects.tex")
    
    # Generate skills.tex
    if (data_dir / "skills.json").exists():
        skills_data = load_json_data(data_dir / "skills.json")
        visible_skills = [skill for skill in skills_data['skillCategories'] if skill.get('show') != False]
        
        skills_content = """%-----------SKILLS-----------------
\\section{\\textbf{Technical Skills}}
"""
        for skill in visible_skills:
            skills_content += f"\\input{{skills/{skill['id']}}}\n"
        
        skills_content += """\\vspace{\\skillsEndSpacing}"""
        
        with open(src_dir / "skills.tex", 'w', encoding='utf-8') as f:
            f.write(skills_content)
        
        print(f"Generated: {src_dir}/skills.tex")
    
    # Generate education.tex
    if (data_dir / "education.json").exists():
        education_data = load_json_data(data_dir / "education.json")
        visible_education = [edu for edu in education_data['education'] if edu.get('show') != False]
        
        education_content = """%-----------EDUCATION-----------------
\\section{\\textbf{Education}}
\\resumeSubHeadingListStart
"""
        for edu in visible_education:
            education_content += f"\\input{{education/{edu['id']}}}\n"
        
        education_content += """\\resumeSubHeadingListEnd
\\vspace{\\educationEndSpacing}"""
        
        with open(src_dir / "education.tex", 'w', encoding='utf-8') as f:
            f.write(education_content)
        
        print(f"Generated: {src_dir}/education.tex")

def main():
    """Main function to generate all LaTeX files from JSON data."""
    data_dir = Path("data")
    src_dir = Path("src")
    
    print("Generating LaTeX files from JSON data...")
    
    # Generate experience files
    if (data_dir / "experience.json").exists():
        experience_data = load_json_data(data_dir / "experience.json")
        generate_experience_files(experience_data, src_dir / "experience")
    
    # Generate project files
    if (data_dir / "projects.json").exists():
        projects_data = load_json_data(data_dir / "projects.json")
        generate_project_files(projects_data, src_dir / "projects")
    
    # Generate skill files
    if (data_dir / "skills.json").exists():
        skills_data = load_json_data(data_dir / "skills.json")
        generate_skill_files(skills_data, src_dir / "skills")
    
    # Generate education files
    if (data_dir / "education.json").exists():
        education_data = load_json_data(data_dir / "education.json")
        generate_education_files(education_data, src_dir / "education")
    
    # Generate main section files
    generate_section_files(data_dir, src_dir)
    
    print("LaTeX file generation complete!")

if __name__ == "__main__":
    main() 