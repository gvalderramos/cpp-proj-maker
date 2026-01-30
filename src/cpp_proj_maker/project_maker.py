from dataclasses import asdict

from cpp_proj_maker.project_config import ProjectConfig
from jinja2 import Environment, PackageLoader, TemplateNotFound
from pathlib import Path
import subprocess


class ProjectMaker:
    """Create a C++ project structure from templates."""

    def __init__(self, config: ProjectConfig):
        self._config = config
        self._templates = Environment(loader=PackageLoader("cpp_proj_maker", "templates"))

        self._root = Path(self._config.path).resolve()
        self._src_path = self._root / "src"
        self._include_path = self._root / "include"
        self._tests_path = self._root / "tests"
        self._docs_path = self._root / "docs"

    def _render_and_write(self, template_name: str, destination: Path) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            template = self._templates.get_template(template_name)
        except TemplateNotFound:
            raise FileNotFoundError(f"Template not found: {template_name}")

        content = template.render(**asdict(self._config))
        destination.write_text(content)

    def _create_file_from_template(self, template_name: str, destination: Path) -> None:
        self._render_and_write(template_name, destination)

    def _create_file_from_list(self, items: list[str], destination: Path, template_name: str) -> None:
        for item in items:
            item_path = destination / item
            item_path.mkdir(parents=True, exist_ok=True)
            self._render_and_write(template_name, item_path / "CMakeLists.txt")

    def _init_git_repo(self) -> None:
        try:
            subprocess.run(["git", "init", str(self._root)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Warning: git init failed: {e}")

    def _create_license_file(self) -> None:
        if self._config.license_type.lower() == "none":
            return

        license_path = self._root / "LICENSE"
        try:
            self._render_and_write("license_file.txt", license_path)
        except FileNotFoundError as e:
            print(f"Warning: {e}")

    def create_project_structure(self) -> None:
        self._root.mkdir(parents=True, exist_ok=True)
        self._init_git_repo()

        self._create_file_from_template("main_cmake.txt", self._root / "CMakeLists.txt")
        self._create_file_from_template("readme_file.txt", self._root / "README.md")

        if self._config.libraries or self._config.executables:
            self._src_path.mkdir(parents=True, exist_ok=True)
            self._create_file_from_template("sub_cmake.txt", self._src_path / "CMakeLists.txt")
            if self._config.libraries:
                self._create_file_from_list(self._config.libraries, self._src_path, "library_cmake.txt")
            if self._config.executables:
                self._create_file_from_list(self._config.executables, self._src_path, "executable_cmake.txt")

        if self._config.common_libraries:
            self._include_path.mkdir(parents=True, exist_ok=True)
            for lib in self._config.common_libraries:
                (self._include_path / lib).mkdir(parents=True, exist_ok=True)

        if self._config.has_tests:
            self._tests_path.mkdir(parents=True, exist_ok=True)
            self._render_and_write("tests_cmake.txt", self._tests_path / "CMakeLists.txt")
            self._render_and_write("test_cpp_cmake.txt", self._tests_path / "main.cpp")

        if self._config.has_auto_docs:
            self._docs_path.mkdir(parents=True, exist_ok=True)
            self._render_and_write("doc_doxyfile.txt", self._root / "Doxyfile")

        self._create_license_file()
        print("Done creating project structure at:", self._root)