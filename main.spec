# -*- mode: python ; coding: utf-8 -*-
import os
import yamllint
from PyInstaller.utils.hooks import collect_submodules

yamllint_path = os.path.dirname(yamllint.__file__)
yamllint_conf = os.path.join(yamllint_path, 'conf')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[(yamllint_conf, 'yamllint/conf')],
    hiddenimports=[
    'yamllint',
    'yamllint.rules.anchors',
    'yamllint.rules.braces',
    'yamllint.rules.colons',
    'yamllint.rules.commas',
    'yamllint.rules.comments',
    'yamllint.rules.comments_indentation',
    'yamllint.rules.document_end',
    'yamllint.rules.document_start',
    'yamllint.rules.empty_lines',
    'yamllint.rules.empty_values',
    'yamllint.rules.float_values',
    'yamllint.rules.hyphens',
    'yamllint.rules.indentation',
    'yamllint.rules.key_duplicates',
    'yamllint.rules.key_ordering',
    'yamllint.rules.line_length',
    'yamllint.rules.new_line_at_end',
    'yamllint.rules.new_lines',
    'yamllint.rules.octal_values',
    'yamllint.rules.quoted_strings',
    'yamllint.rules.trailing_spaces',
    'yamllint.rules.truthy'
],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
