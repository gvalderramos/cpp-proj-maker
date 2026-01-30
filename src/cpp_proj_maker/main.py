from pathlib import Path
from datetime import datetime
from InquirerPy import inquirer
from cpp_proj_maker.project_config import ProjectConfig
from cpp_proj_maker.project_maker import ProjectMaker

def main():
    proj_config = ProjectConfig()
    proj_config.name = inquirer.text(message="Project Name:", default="MyCppProject").execute()
    proj_config.path = Path(inquirer.text(message="Project Path:", default=".").execute())
    proj_config.description = inquirer.text(message="Project Description:", default="A C++ Project").execute()
    proj_config.cpp_standard = inquirer.select(
        message="C++ Standard:", 
        choices=["11", "14", "17", "20", "23", "26"],
        default="23").execute()
    proj_config.version = inquirer.text(message="Project Version:", default="0.1.0").execute()
    
    if inquirer.confirm(message="Does the project have libraries?", default=False).execute():
        libraries = inquirer.text(message="List libraries (comma-separated):").execute()
        proj_config.libraries = [lib.strip() for lib in libraries.split(",") if lib.strip()]

        common_include = inquirer.select(
            message="Any of these libraries are common?",
            choices=proj_config.libraries + ["None"],
            multiselect=True,
            default="None").execute()
        
        if common_include and "None" not in common_include:
            proj_config.common_libraries = common_include

    if inquirer.confirm(message="Does the project have executables?", default=False).execute():
        executables = inquirer.text(message="List executables (comma-separated):").execute()
        proj_config.executables = [exe.strip() for exe in executables.split(",") if exe.strip()]
    
    proj_config.has_tests = inquirer.confirm(message="Include tests?", default=True).execute()
    proj_config.has_auto_docs = inquirer.confirm(message="Include auto documentation?", default=False).execute()
    proj_config.license_type = inquirer.select(
        message="Select license type:",
        choices=["MIT", "Apache-2.0", "GPL-3.0", "None"],
        default="MIT").execute()
    
    if proj_config.license_type != "None":
        current_year = str(datetime.now().year)
        proj_config.author_name = inquirer.text(message="Author Name:", default="Your Name").execute()
        proj_config.current_year = inquirer.text(message="License Year:", default=current_year).execute()

    proj_maker = ProjectMaker(proj_config)
    proj_maker.create_project_structure()


if __name__ == '__main__':
    main()