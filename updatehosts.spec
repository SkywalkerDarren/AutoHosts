# -*- mode: python -*-

block_cipher = None


a = Analysis(['updatehosts.py'],
             pathex=['C:\\Users\\yh134\\PycharmProjects\\updatehosts'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='updatehosts',
          debug=False,
          strip=False,
          upx=True,
          console=False )
