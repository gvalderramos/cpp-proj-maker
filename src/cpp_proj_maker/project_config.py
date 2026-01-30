from dataclasses import dataclass, field, asdict
from pathlib import Path


@dataclass
class ProjectConfig:
    name: str = field(default="MyCppProject")
    path: Path = field(default=Path("."))
    description: str = field(default="A C++ Project")
    version: str = field(default="0.1.0")
    cpp_standard: str = field(default="23")
    common_libraries: list[str] = field(default_factory=list)
    libraries: list[str] = field(default_factory=list)
    executables: list[str] = field(default_factory=list)
    has_tests: bool = field(default=True)
    has_auto_docs: bool = field(default=False)
    license_type: str = field(default="MIT")
    author_name: str = field(default="Your Name")
    current_year: str = field(default="2026")

    def as_dict(self) -> dict:
        return asdict(self)
