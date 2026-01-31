from pathlib import Path
import tempfile

import pytest
from jinja2 import Environment, DictLoader

from cpp_proj_maker.project_config import ProjectConfig
from cpp_proj_maker.project_maker import ProjectMaker



@pytest.fixture
def cfg() -> ProjectConfig:
    tmp_path = Path(tempfile.mkdtemp())
    cfg = ProjectConfig()
    cfg.name = "TestProj"
    cfg.path = tmp_path
    cfg.description = "A test C++ project"
    cfg.cpp_standard = "20"
    cfg.version = "0.2.0"
    cfg.libraries = ["libA", "libB"]
    cfg.executables = ["app"]
    cfg.common_libraries = ["libA"]
    cfg.has_tests = True
    cfg.has_auto_docs = True
    cfg.license_type = "MIT"
    cfg.author_name = "Tester"
    cfg.current_year = "2099"
    return cfg


def templates() -> Environment:
    # Minimal templates that reference common fields for assertions
    templates = {
        "main_cmake.txt": "# Project CMake: {{ name }}\n",
        "readme_file.txt": "# {{ name }}\n{{ description }}\n",
        "sub_cmake.txt": "# Subdir CMake for {{ name }}\n",
        "library_cmake.txt": "# Library {{ target_name }} - {{ cpp_standard }}\n",
        "executable_cmake.txt": "# Executable {{ target_name }}\n",
        "tests_cmake.txt": "# Tests for {{ name }}\n",
        "test_cpp_cmake.txt": "// test main for {{ name }}\n",
        "doc_doxyfile.txt": "# Doxygen for {{ name }}\n",
        "license_file.txt": "{{ author_name }} - {{ current_year }}\n",
    }
    return Environment(loader=DictLoader(templates))


def test_project_config_as_dict_defaults(cfg: ProjectConfig):
    d = cfg.as_dict()
    assert isinstance(d, dict)
    assert d["name"] == "TestProj"
    assert d["cpp_standard"] == "20"

@pytest.mark.parametrize("tmp_path", [Path(tempfile.mkdtemp())])
def test_project_maker_creates_structure(cfg, tmp_path: Path):
    cfg.name = "TestProj"
    cfg.path = tmp_path
    cfg.description = "A test C++ project"
    cfg.cpp_standard = "20"
    cfg.version = "0.2.0"
    cfg.libraries = ["libA", "libB"]
    cfg.executables = ["app"]
    cfg.common_libraries = ["libA"]
    cfg.has_tests = True
    cfg.has_auto_docs = True
    cfg.license_type = "MIT"
    cfg.author_name = "Tester"
    cfg.current_year = "2099"

    maker = ProjectMaker(cfg)
    # inject a lightweight in-memory template environment
    maker._templates = templates()

    maker.create_project_structure()

    # root files
    readme = tmp_path / "README.md"
    assert readme.exists()
    assert "TestProj" in readme.read_text()

    cmake = tmp_path / "CMakeLists.txt"
    assert cmake.exists()
    assert "TestProj" in cmake.read_text()

    # src and library directories
    src = tmp_path / "src"
    assert src.exists()
    assert (src / "libA" / "CMakeLists.txt").exists()
    assert (src / "libB" / "CMakeLists.txt").exists()
    assert (src / "app" / "CMakeLists.txt").exists()
    for target in ["libA", "libB", "app"]:
        target_cmake = (src / target / "CMakeLists.txt").read_text()
        assert target in target_cmake
        assert "20" in target_cmake if "lib" in target else True

    # include common libraries
    include_lib = tmp_path / "include" / "libA"
    assert include_lib.exists()

    # tests
    tests_cmake = tmp_path / "tests" / "CMakeLists.txt"
    tests_main = tmp_path / "tests" / "main.cpp"
    assert tests_cmake.exists()
    assert tests_main.exists()

    # docs
    doxy = tmp_path / "Doxyfile"
    assert doxy.exists()

    # license
    license_path = tmp_path / "LICENSE"
    assert license_path.exists()
    assert "Tester" in license_path.read_text()
