"""Main generator module that orchestrates LaTeX file generation."""

from pathlib import Path
from .utils import load_json_data
from .experience_generator import generate_experience_files, generate_experience_section
from .projects_generator import generate_project_files, generate_projects_section
from .skills_generator import generate_skills_section
from .education_generator import generate_education_files, generate_education_section


def generate_section_files(data_dir, src_dir):
    """Generate main section files that only include visible entries."""
    src_dir = Path(src_dir)
    
    if (data_dir / "experience.json").exists():
        experience_data = load_json_data(data_dir / "experience.json")
        generate_experience_section(experience_data, src_dir)
    
    if (data_dir / "projects.json").exists():
        projects_data = load_json_data(data_dir / "projects.json")
        generate_projects_section(projects_data, src_dir)
    
    if (data_dir / "skills.json").exists():
        skills_data = load_json_data(data_dir / "skills.json")
        generate_skills_section(skills_data, src_dir)
    
    if (data_dir / "education.json").exists():
        education_data = load_json_data(data_dir / "education.json")
        generate_education_section(education_data, src_dir)


def generate_all(data_dir="data", src_dir="src"):
    """Generate all LaTeX files from JSON data."""
    data_dir = Path(data_dir)
    src_dir = Path(src_dir)
    
    print("Generating LaTeX files from JSON data...")
    
    if (data_dir / "experience.json").exists():
        experience_data = load_json_data(data_dir / "experience.json")
        generate_experience_files(experience_data, src_dir / "experience")
    
    if (data_dir / "projects.json").exists():
        projects_data = load_json_data(data_dir / "projects.json")
        generate_project_files(projects_data, src_dir / "projects")
    
    if (data_dir / "education.json").exists():
        education_data = load_json_data(data_dir / "education.json")
        generate_education_files(education_data, src_dir / "education")
    
    generate_section_files(data_dir, src_dir)
    
    print("LaTeX file generation complete!") 