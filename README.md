# cpp-proj-maker

**cpp-proj-maker** is a Python-based CLI tool that **bootstraps modern C++ project structures** with CMake, tests, documentation, and sensible defaults — so you can stop rewriting the same boilerplate over and over.

It’s designed to be:
* ⚡ Fast to use
* 🧱 Opinionated but flexible
* 📦 Easy to distribute as a single executable
* 🛠 Friendly to real-world C++ projects (libraries, executables, tests, docs)

##✨ Features

* Generate C++ executable or library projects
* CMake project structure out of the box
* Ready-to-use templates for:
  * CMakeLists.txt
  * subdirectories
  * tests
  * README
  * license file
  * Doxygen config
* Jinja2-powered templates (easy to customize)
* Works as:
  * Python module
  * Standalone executable (PyInstaller)

## 📁 Project Structure
```bash
cpp-proj-maker/
├─ src/
│  └─ cpp_proj_maker/
│     ├─ main.py
│     ├─ project_maker.py
│     ├─ project_config.py
│     └─ templates/
│        ├─ main_cmake.txt
│        ├─ executable_cmake.txt
│        ├─ library_cmake.txt
│        ├─ tests_cmake.txt
│        ├─ sub_cmake.txt
│        ├─ test_cpp_cmake.txt
│        ├─ readme_file.txt
│        ├─ license_file.txt
│        └─ doc_doxyfile.txt
├─ tests/
├─ pyproject.toml
└─ README.md
```

## 🚀 Installation
Option 1 — Run with Poetry (recommended for development)
```bash
poetry install
poetry run cpp-proj-maker
```

Option 2 — Standalone executable (no Python required)
Download the prebuilt executable from the Releases page
(or build it yourself with PyInstaller).

## 🧑‍💻 Usage

Basic example:
```bash
$> cpp-proj-maker
? Project Name: MyCppProject
? Project Path: c:\dev\temp\final-proj-test-01
? Project Description: A C++ Project
? C++ Standard: 26
? Project Version: 0.1.0
? Does the project have libraries? No
? Does the project have executables? Yes
? List executables (comma-separated): MyCppProject
? Include tests? Yes
? Include auto documentation? Yes
? Select license type: MIT
? Author Name: Gabriel Valderramos
? License Year: 2026
```

## Example output structure:
```bash
MyCppProject/
├─ CMakeLists.txt
├─ Doxyfile
├─ src/
│  └─ MyCppProject/
│    └─ main.cpp
├─ tests/
│  └─ CMakeLists.txt
│  └─ main.cpp
├─ docs/
└─ README.md
```

## 🧩 Templates

All generated files are based on Jinja2 templates located in:
`cpp_proj_maker/templates/`


## 🛠 Development
### Run tests
```bash
poetry run pytest
```
### Build executable (Windows example)
```bash
poetry run pyinstaller cpp-proj-maker.spec
```

### Output:
```bash
dist/cpp-proj-maker.exe
```

## 📦 Packaging details

Uses Poetry for dependency management

Uses PyInstaller for standalone builds

Templates are bundled via Python package data

Jinja2 loads templates using PackageLoader (PyInstaller-safe)

## 🧠 Why this exists

CMake projects tend to start the same way — but everyone rewrites them manually.

This tool exists to:
* reduce setup friction
* enforce consistency
* let you focus on actual C++ code

## 📌 Roadmap (ideas)

* Presets (game engine, library-only, header-only)
* Conan / vcpkg integration
* Toolchain presets
* Custom template packs
* add dependencies


## 📄 License
MIT License (see LICENSE file).

## 🤝 Contributing
PRs, issues, and suggestions are welcome.
This project is meant to evolve with real-world usage.
