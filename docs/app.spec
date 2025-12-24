# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/app.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/templates', 'templates'), ('D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/static', 'static'), ('D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/haarcascade_frontalface_default.xml', '.')],
    hiddenimports=[],
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
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
