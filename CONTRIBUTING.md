# Introduction
**cpp-proj-maker** is a Python-based CLI tool that **bootstraps modern C++ project structures** with CMake, tests, documentation, and sensible defaults — so you can stop rewriting the same boilerplate over and over.

# Ways to Contribute
Before starting, please check the **Issues** tab to see if someone is already working on your idea or feature.

If not, feel free to:
1. Open a new issue to discuss your idea
2. Fork this repository
3. Create your changes
4. Submit a Pull Request for review

# Development Setup
You should have at least **Python >= 3.10 and < 3.15**.
You also need to have the [Poetry](https://python-poetry.org/docs/) installed.

Then, to run this repository is quite simple, you need just:
```bash
git clone <forked-repository.git>
poetry install
poetry run cpp-proj-maker
```

# Running Tests
After cloned and poetry installed, you can run:
```bash
poetry run pytest
```

# Project Structure
```bash
cpp-proj-maker/
├─ src/
│  └─ cpp_proj_maker/  <-- Main python library
│     └─ templates/    <-- Jinja templates
└─ tests/              <-- Unit tests
```

# Coding Guidelines

> _if I have seen further (than others), it is by standing on the shoulders of giants._
— Isaac Newton

Just be kind and friendly. If you know more, help the community with your knowledge. We together can go further.

In terms of code, I always tend to aim in the **PIP 8** and also ``black`` formating. Keep the code simple and with small changes that will contribute to a code more stable and secure.

You can also check the **CODE_OF_CONDUCT.md** for more info.

# Pull Request Guidelines

Your PR description should include:

* What this PR does
* Why the change is needed
* How it was tested

### Example:
```
What:
- Adds support for generating static libraries

Why:
- Needed to support common CMake workflows

Testing:
- Added unit tests
- Manually tested CLI on Windows and Linux
```
