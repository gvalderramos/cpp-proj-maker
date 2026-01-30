# cpp-proj-maker.spec
# -*- mode: python ; coding: utf-8 -*-
import sys

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Collect templates inside cpp_proj_maker/templates
datas = collect_data_files(
    "cpp_proj_maker",
    includes=["templates/*.txt"]
)

hiddenimports = collect_submodules("cpp_proj_maker")

a = Analysis(
    ["src/cpp_proj_maker/main.py"],
    pathex=["src"],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=f"cpp-proj-maker-{sys.platform}",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,   # set False if you want GUI
)
