# -*- mode: python -*-
a = Analysis(['[--onefile]', 'test/calc.py'],
             pathex=['/Users/SeungWoo_0914/MyFuture/Columbia/PLT/PLT-SLAMM/pyinstaller-2.0'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.darwin/[--onefile]', '[--onefile]'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', '[--onefile]'))
